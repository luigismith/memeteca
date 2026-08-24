# -*- coding: utf-8 -*-
"""
MEMETECA — ripara il commento con le fonti di una scheda già pubblicata.

Il 7 agosto la 005 è uscita ma il commento «Fonti verificate» è saltato
(il token di allora non aveva il permesso sui commenti). Questo script trova
il post dal numero di scheda e aggiunge il commento SOLO se manca: si può
rilanciare quante volte si vuole senza produrre doppioni.

    python commento_fonti.py 005
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import sys

from contenuti import MEMI
from instagram import Instagram


def ripara(num):
    m = next((x for x in MEMI if x["num"] == num), None)
    if not m:
        sys.exit(f"scheda {num} non trovata in contenuti.py")

    ig = Instagram()
    firma = f"Scheda n. {num}"
    post = next((p for p in ig.post_recenti(50)
                 if firma in (p.get("caption") or "")), None)
    if not post:
        sys.exit(f"nessun post con «{firma}» tra gli ultimi 50")

    if any(c.get("text", "").startswith("Fonti verificate")
           for c in ig.commenti(post["id"])):
        print(f"il post della {num} ha già il commento con le fonti")
        return

    ig.commenta(post["id"], "Fonti verificate: " + " · ".join(m["fonti"]))
    print(f"commento con le fonti aggiunto alla {num} ({post['permalink']})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: python commento_fonti.py <numero scheda>")
    ripara(sys.argv[1].zfill(3))
