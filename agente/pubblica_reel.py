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


def caption_reel(m):
    """Breve, diversa dal carosello: gancio, richiamo, 5 hashtag."""
    return (f"{m['hook']}\n\n"
            f"La scheda completa — date, fonti e cos'e' successo dopo — "
            f"e' sul profilo.\n\n"
            f"Segui {BRAND['handle']}\n\n"
            f"{m['hashtags']}")


def main(num):
    m = next((x for x in MEMI if x["num"] == num), None)
    if not m:
        sys.exit(f"scheda {num} non trovata")

    base = os.environ.get("MEMETECA_BASE_URL", "").rstrip("/")
    if not base:
        sys.exit("serve MEMETECA_BASE_URL")
    video = f"{base}/assets/reel_{num}.mp4"

    s = json.loads(STATO.read_text(encoding="utf-8"))
    fatti = {r.get("num") for r in s.get("reel", [])}
    if num in fatti:
        print(f"il reel della {num} risulta gia' pubblicato")
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
        sys.exit("uso: python pubblica_reel.py <numero scheda>")
    main(sys.argv[1].zfill(3))
