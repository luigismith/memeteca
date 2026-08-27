# -*- coding: utf-8 -*-
"""
MEMETECA — pubblica il Reel di una scheda via API.

Il video sta in assets/reel_<num>.mp4 nel repository (servito da GitHub
Pages) e contiene gia' la traccia musicale originale generata da musica.py:
niente libreria di Instagram, niente rights management.

    python pubblica_reel.py 021
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import datetime as dt
import json
import os
import pathlib
import sys

from contenuti import BRAND, MEMI
from instagram import Instagram

QUI = pathlib.Path(__file__).parent
STATO = QUI / "stato.json"
SUFFISSO_FILE = "_v5"


def caption_reel(m):
    """Breve, diversa dal carosello: gancio, richiamo, 5 hashtag."""
    return (f"{m['hook']}\n\n"
            f"La scheda completa — date, fonti e cos'e' successo dopo — "
            f"e' sul profilo.\n\n"
            f"Segui {BRAND['handle']}\n\n"
            f"{m['hashtags']}")


def main(num, prova=False, url=None):
    m = next((x for x in MEMI if x["num"] == num), None)
    if not m:
        sys.exit(f"scheda {num} non trovata")

    base = os.environ.get("MEMETECA_BASE_URL", "").rstrip("/")
    if not (base or url):
        sys.exit("serve MEMETECA_BASE_URL")
    # Il percorso si versiona perche' un URL gia' rifiutato resta rifiutato.
    #
    # LA TEORIA DEL «BUDGET VIDEO» ERA SBAGLIATA. Il 24 e il 25 agosto, dopo
    # una ventina di container tutti finiti in ERROR, avevamo scritto qui che
    # il vincolo era un budget di elaborazione video dell'account, e che
    # anche --prova lo consumasse. Il 27 agosto 2026 diagnosi_reel.py ha
    # chiesto il dato all'API invece di dedurlo:
    #
    #   content_publishing_limit → quota_total 100 / 24h, quota_usage 1
    #
    # Uno su cento. Il budget non c'entrava niente: i tentativi falliti non
    # consumano quota, perche' la quota conta le pubblicazioni riuscite.
    # Distanziare i tentativi non serviva, e la regola «mai una prova sul
    # file vero» era una precauzione contro un vincolo inesistente.
    #
    # Quello che la stessa diagnosi ha trovato davvero:
    #   · account_type MEDIA_CREATOR, 34 media, di cui 33 CAROUSEL_ALBUM in
    #     FEED e UNO solo VIDEO/REELS — quell'uno caricato dal telefono. Via
    #     API non e' mai passato niente.
    #   · assets/reel_021_v5.mp4 e' a norma: 720x1280, 27,5 s, avc1 + mp4a,
    #     nessuna edit list, moov in testa. Servito da GitHub Pages con
    #     Content-Type video/mp4 e HTTP 200.
    #
    # Cioe': il file va bene, l'URL va bene, la quota e' libera, e i reel
    # falliscono lo stesso. Resta un'ipotesi sola, ed e' strutturale: la
    # pubblicazione di REELS non e' aperta a questo account per la strada
    # Instagram Login (graph.instagram.com, senza Pagina Facebook), dove
    # invece i caroselli passano da sempre. Non e' una cosa che si aggiusta
    # ritentando.
    #
    # REGOLA: non si ricopia il file su un percorso nuovo, non si riprova.
    # I reel si caricano dal telefono, che e' come funzionava prima e
    # funzionava. Se un giorno si vuole riaprire la strada API, la prova da
    # fare e' un'altra: collegare una Pagina Facebook e passare a
    # MEMETECA_API=facebook, non un ventunesimo tentativo identico.
    video = url or f"{base}/assets/reel_{num}{SUFFISSO_FILE}.mp4"

    s = json.loads(STATO.read_text(encoding="utf-8"))
    fatti = {r.get("num") for r in s.get("reel", [])}
    if num in fatti and not prova:
        print(f"il reel della {num} risulta gia' pubblicato")
        return

    if prova:
        # crea il contenitore e aspetta la validazione, SENZA pubblicare:
        # serve a collaudare video e hosting senza sporcare il profilo.
        ig = Instagram()
        c = ig._post(f"{ig.ig_user_id}/media", media_type="REELS",
                     video_url=video, caption="prova")["id"]
        ig._attendi_pronto(c, tentativi=60, pausa=6)
        print(f"PROVA OK: il video {video} passa la validazione (contenitore {c}, non pubblicato)")
        return

    print(f"video: {video}")
    post_id = Instagram().pubblica_reel(video, caption_reel(m))

    # lo stato si salva subito, come per le schede
    s.setdefault("reel", []).append({
        "num": num, "post_id": post_id,
        "quando": dt.datetime.now(dt.timezone.utc).isoformat(),
        "canale": "github actions (api, musica originale)"})
    STATO.write_text(json.dumps(s, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8", newline="\n")
    print(f"Pubblicato reel {num} — {m['titolo']} (post {post_id})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: python pubblica_reel.py <numero> [--prova] [--url URL]")
    url = None
    if "--url" in sys.argv:
        url = sys.argv[sys.argv.index("--url") + 1]
    main(sys.argv[1].zfill(3), prova="--prova" in sys.argv, url=url)
