# L'agente autonomo

## Chi fa cosa

Il sistema ha due metà, e la divisione non è arbitraria: **il token Instagram vive
nei segreti del repository GitHub**, e non esce da lì. Chi può pubblicare è solo
chi può leggere quel segreto.

```
   GitHub Actions                    Sessioni pianificate
   (ha il token)                     (hanno il web e il giudizio)
   ─────────────                     ────────────────────────────
   12:30  pubblica una scheda        12:30 · 18:30 · 21:00
   18:30  pubblica una scheda        guardano le notizie
                                     scrivono le schede nuove
                                     preparano i post bonus
```

Il post ordinario esce da GitHub, puntuale, anche se nessuno guarda. Il giudizio
— che cosa merita un post fuori collana, quale candidato regge la verifica —
resta alle sessioni, che di token non ne hanno bisogno.

## Il tetto giornaliero non dipende dagli orari

**Due schede al giorno.** La regola sta in `pubblica.py`, non nel cron:

```python
uscite_di_oggi()      # conta le uscite in ora italiana, esclusi i fuori collana
```

Se una scheda è già uscita a mano — com'è successo con la 004 — il cron
successivo se ne accorge e si ferma da solo. È il motivo per cui gli orari si
possono cambiare senza paura di doppioni.

Il terzo post esiste solo come **bonus legato a una notizia**, e ha un budget
suo. Non passa dal cron: lo prepara la sessione e lo pubblica Luigi, dal telefono
o con il mio aiuto dal browser.

## La regola che regge tutto: si prepara poco prima di pubblicare

Ogni sessione **scrive una scheda nuova**: prende il candidato successivo da
`scaletta.py`, lo verifica con almeno due fonti indipendenti, e **lo scarta senza
rimpianti se non regge**. Scartare è la norma: nella prima settimana sono stati
buttati oltre 50 candidati su 71, ed è esattamente il motivo per cui l'archivio è
credibile.

La coda resta corta — **una, due, al massimo tre schede pronte** — e non torna mai
a essere una scorta da venti. Una scorta grande invecchia, si scollega
dall'attualità, e nessuno la rilegge prima che esca.

Ma non va nemmeno a zero: **una o due schede di margine** servono perché una
sessione che fallisce non lasci la pagina muta.

## Il passaggio manuale che resta

Le sessioni scrivono le schede nuove nella cartella di Luigi, non su GitHub: per
spingere servono le sue credenziali git, che io non ho e non voglio. Quindi ogni
tanto, quando la coda si allunga:

```bash
cd D:\IMDB\memeteca && git add -A && git commit -m "schede nuove" && git push
```

Non è urgente: in archivio ci sono già diciassette schede non pubblicate, cioè
più di una settimana di margine. Le sessioni avvisano quando serve davvero.

## Gli orari e l'ora legale

Il cron di GitHub è in **UTC** e non conosce l'ora legale. Adesso è impostato su
`30 10` e `30 16`, cioè 12:30 e 18:30 italiane. **Da fine ottobre**, con l'ora
solare, vanno spostati un'ora avanti — `30 11` e `30 17` — altrimenti i post
escono un'ora prima.

## Se qualcosa va storto

```bash
gh workflow run verifica.yml     # controllo completo, non pubblica niente
gh workflow run pubblica.yml     # pubblica subito la prossima in coda
gh run list -L 5                 # come sono andate le ultime
```

Il controllo gira su GitHub apposta: verifica il token **dove il token vive**,
senza bisogno di averlo sul PC.

Le sessioni delle 18:30 e delle 21:00 controllano da sole che le run del giorno
siano andate a buon fine, e segnalano solo ciò che richiede una decisione.

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
| `agente/verifica.py` | controllo preliminare |
| `agente/stato.json` | che cosa è già uscito — l'unica cosa da conservare |
| `.github/workflows/pubblica.yml` | il cron che pubblica |
| `.github/workflows/verifica.yml` | il controllo, a richiesta |

---

# I Reel via API — la ricetta e il prezzo che l'abbiamo pagata

Scoperto il 24 agosto 2026, in tre ore di tentativi. Sta scritto qui perché
non si ripeta.

## Cosa accetta l'API dei Reel

La validazione di Meta rifiuta con un secco `status: ERROR` e **non dice mai
perché**. Non esiste un messaggio diagnostico: si procede per esclusione.
Questi sono i parametri che passano, verificati sul campo:

- **720x1280** — il nostro contenuto a 1080x1920 per 27 secondi viene
  rifiutato, mentre gli stessi 27 secondi a 720x1280 passano. Su un Reel
  tipografico la differenza non si vede: Instagram ricomprime comunque.
- **H.264 profilo main, `-pix_fmt yuv420p`**, GOP chiuso (`-g 60
  -sc_threshold 0`), **niente B-frame** (`-bf 0`).
- **Niente edit list.** ffmpeg le scrive di default e Meta le rifiuta: serve
  un secondo passaggio di remux con `-use_editlist 0`.
- Audio AAC 44.1 kHz stereo, con `aresample=first_pts=0`.

La ricetta è dentro `agente/reel.py`: i Reel nascono già conformi.

## La musica

`agente/musica.py` sintetizza una traccia originale — nessun campione,
nessun diritto altrui, quindi nessun rights management che possa silenziare
il video. La libreria musicale di Instagram non serve e non è raggiungibile
da API: era il motivo per cui i Reel uscivano muti.

## Il freno di Meta — la regola di ritmo

**Dopo una decina di container video creati in un'ora, Meta frena
l'elaborazione dell'account e rifiuta anche i file che venti minuti prima
passavano.** Il 24 agosto lo stesso identico file (2.599.638 byte) è stato
accettato alle 12:38 e rifiutato alle 12:55: nessuna differenza se non il
numero di tentativi in mezzo. Non è la quota di pubblicazione — quel giorno
ne restavano 91 su 100.

Quindi: **un tentativo per volta, mai più di un Reel all'ora.** Se fallisce,
ci si ferma e si riprova al ciclo successivo. Insistere allunga il freno.

Per validare senza pubblicare:
`gh workflow run reel.yml -f num=<numero> -f prova=true`

## La cache degli URL

Meta ricorda i percorsi già tentati **ignorando la query string**: un
`?v=123` non serve a niente. Se si rigenera un video già tentato bisogna
cambiare il percorso del file, alzando `SUFFISSO_FILE` in
`agente/pubblica_reel.py` (oggi `_v2`).
