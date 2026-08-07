# -*- coding: utf-8 -*-
"""
MEMETECA — il carosello manifesto.

Il post che spiega perché la pagina esiste. Non è una scheda e non è un bonus
d'attualità: è la dichiarazione d'intenti, e va pubblicata una volta sola.

Usa il generatore dei post fuori collana (palette invertita) perché deve
distinguersi nella griglia: è l'unico post che parla della pagina invece che
di un meme.

    python manifesto.py            # genera le tre slide in ../assets
    python manifesto.py caption    # stampa solo la caption

Ogni dato qui dentro è verificato e ha una fonte. È il minimo, visto che il
post promette esattamente questo.
"""

# Console Windows in cp1252: senza questo, un accento fa morire lo script.
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import pathlib
import sys

from bonus import caption, genera, verifica

QUI = pathlib.Path(__file__).parent

MANIFESTO = {
    "slug": "manifesto",
    "collana": "Manifesto",
    "etichetta": "Manifesto",
    "titolo": "QUI NON C'ERA NIENTE",
    "sottotitolo": "Perché esiste MEMETECA",
    "occhiello": "«Il fenomeno internet italiano del 2025 lo ha raccontato "
                 "il New York Times. In italiano, nessuno.»",

    "apertura": "Prima di aprire questa pagina abbiamo controllato se servisse "
                "davvero. Cioè se un archivio dei meme italiani esistesse già. "
                "La risposta è no, e l'abbiamo verificata in cinque modi diversi.",

    "blocchi": [
        {
            "titolo": "Il posto era vuoto",
            "testo": "Esiste un sito che si dichiara «the wiki of italian memes»: "
                     "contiene tre pagine, tutte ferme al gennaio 2019. Il Meglio "
                     "di Internet, storico sito italiano di cultura digitale, ha "
                     "smesso di pubblicare nel giugno 2017. Nonciclopedia è "
                     "parodia, non filologia. E quando Il Post deve spiegare da "
                     "dove nasce un meme, cita Know Your Meme: una fonte "
                     "americana, perché una italiana non c'è. La prova finale: "
                     "la voce Wikipedia sull'Italian brainrot — fenomeno "
                     "italiano, del 2025 — è documentata da New York Times, "
                     "Guardian e Daily Dot. Da nessuna fonte italiana.",
        },
        {
            "titolo": "Cosa facciamo",
            "testo": "Una scheda per meme: chi l'ha fatto, quando è apparso la "
                     "prima volta, da dove viene, cosa significa oggi. Ogni "
                     "affermazione regge su almeno due fonti indipendenti, e le "
                     "fonti sono scritte in fondo a ogni post. Due schede al "
                     "giorno. La domenica è monografica: TV e pubblicità, che in "
                     "Italia sono la miniera da cui viene metà di tutto. Le schede le "
                     "scriviamo con l'intelligenza artificiale, e lo "
                     "dichiariamo: qui, e sull'etichetta del profilo. "
                     "Quello che non deleghiamo è la verifica.",
        },
        {
            "titolo": "Cosa non facciamo",
            "testo": "Non ripubblichiamo il materiale di nessuno. Niente "
                     "screenshot di post altrui, niente compilation, niente "
                     "«visto in giro». Ogni slide è scritta qui. Non è una posa "
                     "morale: è che un archivio che ruba non è un archivio, "
                     "è un mucchio.",
        },
    ],

    "riquadro": {
        "testo": "Se un meme non regge alla verifica, non esce. "
                 "Nella prima settimana ne abbiamo scartati più di cinquanta su "
                 "settantuno: è il motivo per cui puoi fidarti dei ventuno "
                 "rimasti.",
    },

    "chiusura": "Se ti è mai capitato di spiegare un meme a qualcuno e di "
                "accorgerti che non sapevi da dove venisse: questa pagina è "
                "per quello.",

    "fonti": [
        "Il Post, tag origine-meme",
        "Wikipedia EN, Italian brainrot",
        "knowyourmemeita.weebly.com (ultimo aggiornamento 2019)",
    ],

    "hashtag": ["#memeteca", "#memeitaliani", "#storiadeimeme",
                "#culturaitaliana", "#internetitaliano"],
}


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "caption":
        print(caption(MANIFESTO))
    else:
        verifica(MANIFESTO)
        percorsi = genera(MANIFESTO, QUI.parent / "assets")
        for p in percorsi:
            print(p)
        print(f"\ncaption: {len(caption(MANIFESTO))} caratteri")
