# -*- coding: utf-8 -*-
"""
MEMETECA — la menzione in commento sui post già pubblicati.

Le caption di Instagram NON si modificano via API: una volta uscito, il post
è quello. Ma un commento con la menzione notifica comunque l'account citato,
che è il punto — attribuzione a chi il meme l'ha fatto, e la sola leva di
crescita che non costa niente.

Idempotente: se la menzione c'è già, non fa nulla. Si può rilanciare.

    python menziona.py 023          # menziona il tag della scheda 023
    python menziona.py --tutte      # tutte le schede uscite che hanno un tag
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import datetime as dt
import json
import pathlib
import sys
import time

from contenuti import MEMI
from instagram import Instagram

QUI = pathlib.Path(__file__).parent
STATO = QUI / "stato.json"

# Il testo della menzione. Non è un saluto generico: dice perché l'account
# è citato, così chi lo riceve capisce in due secondi che è attribuzione e
# non spam. Una scheda può sovrascriverlo con il campo "menzione".
def testo(m):
    if m.get("menzione"):
        return m["menzione"]
    return (f"La scheda è su {m['tag']} — chi, quando, perché, "
            f"con le fonti in fondo al post.")


def trova_post(ig, num, cache=None):
    firma = f"Scheda n. {num}"
    post = cache if cache is not None else ig.post_recenti(50)
    return next((p for p in post if firma in (p.get("caption") or "")), None)


def menziona(ig, m, cache=None):
    num = m["num"]
    if not m.get("tag"):
        print(f"  {num}: nessun tag, salto")
        return False

    post = trova_post(ig, num, cache)
    if not post:
        print(f"  {num}: post non trovato tra gli ultimi 50")
        return False

    # Il tag nella caption NON basta: finisce a meta' di un testo lungo, sotto
    # CREATORE, e sul telefono resta dietro il «… altro». Il commento invece
    # si vede in fondo al post senza aprire niente. Quindi la menzione si fa
    # comunque, anche dove la caption ha gia' il tag.

    # L'idempotenza si tiene nello stato, NON interrogando l'API: il 25 agosto
    # /comments non ha restituito un commento che avevamo appena pubblicato, e
    # la 023 si e' presa un doppione. Lo stato e' nostro e non mente.
    s = json.loads(STATO.read_text(encoding="utf-8"))
    gia = {(x["num"], x["tag"]) for x in s.get("menzioni", [])}
    if (num, m["tag"]) in gia:
        print(f"  {num}: {m['tag']} risulta già menzionato")
        return False

    # cintura e bretelle: se per caso il commento si vede, non si ripete
    if any(m["tag"] in c.get("text", "") for c in ig.commenti(post["id"])):
        print(f"  {num}: {m['tag']} già presente in un commento")
        return False

    ig.commenta(post["id"], testo(m))
    s.setdefault("menzioni", []).append(
        {"num": num, "tag": m["tag"],
         "quando": dt.datetime.now(dt.timezone.utc).isoformat()})
    STATO.write_text(json.dumps(s, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8", newline="\n")
    print(f"  {num}: menzionato {m['tag']}")
    return True


def main(argv):
    ig = Instagram()
    if "--tutte" in argv:
        usciti = set(json.loads(STATO.read_text(encoding="utf-8"))["pubblicate"])
        da_fare = [m for m in MEMI if m.get("tag") and m["num"] in usciti]
        cache = ig.post_recenti(50)
        fatti = 0
        for m in da_fare:
            if menziona(ig, m, cache):
                fatti += 1
                time.sleep(20)   # ritmo umano: mai una raffica di commenti
        print(f"menzioni aggiunte: {fatti}")
    else:
        num = argv[1].zfill(3)
        m = next((x for x in MEMI if x["num"] == num), None)
        if not m:
            sys.exit(f"scheda {num} non trovata")
        menziona(ig, m)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: python menziona.py <numero> | --tutte")
    main(sys.argv)
