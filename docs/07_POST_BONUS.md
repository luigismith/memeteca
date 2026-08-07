# Il post bonus — quando la giornata lo merita

Due post al giorno sono il calendario. Il bonus è la terza uscita, e non è
programmata: nasce solo se succede qualcosa a cui l'archivio può rispondere con
qualcosa di vero.

Il modello è il fuori collana su Guccini del 6 agosto 2026. Funzionava per un
motivo preciso: **non ho inventato un meme che non c'era**. Ho scritto in apertura
di caption che un meme su Guccini non esiste, e ho raccontato le due cose
documentate che collegavano davvero la sua morte alla storia di internet italiano.

Questo documento serve a rendere quella logica ripetibile senza che degeneri.

---

## Come funziona

Un'ora prima di ogni orario di pubblicazione — **11:30 e 18:00** — parte una
sessione che cerca le notizie italiane del giorno e decide. Nella stragrande
maggioranza dei casi la decisione giusta è **non pubblicare**, e la sessione si
chiude senza fare niente.

L'ordine delle operazioni non è negoziabile:

1. **Cerca** le notizie italiane rilevanti delle ultime ore
2. **Verifica** con almeno due fonti indipendenti e attendibili
3. **Cerca il collegamento con l'archivio** — e il collegamento deve esistere già,
   non lo si costruisce
4. Se il collegamento non c'è, **si ferma**
5. Se c'è, produce le tre slide e la caption e pubblica

Un solo bonus al giorno. Se è uscito a mezzogiorno, la sessione delle 18:00 si
limita a verificarlo e chiude.

---

## Quando si pubblica

Sono pochi casi, e sono tutti riconoscibili.

**Il protagonista di un meme documentato esce di scena.** Muore, si ritira,
smette. Vale se la persona è già nell'archivio o meriterebbe di esserci: il
creatore di un format, il volto involontario di un tormentone, l'autore di una
battuta entrata nella lingua.

**Un meme dell'archivio torna nella cronaca.** Una sentenza, un anniversario, una
citazione in Parlamento, un revival. È il caso più pulito: c'è già tutto, basta
raccontarlo.

**Un evento nazionale che una scheda specifica illumina.** Sanremo, elezioni, una
qualificazione ai Mondiali. Ma solo se il collegamento è **documentato e
puntuale**. «Elezioni → io sono Giorgia» va bene se c'è un fatto nuovo, non se
serve solo a cavalcare l'hashtag.

---

## Quando si desiste, sempre

Queste non ammettono eccezioni, nemmeno se il collegamento sembra brillante.

- **Morti che non c'entrano con l'archivio.** Una tragedia non è un'occasione
  editoriale.
- **Disastri, incidenti, cronaca nera, guerra, terrorismo.** Mai. Nessuna
  angolazione, nessun tono, nessun pretesto.
- **Qualunque cosa che coinvolga minori.**
- **Salute e malattia di persone vive.**
- **Polemiche politiche in corso** dove la pagina finirebbe per prendere una
  parte. MEMETECA racconta come nasce un meme politico, non chi ha ragione.
- **Collegamenti forzati.** Se per arrivare al meme servono due passaggi logici,
  il collegamento non esiste: lo stai costruendo tu.
- **Meme che andrebbero inventati.** La regola Guccini: se il meme non esiste, o
  lo si scrive («un meme su X non esiste, e infatti...»), o non si pubblica.
- **Notizie con una sola fonte**, o solo su siti di gossip e aggregatori.
- **Il dubbio.** Nel dubbio non si pubblica. Un bonus mancato non costa niente,
  un bonus sbagliato costa la credibilità dell'archivio.

---

## Frequenza attesa

**Uno o due al mese, non uno al giorno.** Se ne escono tre in una settimana, la
soglia si è abbassata da sola e va rialzata.

Il valore del bonus sta nella sua rarità: è il segnale che la pagina è viva e
guarda il mondo. Se diventa quotidiano è solo rumore, e per giunta porta la
frequenza settimanale fuori dalla banda ottimale — che è esattamente il problema
che abbiamo evitato passando a due post al giorno.

---

## La forma

Palette invertita: carta scura, inchiostro chiaro. Nella griglia il bonus si
distingue a colpo d'occhio dalle schede ordinarie, e deve restare così.

Il codice è in `agente/bonus.py`:

```python
from bonus import genera, caption, verifica

verifica(dati)                 # solleva se qualcosa non va
genera(dati, "../assets")      # tre slide 1080x1350
caption(dati)                  # caption pronta
```

`verifica()` blocca la pubblicazione se mancano due fonti, se gli hashtag sono più
di cinque, se i blocchi non sono fra due e quattro o se la caption sfora. È un
guardrail meccanico, non un consiglio.

Campi del dizionario: `slug`, `titolo`, `sottotitolo`, `etichetta` (il chip rosso:
*In memoria*, *L'attualità*, *Anniversario*), `occhiello`, `apertura`, `blocchi`
(2-4 dict con `titolo` e `testo`), `riquadro` facoltativo su fondo pieno,
`chiusura`, `fonti`, `hashtag`. `bonus.DATI_ESEMPIO` contiene il post su Guccini
come modello di riferimento.

---

## Il tono

MEMETECA non commenta l'attualità: la guarda dalla sua feritoia, che è l'archivio.

La differenza è tutta qui. Un post che dice «che tristezza» è una pagina qualunque.
Un post che dice «nel 2014 internet lo diede per morto con un tweet falso, ed è
successo questo» è un archivio che fa il suo mestiere in un giorno in cui serve.

Nessun tono luttuoso di maniera, nessuna presa di posizione, nessuna morale.
Fatti verificati, messi in fila, e una frase finale che resta.
