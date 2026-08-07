# L'agente autonomo

## Come funziona adesso

Tre sessioni al giorno, agli orari di pubblicazione: **12:30, 18:30, 21:00**.
Ognuna fa la stessa cosa, in questo ordine.

```
        ┌─ guarda le notizie
        │
        ├─ c'è un evento che l'archivio può illuminare?
        │     sì  → prepara il post bonus e pubblica
        │     no  ↓
        │
        ├─ oggi sono uscite meno di 2 schede?
        │     sì  → pubblica la prossima in coda
        │     no  → non esce niente, e va bene così
        │
        └─ prima di chiudere: prepara la scheda successiva
```

**Due post al giorno, tre se succede qualcosa.** Lo slot delle 21:00 è riservato
all'attualità: se non c'è notizia e la giornata è già completa, resta vuoto. Un
terzo post senza una ragione è rumore.

## La regola che regge tutto: si prepara poco prima di pubblicare

Niente più produzione a blocchi. Ogni sessione pubblica un post e **ne prepara
uno**: ricerca il candidato successivo, lo verifica, scrive la scheda, genera le
slide. La coda resta corta — **una, due, al massimo tre schede pronte** — e non
torna mai a essere una scorta da venti.

È il motivo per cui il sistema regge: una scorta grande invecchia, si scollega
dall'attualità e nessuno la rilegge prima che esca. Una coda corta obbliga a
guardare ogni scheda poco prima che venga vista da qualcun altro.

La coda non va però a zero: **una o due schede di margine** servono perché una
sessione che fallisce (rete giù, fonti irraggiungibili, candidato da scartare)
non lasci la pagina muta.

## La scaletta

`agente/scaletta.py` contiene **59 candidati**: nomi con una riga di appunto, non
schede. Sono ipotesi da verificare, non fatti.

```bash
python agente/scaletta.py     # il prossimo da lavorare
```

Ogni sessione ne prende uno, lo verifica con almeno due fonti indipendenti e
**lo scarta senza rimpianti se non regge**. Scartare è la norma: nella prima
settimana sono stati buttati oltre 50 candidati su 71. È esattamente il motivo per
cui l'archivio è credibile, e la scaletta è scritta apposta con voci del tipo
*«da verificare se esiste davvero»*.

Quando i candidati finiscono, la sessione ne cerca di nuovi.

## Perché non GitHub Actions

Il workflow c'è ancora, ma **il cron è spento**. Un'azione GitHub sa eseguire
codice, non sa leggere le notizie, valutare se una notizia merita un post o
verificare che un meme esista. Serviva quando le schede erano già scritte e
bastava pubblicarle in ordine.

Resta come **rete di sicurezza da lanciare a mano**: se i task pianificati sono
fermi, pubblica la prossima scheda già pronta in coda.

```bash
gh workflow run pubblica.yml --repo TUONOME/memeteca
```

## Che cosa serve perché pubblichi da sola

Il token Instagram (`docs/05_COSA_DEVI_FARE_TU.md`). Senza, le sessioni fanno
tutto lo stesso — notizie, ricerca, scrittura, slide — e alla fine ti consegnano
immagini e caption da pubblicare a mano, dicendotelo.

Le tre sessioni provano a prendere il progetto in quest'ordine: repository GitHub,
poi la cartella `D:\IMDB\memeteca` dal tuo computer, poi si fermano. Una volta
fatto il setup, il repository è la strada buona: non dipende dal PC acceso.

## I file

| File | Cosa fa |
|---|---|
| `agente/scaletta.py` | i candidati da lavorare, e il prossimo numero libero |
| `agente/contenuti.py` | le schede scritte, la coda, il calendario |
| `agente/grafica.py` | le tre slide di una scheda |
| `agente/bonus.py` | le tre slide di un post bonus, palette invertita |
| `agente/instagram.py` | client API: pubblica, commenta, rinnova il token |
| `agente/commenti.py` | i commenti sui nostri post |
| `agente/pubblica.py` | `genera` · `esporta` · `prossimo` · `pubblica` |
| `agente/verifica.py` | controllo preliminare prima del primo post |
| `agente/stato.json` | che cosa è già uscito — l'unica cosa da conservare |

## Se qualcosa va storto

Ogni sessione ti manda una notifica con l'esito. Le sere in cui non esce niente
sono normali e te lo dice in una riga.

Se una sessione fallisce, la successiva riprende da dove si era fermata: lo stato
sta in `stato.json` e la coda in `contenuti.py`, entrambi nel repository. Non c'è
niente di volatile.
