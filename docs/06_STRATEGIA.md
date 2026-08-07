# MEMETECA — crescita e monetizzazione

Ricerca fatta la sera del 6 agosto 2026 su fonti primarie Meta, studi con campione
dichiarato (Metricool 24,3 milioni di post; Socialinsider 35 milioni; Buffer 45
milioni) e dati di mercato italiani (DeRev, 5.000 creator e 865.000 post).

Dove un numero non esiste lo dico. È la parte più importante di questo documento:
quasi tutto ciò che circola su «quanto guadagna una pagina Instagram» è lo stesso
listino riciclato da dieci testate diverse.

---

## 1. La cosa che cambia tutto, e gioca a nostro favore

Il **30 aprile 2026** Instagram ha esteso a **foto e caroselli** una regola che
prima valeva solo per i Reel: gli account che pubblicano prevalentemente contenuti
non propri **escono dalle raccomandazioni**. Non vengono bannati, non perdono
follower: semplicemente spariscono da Esplora, dai feed suggeriti, dai reel
consigliati. Cioè dall'unico canale che fa crescere una pagina da zero.

Mosseri, citato da PetaPixel: *«If most of what you post to Instagram is someone
else's content, your account is no longer going to be recommendable.»*

**Non contano come originali:** repost, watermark aggiunti, cambi di velocità,
screenshot di post altrui anche con il credit.
**Contano come originali:** contenuti creati ex novo, o materiale di terzi
alterato in modo sostanziale con testo, contesto e prospettiva propri.

Adesso guarda cosa abbiamo fatto stamattina, senza saperlo.

MEMETECA **non ricarica nulla**. Non un fotogramma, non uno screenshot, non un
meme. Le 63 slide sono tipografia e testo redazionale originale al 100%. La
scelta era nata per evitare i takedown per copyright: si è rivelata anche
l'assicurazione contro la penalizzazione più pesante introdotta da Instagram in
due anni.

**Questo è il vantaggio competitivo del progetto, ed è enorme.** Le pagine di meme
italiane sono centinaia e vivono tutte di ricarica: dal 30 aprile stanno uscendo
dalle raccomandazioni una dopo l'altra, che se ne accorgano o no. Noi entriamo in
un mercato in cui il concorrente medio è appena stato zavorrato.

**Da fare ogni settimana:** Impostazioni → Account → **Stato dell'account**.
Dice se sei idoneo alle raccomandazioni. È il primo indicatore da guardare, prima
dei follower.

---

## 2. Le tre correzioni che ho già applicato stasera

La ricerca ha trovato tre errori nel setup di stamattina. Sono corretti nel
codice, le slide e le caption sono già rigenerate.

### a) Gli hashtag erano dodici. Il massimo è cinque.

Da **dicembre 2025** Instagram impone un tetto di **5 hashtag per post**. Le
nostre caption ne avevano dodici: sopra il limite, e per giunta inutili — Mosseri,
luglio 2026: *«Hashtags work, but they've never been a good way to actually
increase your reach.»* I dati Metricool sono anche peggio della posizione
ufficiale: i post con hashtag ottengono **31,7% di views in meno** della media.

Ora sono 5 per scheda, tutti specifici. Niente più `#culturapop`.

### b) Il nome del meme non era nella prima riga

La ricerca interna di Instagram ha sostituito gli hashtag come meccanismo di
scoperta per i contenuti testuali. Ogni nostra scheda contiene naturalmente le
query che le persone digitano: *supercazzola*, *er faina*, *non ce n'è coviddi*.
Sprecarle dentro la grafica, dove l'OCR le legge male, era un autogol.

Ogni caption ora comincia con il nome del meme.

### c) La slide 2 non reggeva da sola

Mosseri: *«If someone sees your carousel post but they don't swipe, we'll often
give that carousel a second chance and automatically move to that second piece of
media for the viewer.»* Instagram può cioè mostrare il carosello **partendo dalla
slide 2**. La nostra diceva solo «LA SCHEDA»: chi la incrociava non capiva di
cosa si stesse parlando.

Ora la slide 2 porta il nome del meme in evidenza.

---

## 3. Il punto su cui non sono d'accordo con te

Tu vuoi 3 post al giorno. I dati dicono che è troppo, e te li metto davanti
invece di eseguire e basta.

| Fonte | Dato |
|---|---|
| Metricool (24,3M post) | frequenza ottimale per un account 2K-10K: **7-14 post/settimana** |
| Buffer (2,1M post) | punto di massimo rendimento: **3-5/settimana**; oltre, rendimenti decrescenti |
| Quintly | da 1,5 a 2,5 post/giorno: **−9% engagement per post**; fino a 3,5: **−6% ulteriore** |
| Socialinsider | media osservata: 5 caroselli/mese |

3 al giorno fanno **21 a settimana**: il 50% sopra il tetto della banda ottimale,
e circa 16 volte la media di piattaforma.

**Non scatta nessuna penalità** — non esiste una regola che punisca la frequenza,
e Mosseri ha confermato che nemmeno la programmazione penalizza. Il problema è
diverso, ed è doppio.

Il primo è la cannibalizzazione: i tuoi tre post competono fra loro per la stessa
audience. Il totale giornaliero cresce, ma sub-linearmente, e la reach per post
cala.

Il secondo è più serio. Il segnale numero uno per raggiungere pubblico nuovo —
dichiarato da Mosseri il 22 gennaio 2025 — sono i **sends**, le condivisioni in
DM. Non i salvataggi, non i commenti: quante persone mandano il tuo post a un
amico. È una metrica di qualità pura. 90 schede al mese con ricerca vera,
verifica delle fonti e scrittura curata non sono sostenibili: la prima cosa che
cede è esattamente ciò che spinge qualcuno a mandare il post a un amico.

**La mia proposta: 2 al giorno, 14 a settimana.** Resti dentro la banda ottimale,
la scorta di 21 schede copre 10 giorni invece di 7, e il task della domenica ha il
tempo di produrre materiale verificato senza tirare via.

Si cambia con una riga in `agente/contenuti.py`:

```python
ORARI = ["12:30", "19:00"]        # 2 al giorno, dentro la banda ottimale
# ORARI = ["12:30", "18:30", "21:00"]   # 3 al giorno, come da piano iniziale
```

Decidi tu: è la tua pagina. Ma volevo che la decisione la prendessi coi numeri
davanti.

---

## 4. Quanto si cresce davvero

Il dato che ridimensiona tutto, da Metricool 2026: **solo il 21% degli account
sotto i 10.000 follower ha registrato crescita nell'ultimo anno.** Quattro su
cinque non crescono affatto. E solo l'8,93% degli account cambia fascia in un
anno.

Crescita annua per fascia (Socialinsider, 35M post):

| Fascia | Crescita annua |
|---|---|
| 1–5K | 22,0% |
| 5–10K | 20,3% |
| 10–50K | 17,2% |
| 50–100K | 13,6% |

Views per post nella fascia 1-5K: **caroselli 993**, Reel 580, immagini 417. Nelle
fasce basse **il carosello batte il Reel**: la scelta di formato è quella giusta.

**Proiezione realistica.** Non esistono dati pubblicati sulla crescita mese per
mese di pagine italiane di nicchia partite da zero: quella che segue è una stima
costruita sui benchmark sopra, non un dato osservato.

| | Realistico | Buono | Eccellente |
|---|---|---|---|
| Mese 1 | 100–400 | 400–800 | 1.000+ |
| Mese 3 | 500–1.500 | 1.500–3.000 | 5.000+ |
| Mese 6 | 1.500–4.000 | 4.000–8.000 | 15.000+ |

E qui il punto che conta più di ogni tabella: **le pagine d'archivio non crescono
in modo lineare, crescono a gradini.** Una scheda che ricostruisce l'origine di un
meme che tutti conoscono ma nessuno sa spiegare è il contenuto che viene mandato
in DM in massa. Un singolo post così vale più di novanta schede ordinarie. È
questo che il segnale *sends* premia, e non il volume.

Nel mazzo attuale i candidati a fare quel salto sono tre: **la supercazzola**
(entrata nello Zingarelli, ha generato un linguaggio di programmazione),
**«io so' io»** (non è di Sordi, è di Belli, 1831) e **la corazzata Kotiomkin**
(mezza Italia cita male il titolo). Sono le schede da spingere, non da spendere
in un giovedì qualunque.

---

## 5. Dove sta il pubblico

Instagram Italia: **29,9 milioni di utenti**, +4,2% sull'anno. Ma il baricentro
reale è **25-34 anni** (~25,5% del totale), non 20-60.

Tradotto: la nostalgia che raggiunge più persone è quella del periodo
**2010-2018** — chi oggi ha 28 anni allora ne aveva 18. Bimbominkia, il Trota,
Osho, Er Faina, Rovazzi, #ciaone sono il cuore commerciale dell'archivio.
Fantozzi e l'uomo del Monte funzionano lo stesso, ma su una platea più stretta e
con un ruolo diverso: sono le schede che i quarantenni mandano ai coetanei, e i
sends valgono comunque.

**Il canale esterno con il miglior rapporto sforzo/rendimento è Reddit italiano:**

| Subreddit | Iscritti |
|---|---|
| r/memesITA | 498.232 |
| r/ITAGLIA | 229.251 |
| r/MemeItaliani | 104.004 |
| r/BancaDelMeme | 71.401 |
| **r/Lostmediaitalia** | **8.807** |

r/Lostmediaitalia è piccolo ed è letteralmente il nostro pubblico: gente che per
hobby ricostruisce l'origine di media italiani dimenticati. Ma va usato
**contribuendo**: la scheda si posta come testo integrale, l'account resta una
firma. Chi posta link viene rimosso, le regole anti-autopromozione lì sono
applicate sul serio.

---

## 6. Monetizzazione, per soglie reali

Niente di tutto questo esiste sotto i mille follower. Il primo mese non si
monetizza: si costruisce l'archivio.

### Cosa è davvero attivo in Italia

| Canale | Soglia | Stato |
|---|---|---|
| **Regali (stelle) sui Reel** | 5.000 follower al lancio, forse 500 oggi | Attivo in Italia — confermato da Meta, novembre 2023 |
| **Abbonamenti** | 10.000 follower | Attivo in Italia. Meta trattiene **0%**, Apple/Google **30%** |
| **Contenuti brandizzati** | nessuna | Attivo |
| **Creator Marketplace** | — | Italia storicamente esclusa; una fonte del 2026 dice riaperto, non confermato da Meta |
| **Bonus a invito** | — | Solo USA e Corea. **Non disponibili in Italia** |
| **Revenue share sulle views** | — | **Non esiste su Instagram.** Instagram non paga per le visualizzazioni |

Su un abbonamento da €9,99 sottoscritto da app incassi circa **€7**: Meta non
prende nulla, se lo prende Apple. Una stella vale **$0,01** per te, e il tuo
pubblico ne paga circa il doppio: per una pagina editoriale i regali sono rumore
di fondo, non una voce di bilancio.

**Il canale vero è e resta la sponsorizzazione.** Listino italiano 2026 (DeRev,
5.000 creator, 865.000 post):

| Fascia | Follower | Per contenuto |
|---|---|---|
| Nano | 100–1K | €50–300 |
| Micro | 1K–10K | **€300–1.000** |
| Mid-tier | 10K–100K | **€1.000–5.000** |
| Macro | 100K–1M | €5.000–15.000 |

Sono **prezzi di listino, non prezzi pagati**, e una pagina tematica senza volto
negozia sotto listino a parità di follower. Ma il mercato si muove nella nostra
direzione: micro **+5,6%**, mid-tier **+9,2%**, mentre i compensi celebrity calano
per il terzo anno consecutivo (**−9,5%**). I brand stanno spostando budget verso
l'engagement e via dalla notorietà. L'influencer marketing italiano vale **425
milioni nel 2026**, +10,4%.

Il numero che vale la pena tenere a mente: in Italia ci sono **285.000 creator
sopra i 10.000 follower**. Superare quella soglia non è entrare in un club
esclusivo — è entrare nel mercato.

### Le tre soglie

**1.000 follower — le prime collaborazioni.** Fascia nano, €50-300 a contenuto.
Poco, ma serve a costruire il portfolio e a capire chi ti cerca. In parallelo:
affiliazione Amazon sui **libri al 5%** — la percentuale più alta dopo moda e
lusso, e la categoria naturale per un archivio. Su un libro da €18 fanno €0,90 a
conversione: non è un reddito, è una copertura dei costi.

**5.000 — la newsletter diventa sensata.** Andrea Girolami (*Scrolling Infinito*)
indica 5.000 iscritti come la soglia in cui la monetizzazione diventa praticabile,
e oltre 10.000 aumentano le richieste inbound dai brand. Ha fatto **~50.000 euro
nel 2025 con 20-25.000 iscritti**, e la sua frase è la più istruttiva di tutta
questa ricerca: *«La newsletter da sola non fattura 50.000 euro ma li rende
possibili.»* Le tre gambe sono sponsorizzazioni (€300-1.000 a invio), consulenza,
formazione ed eventi.

Aspettative sulla conversione, perché qui girano numeri falsi: la mediana da
iscritto gratuito a pagante è **0,62%**, il quartile superiore sta fra 2% e 5%.
**Pianifica su 1-2%**, non sul 5-10% che si legge ovunque. Il churn dei paganti è
del 3-5% al mese: metà degli abbonati disdice entro 17 mesi.

**10.000 — si apre tutto.** Abbonamenti Instagram, fascia mid-tier del listino,
richieste inbound. È la soglia su cui puntare, ed è realisticamente a 6-12 mesi.

### Quello che MEMETECA può vendere e le altre pagine no

Questa è la parte che vale più delle tabelle. Una pagina che ricarica meme ha un
solo prodotto: lo spazio pubblicitario. Un archivio verificato ne ha quattro.

**L'archivio come prodotto.** Ventuno schede a settimana fanno ~1.100 voci in un
anno, ognuna con fonti verificate. È un'opera di consultazione, e non esiste in
italiano. Un libro è la conversione naturale: royalty italiane **6-8% sul
cartaceo, 20-25% sull'ebook**. Carlotta Perego (Cucina Botanica) ha venduto
**20.000 copie in prevendita** con 346.000 follower, circa due anni dopo l'inizio.
Ordine di grandezza: ~€1,18 a copia al 7%. Un ottimo risultato editoriale, non un
reddito annuo — ma è patrimonio, e apre porte.

**La competenza come servizio.** Il pattern Girolami: per audience piccole ma
qualificate, consulenza e formazione pesano più del contenuto. Chi sa ricostruire
e verificare l'origine di un fenomeno internet ha una competenza che agenzie e
redazioni comprano. Non serve aspettare i 10.000 follower per venderla.

**Le partnership editoriali, non pubblicitarie.** Il nostro interlocutore naturale
non è il brand di bevande: è **Treccani** (che ha già lemmatizzato bimbominkia e
ciaone), **il Post**, **Feltrinelli**, **Wired Italia**, i festival di cultura
digitale, le piattaforme streaming quando escono documentari sulla cultura pop
italiana. Sono collaborazioni che pagano meno di uno spot ma costruiscono
l'autorevolezza che poi permette di chiedere di più.

**Il licensing dell'archivio.** Non ho trovato **nessun caso italiano documentato
con numeri** di licensing di archivi da pagine Instagram. Lo segnalo come vuoto
informativo, non come opportunità dimostrata: se ci arriviamo, ci arriviamo per
primi e senza precedenti a cui appoggiarci.

---

## 7. I prossimi trenta giorni

1. **Sbloccare il token** e lasciar pubblicare l'automazione — nessun rischio di
   sembrare attività sospetta, che è esattamente il problema in cui siamo
   incappati oggi pubblicando dal browser.
2. **Decidere la frequenza**: 2 o 3 al giorno, coi numeri della sezione 3.
3. **Controllare Stato dell'account ogni lunedì.** È l'indicatore che conta.
4. **Chiudere la restrizione pubblicitaria** con il ricorso dall'app: serve per
   accedere ai programmi Meta più avanti.
5. **Reddit, una volta a settimana**, la scheda migliore, come testo integrale su
   r/Lostmediaitalia e r/memesITA. Contribuendo, non promuovendo.
6. **Misurare la cosa giusta.** Non i follower: **sends per reach**. Ogni scheda
   va giudicata su quanti l'hanno mandata a qualcuno. Dopo 30 giorni sapremo quale
   tipo di scheda spinge davvero, e il task della domenica potrà produrne di più.
7. **A 500 follower** aprire la newsletter. Non per monetizzarla: perché è
   l'unico canale che nessun cambio di algoritmo può togliere. Oggi tutto il
   progetto dipende da una policy Instagram che è cambiata due volte in
   quattordici mesi.

---

## Quattro cose che nessuno può dirti, e diffida di chi ci prova

- La soglia esatta oltre cui Instagram ti classifica «aggregatore»
- Il tasso di conversione da follower Instagram a iscritti newsletter
- Le tariffe **reali** (non di listino) per pagine tematiche senza volto
- I ricavi dichiarati di pagine italiane da 10k, 50k, 100k follower — ho cercato,
  non esistono: tutti gli articoli italiani sul tema ripubblicano lo stesso
  listino DeRev senza aggiungere un solo dato primario

---

**Fonti principali:** [Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained) · [Recommendations Eligibility](https://creators.instagram.com/blog/instagram-recommendations-eligibility-tips-creators) · [Mosseri, 22 gen 2025](https://www.instagram.com/p/DFFyRp-pINJ/) · [TechCrunch, stretta aggregatori 30 apr 2026](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/) · [Metricool Instagram Study 2026](https://metricool.com/press-release-instagram-study-2026/) · [Socialinsider benchmark](https://www.socialinsider.io/social-media-benchmarks/instagram) · [Buffer, frequenza](https://buffer.com/resources/how-often-to-post-on-instagram/) · [DeRev, compensi 2026](https://derev.com/2026/07/influencer-marketing-in-italia-compensi-degli-influencer-2026/) · [Meta Newsroom, monetizzazione](https://about.fb.com/news/2023/11/giving-creators-more-ways-to-earn-money-on-facebook-and-instagram/) · [Scrolling Infinito, 50.000 euro](https://scrollinginfinito.substack.com/p/come-ho-guadagnato-50000-euro-con) · [Il Post, newsletter Lucarelli](https://www.ilpost.it/2026/05/28/newsletter-selvaggia-lucarelli-successo/) · [Social Media Today, limite 5 hashtag](https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/)
