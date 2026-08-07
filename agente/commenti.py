# -*- coding: utf-8 -*-
"""
MEMETECA — i commenti sui nostri post.

    python commenti.py                      # elenca i commenti senza risposta
    python commenti.py rispondi ID "testo"  # risponde a un commento

Cosa si può fare e cosa no, senza giri di parole:

  SÌ  leggere i commenti sui nostri post, rispondere, nascondere gli insulti
  NO  seguire account — l'API di Instagram non espone nessun endpoint per farlo
  NO  commentare sotto i post altrui — stessa cosa: non esiste

Non è una limitazione del codice, è una scelta di Meta: l'automazione di follow
e commenti verso terzi è il vettore principale dello spam, e infatti è anche il
comportamento che fa scattare i blocchi. Quella parte resta a mano.

Perché rispondere conta: dal gennaio 2025 Instagram dichiara che il segnale più
forte per la distribuzione sono le condivisioni in DM, e la conversazione sotto
il post è ciò che le innesca. Una risposta che aggiunge una fonte o una data vale
più di dieci commenti generici altrove.
"""

# Console Windows in cp1252: senza questo, un accento fa morire lo script.
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")
import sys

from instagram import Instagram


def elenca():
    ig = Instagram()
    aperti = ig.da_rispondere()
    if not aperti:
        print("Nessun commento in attesa di risposta.")
        return
    print(f"\n{len(aperti)} commenti senza risposta\n" + "─" * 62)
    for c in aperti:
        print(f"\n@{c['chi']} — {c['quando']}\n  {c['testo']}")
        print(f"  post: {c['media']}")
        print(f"  rispondi con:  python commenti.py rispondi {c['id']} \"...\"")
    print()


def rispondi(comment_id, testo):
    if len(testo) > 300:
        sys.exit("Risposta troppo lunga: tienila sotto i 300 caratteri.")
    print("Risposta inviata:", Instagram().rispondi(comment_id, testo))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        elenca()
    elif sys.argv[1] == "rispondi" and len(sys.argv) == 4:
        rispondi(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
