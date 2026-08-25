# -*- coding: utf-8 -*-
"""
MEMETECA — cosa vede l'API.

Serve quando il profilo e lo stato non concordano: elenca i media che
Instagram dichiara nostri, con id, data e la riga di firma della caption.

    python diagnosi.py
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import json
import pathlib
import re

from contenuti import MEMI
from instagram import Instagram

QUI = pathlib.Path(__file__).parent

ig = Instagram()
media = ig.post_recenti(60)
print(f"media secondo l'API: {len(media)}\n")

visti = set()
for p in media:
    cap = p.get("caption") or ""
    firma = re.search(r"Scheda n\. (\S+)", cap)
    num = firma.group(1) if firma else "—"
    visti.add(num)
    titolo = cap.split(" — ")[0][:34] if cap else "(senza caption)"
    print(f"  {p.get('timestamp','')[:16]}  {num:>6}  {titolo}")

stato = json.loads((QUI / "stato.json").read_text(encoding="utf-8"))
mancanti = [n for n in stato["pubblicate"] if n not in visti]
print(f"\nschede date per pubblicate ma NON viste dall'API: "
      f"{', '.join(mancanti) if mancanti else 'nessuna'}")
