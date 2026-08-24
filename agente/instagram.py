# -*- coding: utf-8 -*-
"""
MEMETECA — pubblicazione su Instagram.

Supporta le due strade possibili:

  1. INSTAGRAM LOGIN (predefinita, e molto più semplice)
     Host: graph.instagram.com — NON serve una Pagina Facebook.
     Permessi: instagram_business_basic + instagram_business_content_publish
     Il token è legato all'account, quindi l'id utente può restare "me".
     Dura 60 giorni ed è rinnovabile all'infinito senza app secret.

  2. FACEBOOK LOGIN (la vecchia strada)
     Host: graph.facebook.com — richiede una Pagina Facebook collegata.
     Permessi: instagram_basic + instagram_content_publish + pages_read_engagement
     Si attiva con MEMETECA_API=facebook.

Limite Meta in entrambi i casi: 50 pubblicazioni ogni 24 ore.

NOTA: la Graph API non accetta upload di file. Scarica le immagini da un URL
pubblico, quindi le slide devono essere raggiungibili via HTTP.
"""
import os
import time

import requests

HOST_INSTAGRAM = "https://graph.instagram.com"
HOST_FACEBOOK = "https://graph.facebook.com/v21.0"


class ErrorePubblicazione(RuntimeError):
    pass


class Instagram:
    def __init__(self, ig_user_id=None, token=None, api=None, timeout=60):
        self.token = token or os.environ["IG_ACCESS_TOKEN"]
        self.api = (api or os.environ.get("MEMETECA_API", "instagram")).lower()
        self.host = HOST_FACEBOOK if self.api == "facebook" else HOST_INSTAGRAM
        # Con Instagram Login il token è già legato all'account: "me" basta.
        self.ig_user_id = ig_user_id or os.environ.get("IG_USER_ID") or "me"
        self.timeout = timeout

    # ---------------------------------------------------------------- interno
    def _post(self, percorso, **dati):
        dati["access_token"] = self.token
        r = requests.post(f"{self.host}/{percorso}", data=dati, timeout=self.timeout)
        corpo = r.json() if r.content else {}
        if r.status_code >= 400 or "error" in corpo:
            raise ErrorePubblicazione(f"{r.status_code} — {corpo.get('error', corpo)}")
        return corpo

    def _get(self, percorso, **params):
        params["access_token"] = self.token
        r = requests.get(f"{self.host}/{percorso}", params=params, timeout=self.timeout)
        corpo = r.json() if r.content else {}
        if r.status_code >= 400 or "error" in corpo:
            raise ErrorePubblicazione(f"{r.status_code} — {corpo.get('error', corpo)}")
        return corpo

    def _attendi_pronto(self, creation_id, tentativi=30, pausa=4):
        """La Graph API elabora i media in modo asincrono."""
        for _ in range(tentativi):
            stato = self._get(creation_id, fields="status_code")["status_code"]
            if stato == "FINISHED":
                return True
            if stato == "ERROR":
                raise ErrorePubblicazione(f"Media {creation_id} in errore")
            time.sleep(pausa)
        raise ErrorePubblicazione(f"Timeout in elaborazione per {creation_id}")

    # ---------------------------------------------------------------- pubblico
    def profilo(self):
        campi = ("id,username" if self.api == "instagram"
                 else "id,username,followers_count")
        return self._get(self.ig_user_id, fields=campi)

    def quota_residua(self):
        d = self._get(f"{self.ig_user_id}/content_publishing_limit",
                      fields="quota_usage,config")
        voce = d.get("data", [{}])[0]
        return voce.get("config", {}).get("quota_total", 50) - voce.get("quota_usage", 0)

    def pubblica_carosello(self, url_immagini, caption):
        """Pubblica un carosello (2-10 immagini). Ritorna l'id del post."""
        if not 2 <= len(url_immagini) <= 10:
            raise ValueError("Un carosello richiede da 2 a 10 immagini")

        figli = []
        for url in url_immagini:
            c = self._post(f"{self.ig_user_id}/media",
                           image_url=url, is_carousel_item="true")["id"]
            figli.append(c)
        for c in figli:
            self._attendi_pronto(c)

        contenitore = self._post(f"{self.ig_user_id}/media",
                                 media_type="CAROUSEL",
                                 children=",".join(figli),
                                 caption=caption)["id"]
        self._attendi_pronto(contenitore)
        return self._post(f"{self.ig_user_id}/media_publish",
                          creation_id=contenitore)["id"]

    def pubblica_singola(self, url_immagine, caption):
        c = self._post(f"{self.ig_user_id}/media",
                       image_url=url_immagine, caption=caption)["id"]
        self._attendi_pronto(c)
        return self._post(f"{self.ig_user_id}/media_publish", creation_id=c)["id"]

    def pubblica_reel(self, url_video, caption):
        """Pubblica un Reel da un video mp4 raggiungibile pubblicamente.
        I video vengono elaborati piu' lentamente delle immagini: l'attesa
        e' piu' lunga di proposito."""
        c = self._post(f"{self.ig_user_id}/media",
                       media_type="REELS", video_url=url_video,
                       caption=caption)["id"]
        self._attendi_pronto(c, tentativi=60, pausa=6)
        return self._post(f"{self.ig_user_id}/media_publish", creation_id=c)["id"]

    def commenta(self, post_id, testo):
        """Utile per mettere le fonti estese nel primo commento."""
        return self._post(f"{post_id}/comments", message=testo)["id"]

    # ---------------------------------------------------- commenti in entrata
    # L'API di Instagram permette di gestire SOLO i commenti sui propri post.
    # Non esiste alcun endpoint per seguire account o commentare post altrui:
    # Meta non lo espone di proposito, ed è una scelta anti-spam.
    def post_recenti(self, quanti=10):
        d = self._get(f"{self.ig_user_id}/media",
                      fields="id,caption,timestamp,permalink", limit=quanti)
        return d.get("data", [])

    def commenti(self, media_id):
        d = self._get(f"{media_id}/comments",
                      fields="id,text,username,timestamp,replies{id,text,username}")
        return d.get("data", [])

    def rispondi(self, comment_id, testo):
        return self._post(f"{comment_id}/replies", message=testo)["id"]

    def nascondi(self, comment_id, nascosto=True):
        """Per gli insulti: nascondere è meglio che cancellare — chi l'ha
        scritto continua a vederlo e non riprova."""
        return self._post(comment_id, hide="true" if nascosto else "false")

    def da_rispondere(self, quanti_post=6):
        """I commenti sui nostri post a cui non abbiamo ancora risposto."""
        mio = self.profilo().get("username", "")
        aperti = []
        for m in self.post_recenti(quanti_post):
            for c in self.commenti(m["id"]):
                if c.get("username") == mio:
                    continue
                risposte = (c.get("replies") or {}).get("data", [])
                if any(r.get("username") == mio for r in risposte):
                    continue
                aperti.append({"media": m.get("permalink"), "id": c["id"],
                               "chi": c.get("username"), "testo": c.get("text"),
                               "quando": c.get("timestamp")})
        return aperti

    # ------------------------------------------------------------- scadenza
    def giorni_alla_scadenza(self):
        """Ritorna i giorni residui, o None se non determinabile."""
        if self.api == "instagram":
            d = requests.get(f"{HOST_INSTAGRAM}/refresh_access_token",
                             params={"grant_type": "ig_refresh_token",
                                     "access_token": self.token},
                             timeout=self.timeout).json()
            if "expires_in" in d:
                return d["expires_in"] // 86400
            return None
        d = requests.get("https://graph.facebook.com/debug_token",
                         params={"input_token": self.token,
                                 "access_token": self.token},
                         timeout=self.timeout).json().get("data", {})
        scad = d.get("expires_at", 0)
        if not scad:
            return None
        return int((scad - time.time()) // 86400)

    def rinnova(self):
        """Solo per Instagram Login: prolunga di altri 60 giorni.
        Ritorna il nuovo token. Non serve l'app secret."""
        if self.api != "instagram":
            raise ErrorePubblicazione(
                "Il rinnovo automatico esiste solo con Instagram Login. "
                "Con Facebook Login rigenera il token dalla dashboard.")
        d = requests.get(f"{HOST_INSTAGRAM}/refresh_access_token",
                         params={"grant_type": "ig_refresh_token",
                                 "access_token": self.token},
                         timeout=self.timeout).json()
        if "access_token" not in d:
            raise ErrorePubblicazione(f"Rinnovo fallito: {d}")
        return d["access_token"], d.get("expires_in", 0) // 86400


if __name__ == "__main__":
    import sys
    ig = Instagram()
    if len(sys.argv) > 1 and sys.argv[1] == "rinnova":
        nuovo, giorni = ig.rinnova()
        print(nuovo)
        print(f"# valido altri {giorni} giorni", file=sys.stderr)
    else:
        print(ig.profilo())
