# Il reperto in copertina

Hai chiesto di mettere in prima slide un accenno dell'originale — uno screenshot,
un frammento — dove esiste e dove ha senso. L'ho fatto, con una scelta di campo
che vale la pena spiegare, perché tocca l'unica cosa che tiene in piedi il
progetto.

Nella copertina c'era un vuoto, sopra il titolo. Adesso lì c'è il **reperto**: un
riquadro bordato, con il bollo rosso, il frammento e sotto la fonte. Esiste in tre
forme.

---

## 1 · Il lemma — dove il meme è finito sul dizionario

Tre schede dell'archivio non sono battute: sono **voci di vocabolario**.

- **supercazzòla** — Zingarelli, edizione 2016
- **bimbominkia** — Treccani, Neologismi
- **ciaóne** — Treccani, Neologismi 2016

Per queste il reperto è la voce di dizionario, composta come una voce di
dizionario: lemma in nero, qualifica grammaticale in corsivo, definizione. È
ricostruzione tipografica, non riproduzione: le definizioni sono riscritte, non
copiate.

È la forma che preferisco, e non solo per prudenza. Una pagina che ti mostra
*«supercazzòla, s. f.: discorso senza senso fatto per confondere l'interlocutore»*
sta dicendo in tre righe tutto quello che la scheda argomenta in tre slide.

## 2 · La citazione — dove il meme è una frase

Quattro schede hanno il reperto testuale, e ogni volta è **qualcosa che l'occhiello
non dice già**:

| Scheda | Reperto | Perché |
|---|---|---|
| Io so' io | il sonetto di Belli, 1831 | l'originale in romanesco ottocentesco, 150 anni prima del film |
| Io sono Giorgia | le nove parole del comizio | il campione esatto, quello che mem&j hanno tagliato |
| L'asteroide del Buondì | la battuta completa della madre | l'occhiello ne porta solo la seconda metà |
| L'uomo del Monte | *«The man from Del Monte, he say yes!»* | lo slogan inglese originale, prima della traduzione |

Il testo di Belli è di pubblico dominio. Gli altri tre sono citazioni brevi con
fonte, autore e anno: rientrano nella **citazione a fini di critica e discussione**
(art. 70 L. 633/1941), che è precisamente il caso d'uso di questa pagina.

## 3 · L'immagine — lo slot c'è, il materiale lo metti tu

Il codice accetta anche un fotogramma o uno screenshot vero:

```python
"reperto": {
  "tipo": "immagine",
  "bollo": "Il fotogramma",
  "file": "003_amici_miei.jpg",          # va in reperti/
  "fonte": "Fotogramma da «Amici miei» (1975), regia di Mario Monicelli. "
           "Citazione a fini di critica e discussione (art. 70 L. 633/1941).",
}
```

Metti il file in `reperti/` e la copertina lo incornicia da sola, con bordo,
bollo e attribuzione. Se il file non c'è, il reperto viene semplicemente omesso e
la slide torna come prima: nessun errore, nessun buco.

**Perché il materiale non lo prendo io.** Non scarico immagini protette da
copyright: è un limite che rispetto sempre, e in questo caso è anche la scelta
giusta nel merito. Tu invece puoi: fai lo screenshot, lo metti nella cartella, e
la grafica fa il resto.

---

## Le due cose da sapere prima di usarlo

### Il diritto

L'art. 70 della legge sul diritto d'autore consente la citazione di brani per
**critica, discussione e insegnamento**, a tre condizioni: che sia **breve**, che
**non faccia concorrenza** all'opera, e che siano **indicati autore e fonte**.

Una pagina che spiega da dove viene un meme è il caso di scuola. Ma vale finché il
frammento resta un frammento: un fotogramma dentro una scheda che lo commenta è
citazione, una gallery di fotogrammi è ricarica.

### L'algoritmo — questa conta di più

Dal **30 aprile 2026** Instagram toglie dalle raccomandazioni gli account che
pubblicano prevalentemente contenuti non propri, e nella lista di ciò che **non**
conta come originale ci sono esplicitamente **gli screenshot di post altrui**.

Restano originali i contenuti «alterati in modo sostanziale con testo, contesto e
prospettiva propri». È esattamente la nostra situazione: un riquadro citato dentro
una slide fatta al 95% di tipografia e testo redazionale nostro.

Ma il margine si consuma in fretta. Tre regole che terrei ferme:

1. **Il reperto resta minoranza.** Un riquadro nella parte alta, non l'immagine di
   fondo, non la slide intera.
2. **Solo in copertina.** Le slide 2 e 3 restano completamente tipografiche.
3. **Sempre con la fonte visibile.** Non è solo correttezza: è la prova che il
   contesto è nostro.

Ho tenuto i reperti su 7 schede su 21 — un terzo. È una proporzione che mantiene
il vantaggio competitivo di cui parla `06_STRATEGIA.md`, invece di buttarlo via
per un fotogramma.

---

## Sull'audio

Qui la risposta è no, e per un motivo tecnico prima che editoriale.

**I caroselli non hanno audio.** È un formato di immagini: l'audio esiste solo sui
Reel. Per mettere un sottofondo bisognerebbe convertire tutto in video — un altro
formato, un'altra grammatica, e per la nostra fascia di follower i dati dicono che
il carosello rende quasi il doppio del Reel (993 views contro 580).

E se anche lo facessimo: l'audio di uno spot o di un film è coperto dal sistema di
rights management di Meta, che lo riconosce e silenzia il video. Non è una zona
grigia, è un blocco automatico.

Se un giorno vorrai i Reel, la strada praticabile è un'altra: audio originale — la
frase letta, o una traccia libera — con le slide animate. Ma è un progetto a sé,
non una spunta da aggiungere stasera.

---

## Come aggiungerne altri

In `agente/contenuti.py`, dentro la scheda, prima di `"confidenza"`:

```python
"reperto": {"tipo": "citazione", "bollo": "La battuta",
  "testo": "«…»",
  "fonte": "Opera, anno, autore. Citazione a fini di critica (art. 70 L. 633/1941)."},
```

Poi `python pubblica.py genera` e le slide si rifanno. I tipi disponibili sono
`lemma`, `citazione` e `immagine`; il campo `bollo` è l'etichetta rossa in alto a
sinistra (*Il lemma*, *L'originale*, *Il campione*, *La battuta*, *Lo slogan*, *Il
fotogramma*).

Non metterlo su tutte. Il reperto funziona perché è un'eccezione: quando c'è,
significa che quella scheda ha qualcosa di più da mostrare.
