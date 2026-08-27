# -*- coding: utf-8 -*-
"""
MEMETECA — perche' i Reel non passano.

Quattro giorni di tentativi (24-26 agosto 2026), una ventina di container,
sempre lo stesso `{'status': 'ERROR'}` secco e senza spiegazione. Il 26 il
primo e unico tentativo della giornata, a freddo dopo 18 ore di pausa, e'
fallito lo stesso: e da li' la teoria del «budget video esaurito» non regge
piu' da sola.

Questo script NON crea container e NON pubblica niente: e' sola lettura, non
consuma budget. Interroga l'API per rispondere a tre domande:

  1. quanto budget di pubblicazione risulta consumato davvero
     (`content_publishing_limit`: se dice 0/50, la teoria del budget muore);
  2. che tipo di account siamo e che cosa l'API dichiara di supportare;
  3. che `media_product_type` hanno i media che l'account possiede
     (se non compare mai REELS, quella strada non e' mai stata aperta).

    python diagnosi_reel.py
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

from collections import Counter

from instagram import Instagram

ig = Instagram()


def prova(titolo, fn):
    """Ogni sonda e' isolata: se una fallisce, l'errore e' il dato."""
    print(f"\n── {titolo}")
    try:
        print("   ", fn())
    except Exception as e:                      # noqa: BLE001 — l'errore serve
        print("    ERRORE:", e)


prova("profilo",
      lambda: ig._get(ig.ig_user_id,
                      fields="id,username,account_type,media_count"))

# Il numero che smonta o conferma la teoria del budget. Se quota_usage e' 0
# mentre i reel falliscono, il problema non e' il consumo: e' strutturale.
prova("budget di pubblicazione (content_publishing_limit)",
      lambda: ig._get(f"{ig.ig_user_id}/content_publishing_limit",
                      fields="config,quota_usage"))

prova("permessi del token",
      lambda: ig._get(f"{ig.ig_user_id}/permissions"))


def tipi_media():
    r = ig._get(f"{ig.ig_user_id}/media",
                fields="id,media_type,media_product_type,timestamp", limit=50)
    dati = r.get("data", [])
    tipi = Counter((m.get("media_type"), m.get("media_product_type"))
                   for m in dati)
    righe = [f"{n} × media_type={t or '—'} product_type={p or '—'}"
             for (t, p), n in tipi.most_common()]
    return f"{len(dati)} media letti · " + " · ".join(righe)


prova("tipi di media posseduti dall'account", tipi_media)

print("\nCome si legge:")
print("  · quota_usage vicino a 0 e reel comunque in ERROR → non e' il budget.")
print("  · nessun product_type REELS fra i media → l'account non ha mai")
print("    pubblicato un reel via API, e probabilmente non e' abilitato.")
print("  · errore 190 in una qualsiasi delle sonde → il token e' invalidato,")
print("    e serve una nuova autorizzazione OAuth: non lo risolve nessuna")
print("    automazione.")
