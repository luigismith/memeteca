# Seguire e commentare — cosa posso fare io e cosa no

Risposta secca prima di tutto, perché cambia il piano: **seguire account e
commentare sotto i post altrui non si può automatizzare.** Non è una limitazione
del nostro codice.

| | Via API | Via browser |
|---|---|---|
| Seguire un account | **impossibile** — l'endpoint non esiste | possibile, ma è il comportamento che oggi ci ha fatto bloccare |
| Commentare post altrui | **impossibile** — l'API copre solo i nostri post | idem |
| Rispondere ai commenti sui nostri post | **sì** | sì |
| Nascondere insulti | **sì** | sì |

Meta non espone follow e commenti verso terzi **di proposito**: è il vettore
principale dello spam. E la conferma pratica ce l'abbiamo già — il soft-block di
oggi è arrivato dopo quattro pubblicazioni ravvicinate da browser automatizzato.
Aggiungerci follow e commenti automatici, su un account nato stamattina e già
sotto restrizione pubblicitaria, sarebbe il modo più rapido per farlo sospendere.

Quindi: **la parte di relazione resta a mano.** Dieci minuti al giorno dal
telefono, su una lista breve. Qui sotto c'è la lista, e ho fatto la ricerca perché
fosse una lista vera.

---

## Quello che invece ho automatizzato: i commenti sui nostri post

```bash
python agente/commenti.py                      # i commenti senza risposta
python agente/commenti.py rispondi ID "testo"  # risponde
```

Conta più di quanto sembri. Dal gennaio 2025 Instagram dichiara che il segnale
più forte per la distribuzione sono le **condivisioni in DM**, e la conversazione
sotto il post è ciò che le innesca. Una risposta che aggiunge una data o una fonte
vale più di dieci commenti generici lasciati altrove.

Il codice sa anche **nascondere** i commenti offensivi invece di cancellarli: chi
l'ha scritto continua a vederlo, non si accorge di niente e non riprova.

---

## La scoperta che vale più della lista

Ho cercato se in Italia esista già un Know Your Meme. **Non esiste, e l'ho
verificato in cinque modi diversi:**

- `knowyourmemeita.weebly.com` si dichiara «the wiki of italian memes»: contiene
  **tre pagine**, tutte ferme al **22 gennaio 2019**
- *Il Meglio di Internet*, storico sito italiano di internet culture: **ultimo
  articolo, giugno 2017**
- Nonciclopedia è parodia, non filologia, e ha **53 utenti attivi al mese**
- **Il Post**, quando deve spiegare da dove nasce un meme, cita **Know Your Meme**:
  cioè una fonte americana, perché una italiana non c'è
- perfino la voce Wikipedia sull'*Italian brainrot* — fenomeno **italiano** del
  2025 — è documentata da NYT, Guardian e Daily Dot, **da nessuna fonte italiana**

Il posto è vuoto. Va detto in bio e nel primo carosello di presentazione, perché è
la ragione per cui la pagina dovrebbe esistere.

---

## Chi seguire, e come

### Presidio quotidiano — sei account, dieci minuti

Qui si commenta **aggiungendo qualcosa**: la data esatta, il nome del creatore, la
fonte. Mai «bel post». Il commento deve essere il servizio che la pagina vende.

| Account | Follower | Perché proprio lì |
|---|---|---|
| **@clipitaliane** | 95.8K | Archivia clip italiane diventate meme ma **non data e non attribuisce**. È esattamente il buco che riempiamo: commentare lì con l'anno e la fonte è metterci in vetrina |
| **@rmemesita** | 35.1K | **Engagement 18%**, il pubblico più caldo della lista, e viene da Reddit: già abituato a chiedere la fonte |
| **@raiteche** | 360.2K | L'archivio Rai. Metà dei meme italiani nasce da una clip loro: siamo il commento naturale |
| **@vivaglianni90official** | 812.3K | Il più grande bacino di nostalgia italiana |
| **@sapore.di.male** | 862.6K | Fa già meta-commento sui meme, «dentro questo meme ci sono due layer»: tono compatibile |
| **@vaberagaa** | 146K | Engagement 9.17%, pubblico che commenta davvero |

### Da evitare, e non è snobismo

**@welcometofavelas** (1,1M) e la rete **Pastorizia Never Dies** (7M dichiarati)
sono aggregatori puri: ripubblicano materiale altrui. Commentare lì associa
MEMETECA all'esatto contrario della sua premessa — e sono anche le pagine che la
stretta del 30 aprile sta penalizzando.

### Le cinque collaborazioni da tentare

Non oggi: quando ci sono trenta schede pubblicate e la pagina si presenta da sola.

**Memissima Festival** (@memissimafestival, 10.5K) — il festival della cultura
memetica di Torino, quinta edizione a gennaio 2026, con Fondazione CRT, Camera di
Commercio e il Dipartimento di Filosofia dell'Università di Torino. Assegna i Meme
Award. Il dato che conta: **oltre 300 pagine italiane hanno candidato materiale via
DM**, e parte del voto passa dal loro Instagram. Un archivio con fonti verificate
ha un ruolo ovvio lì — **partner documentale del premio**, non concorrente. È il
contatto numero uno.

**Alessandro Lolli** — autore di *La guerra dei meme* (effequ), firma del
Tascabile. Scrive esplicitamente di «filologia memetica». MEMETECA è la sua tesi
messa in pratica.

**Daniele Zinni** (@inchiestagram, 12.3K) — *Meme del sottosuolo*, Einaudi. Autore
di peso con un account piccolo: **il miglior rapporto autorevolezza/raggiungibilità
della lista**.

**Iconografie** (@iconografiexxi, 82.9K) — rivista monografica sull'iconografia del
presente, diretta da Mattia Salvia. Il progetto editoriale italiano più affine:
complementare, non concorrente.

**Giulio Armeni / @filosofia_coatta** (209.8K) — fa tour teatrali di meme. Tratta
il meme come materiale d'autore, che è la nostra stessa premessa.

### Tre segnalazioni una tantum, quando c'è la scheda giusta

Non un DM promozionale: **una scheda specifica** che gli serve davvero.

- **Pietro Minto**, *Link Molto Belli* (20.000+ iscritti, dal 2014) — il formato
  «link bello» è fatto apposta
- **Andrea Girolami**, *Scrolling Infinito* (25.000+ iscritti) — la sua newsletter
  parla di come si cresce su Instagram: un archivio ben fatto è materiale da case
  study
- **Il Post** — ha un beat stabile sull'origine dei meme (i tag *origine-meme* e
  *storia-meme*) e per farlo cita Know Your Meme. Il giorno in cui possono citare
  noi, è una notizia

### Da studiare, non da inseguire

**@archeoplastica** (464.1K) è MEMETECA applicata alla plastica: oggetti ritrovati,
ognuno datato e documentato. Stessa promessa di metodo, stesso formato d'archivio,
mezzo milione di follower. **È la dimostrazione che il format funziona in Italia.**

**@depthsofwikipedia** (1.66M) è la stessa prova su scala internazionale: archivio,
tono ironico, zero contenuto rubato.

---

## Come si commenta, in pratica

Tre regole, e sono poche perché contano tutte.

1. **Aggiungi un fatto.** «Questa è del 4 ottobre 2011, il giorno in cui Vasco
   ritirò la querela.» Non «bellissimo».
2. **Mai linkare la pagina.** Il profilo è già cliccabile dal nome. Un link nel
   commento è pubblicità; un fatto è competenza — e la competenza porta al profilo
   da sola.
3. **Se non hai niente da aggiungere, non commentare.** Vale la stessa regola del
   post bonus: nel dubbio si desiste.

Cinque commenti buoni al giorno valgono più di cinquanta generici, e non fanno
scattare nessun blocco.

---

## Le due cose da verificare tu, cinque minuti

Reddit è irraggiungibile dal mio ambiente, quindi due dati mancano e servono prima
di usare quel canale:

- **i regolamenti sull'autopromozione** dei subreddit italiani — r/memesITA
  (498k), r/Lostmediaitalia (8,8k), r/BancaDelMeme (71k). Lì le regole sono
  applicate sul serio, e cambiano tutto
- **se r/ITAGLIA esiste ancora**: non compare in un censimento di 258 subreddit
  italiani

---

**Fonti:** [Il Tascabile, «I meme sono morti?» di Alessandro Lolli](https://www.iltascabile.com/linguaggi/meme-morti/) · [Memissima Festival](https://www.memissimafestival.it/) · [ANSA, Memissima 2026](https://www.ansa.it/piemonte/notizie/2026/01/13/torna-memissima-il-festival-della-cultura-memetica_4e3b83c8-57f0-4b1c-8d26-867e8f12ec1b.html) · [Il Post, tag origine-meme](https://www.ilpost.it/tag/origine-meme/) · [Iconografie](https://www.iconografie.it/) · [Meme del sottosuolo, Einaudi](https://www.einaudi.it/catalogo-libri/problemi-contemporanei/meme-del-sottosuolo-daniele-zinni-9788858443668/) · [awesome-italian-reddit](https://github.com/danieleongari/awesome-italian-reddit) · follower verificati su HypeAuditor, agosto 2026
