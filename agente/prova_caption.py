# -*- coding: utf-8 -*-
"""
MEMETECA — quale pezzo della caption fa fallire il Reel.

27 agosto 2026. Stesso video, stesso URL, stesso token, nello stesso quarto
d'ora: con caption "prova" il contenitore REELS arriva a FINISHED (tre volte
su tre), con la caption vera va in ERROR (cinque volte su cinque). Non e' il
file e non e' il momento: e' il testo. Qui si bisezione il testo.

Non pubblica: crea contenitori e basta, scadono da soli in 24 ore.

    python prova_caption.py <url_video>
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import sys
import time

from contenuti import BRAND, MEMI
from instagram import Instagram
from pubblica_reel import caption_reel

ig = Instagram()
URL = sys.argv[1]
m = next(x for x in MEMI if x["num"] == "021")

VARIANTI = [
    ("A · controllo", "prova"),
    ("B · solo gancio", m["hook"]),
    ("C · gancio + menzione", f"{m['hook']}\n\nSegui {BRAND['handle']}"),
    ("D · gancio + hashtag", f"{m['hook']}\n\n{m['hashtags']}"),
    ("E · caption vera", caption_reel(m)),
]

for nome, testo in VARIANTI:
    print(f"══ {nome}  ({len(testo)} caratteri)")
    try:
        cid = ig._post(f"{ig.ig_user_id}/media", media_type="REELS",
                       video_url=URL, caption=testo)["id"]
    except Exception as e:                          # noqa: BLE001
        print(f"   creazione RIFIUTATA: {e}\n")
        continue
    esito = "timeout"
    for _ in range(15):
        time.sleep(6)
        sc = ig._get(cid, fields="status_code")["status_code"]
        if sc in ("FINISHED", "ERROR", "EXPIRED"):
            esito = sc
            break
    print(f"   {cid} → {esito}\n")
