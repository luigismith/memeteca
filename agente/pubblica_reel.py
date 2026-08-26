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
    # ATTENZIONE pero': il vincolo vero NON e' l'URL, e' il budget di
    # elaborazione video dell'account. Il 24 e il 25 agosto lo stesso schema:
    # i primi container passano, poi TUTTI falliscono con un secco ERROR,
    # anche su percorsi mai usati e con file identici a quelli appena
    # accettati. Ogni tentativo consuma budget — LA PROVA ANCHE. Quindi:
    # un tentativo per volta, ben distanziato, e mai una prova sul file che
    # si intende pubblicare davvero.
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
