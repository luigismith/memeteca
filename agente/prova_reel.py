# -*- coding: utf-8 -*-
"""
MEMETECA — sonda dei contenitori video.

Il messaggio che avevamo dai tentativi di agosto era `{'status': 'ERROR'}`:
inutile, perche' era il risultato di UNA sola lettura con due campi. Qui si
chiede tutto quello che l'API accetta di dire, e si prova lo STESSO video
con tre media_type diversi. La differenza fra i tre e' la diagnosi:

  · se REELS fallisce e STORIES passa → il video e l'URL vanno bene, e il
    problema e' specifico dei Reel su questo account;
  · se falliscono tutti e tre → il problema e' il file o il fetch da parte
    di Meta, non il tipo di media.

NON pubblica: crea solo contenitori, che scadono da soli in 24 ore. Il
27 agosto 2026 abbiamo verificato che i tentativi falliti non consumano
quota (content_publishing_limit: 1 su 100), quindi sondare e' gratis.

    python prova_reel.py <url_video>
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import json
import sys
import time

from instagram import Instagram

ig = Instagram()
URL = sys.argv[1] if len(sys.argv) > 1 else None
if not URL:
    sys.exit("uso: python prova_reel.py <url_video>")

print(f"video: {URL}\nhost:  {ig.host}\napi:   {ig.api!r}\n")


def sonda(media_type):
    print(f"══ media_type={media_type}")
    try:
        c = ig._post(f"{ig.ig_user_id}/media", media_type=media_type,
                     video_url=URL, caption="sonda MEMETECA, non pubblicata")
    except Exception as e:                          # noqa: BLE001
        print(f"   creazione RIFIUTATA: {e}\n")
        return
    cid = c["id"]
    print(f"   contenitore {cid} creato")

    for giro in range(20):
        time.sleep(6)
        try:
            d = ig._get(cid, fields="id,status,status_code")
        except Exception as e:                      # noqa: BLE001
            print(f"   lettura fallita: {e}\n")
            return
        sc = d.get("status_code")
        print(f"   [{giro:02d}] {json.dumps(d, ensure_ascii=False)}")
        if sc in ("FINISHED", "ERROR", "EXPIRED"):
            if sc == "ERROR":
                # `status` di solito porta il codice vero (2207xxx). Se la
                # lettura con i campi non lo mostra, si rilegge il nodo nudo:
                # a volte l'API risponde di piu' senza `fields`.
                try:
                    print(f"   nudo: {json.dumps(ig._get(cid), ensure_ascii=False)}")
                except Exception as e:              # noqa: BLE001
                    print(f"   nudo: {e}")
            print()
            return
    print("   timeout: rimasto IN_PROGRESS\n")


for t in ("REELS", "STORIES", "VIDEO"):
    sonda(t)
