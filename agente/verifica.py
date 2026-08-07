# -*- coding: utf-8 -*-
"""
MEMETECA — controllo preliminare.

Verifica, prima del primo post vero, che ci sia davvero tutto:
credenziali valide, permessi giusti, immagini raggiungibili, caption a norma.

    python verifica.py

Esce con codice 0 se è tutto a posto, 1 se qualcosa manca.
"""
import os
import sys

import requests

# La console di Windows usa cp1252 e non sa stampare i caratteri accentati o i
# tratti di separazione: senza questo, il controllo muore su una riga di grafica.
for flusso in (sys.stdout, sys.stderr):
    if hasattr(flusso, "reconfigure"):
        flusso.reconfigure(encoding="utf-8", errors="replace")

from contenuti import (LIMITE_INSTAGRAM, MARGINE, MEMI,
                       costruisci_caption, lunghezza_instagram)
from instagram import Instagram, ErrorePubblicazione

OK, KO, ATT = "  OK  ", " ERR  ", " ATT  "
problemi = []


def esito(stato, titolo, dettaglio=""):
    print(f"[{stato}] {titolo}" + (f"\n         {dettaglio}" if dettaglio else ""))
    if stato == KO:
        problemi.append(titolo)


def main():
    print("\nMEMETECA — controllo preliminare\n" + "─" * 62)

    token = os.environ.get("IG_ACCESS_TOKEN")
    base = (os.environ.get("MEMETECA_BASE_URL") or "").rstrip("/")
    api = os.environ.get("MEMETECA_API", "instagram")

    esito(OK if token else KO, "variabile IG_ACCESS_TOKEN",
          "" if token else "non impostata")
    esito(OK if base else KO, "variabile MEMETECA_BASE_URL",
          "" if base else "non impostata")
    esito(OK, "strada scelta",
          "Instagram Login (nessuna Pagina Facebook richiesta)" if api == "instagram"
          else "Facebook Login (richiede una Pagina collegata)")
    if not (token and base):
        print("\nManca qualche credenziale: vedi docs/05_COSA_DEVI_FARE_TU.md\n")
        return 1

    ig = Instagram()

    # account raggiungibile
    try:
        p = ig.profilo()
        esito(OK, "account Instagram", f"@{p.get('username')} (id {p.get('id')})")
    except Exception as e:
        esito(KO, "account Instagram", str(e))

    # scadenza del token
    try:
        g = ig.giorni_alla_scadenza()
        if g is None:
            esito(ATT, "token", "scadenza non determinabile")
        else:
            esito(OK if g > 10 else ATT, "token", f"valido ancora {g} giorni")
    except Exception as e:
        esito(KO, "token", str(e))

    # quota di pubblicazione
    try:
        esito(OK, "quota giornaliera", f"{ig.quota_residua()} post ancora disponibili")
    except Exception as e:
        esito(ATT, "quota giornaliera", str(e))

    # le immagini devono essere pubbliche: la Graph API le scarica da sola
    da_provare = [f"{base}/{m['num']}_{i}.jpg" for m in MEMI[:2] for i in (1, 2, 3)]
    irraggiungibili = []
    for url in da_provare:
        try:
            r = requests.head(url, timeout=20, allow_redirects=True)
            if r.status_code != 200:
                irraggiungibili.append(f"{url} → HTTP {r.status_code}")
        except Exception as e:
            irraggiungibili.append(f"{url} → {e}")
    esito(OK if not irraggiungibili else KO, "immagini pubbliche",
          f"{len(da_provare)} controllate, tutte raggiungibili" if not irraggiungibili
          else "\n         ".join(irraggiungibili[:3]))

    # caption entro il limite Instagram
    soglia = LIMITE_INSTAGRAM - MARGINE
    lunghe = [(m["num"], lunghezza_instagram(costruisci_caption(m))) for m in MEMI
              if lunghezza_instagram(costruisci_caption(m)) > soglia]
    massima = max(lunghezza_instagram(costruisci_caption(m)) for m in MEMI)
    esito(OK if not lunghe else KO, "caption",
          f"{len(MEMI)} schede, la più lunga {massima} caratteri su {LIMITE_INSTAGRAM}"
          if not lunghe else f"oltre la soglia di sicurezza ({soglia}): {lunghe}")

    print("─" * 62)
    if problemi:
        print(f"\n{len(problemi)} problemi da sistemare: " + ", ".join(problemi) + "\n")
        return 1
    print("\nTutto a posto. Il primo post può partire:")
    print("    python pubblica.py pubblica\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
