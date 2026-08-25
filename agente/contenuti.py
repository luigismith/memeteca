# -*- coding: utf-8 -*-
"""
MEMETECA — archivio dati dei meme schedati.
Ogni voce alimenta sia la caption Instagram sia le 3 slide del carosello.
Tutti i dati provengono da fonti verificate (campo `fonti`).
"""

# Console Windows in cp1252: senza questo, un accento fa morire lo script.
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

BRAND = {
    "nome": "MEMETECA",
    "payoff": "L'archivio ragionato del meme italiano",
    "handle": "@memeteca_italiana",
    "colori": {
        "carta": "#EFE7D8",
        "inchiostro": "#14110F",
        "rosso": "#C8341F",
        "grigio": "#8A8073",
        "carta_scura": "#E2D8C4",
    },
}

# Ordine di pubblicazione.
# lun-sab: 1 meme "internet classico", 1 "internet recente", 1 "cinema"
# domenica: monografia TV & pubblicità
#
# Frequenza: i dati (Metricool 24,3M post, Buffer 2,1M) collocano l'ottimo per un
# account 2K-10K a 7-14 post/settimana. Tre al giorno fanno 21: sopra la banda.
# Vedi docs/06_STRATEGIA.md, sezione 3. Le schede in eccesso slittano al giorno dopo.
# Tre slot, due post. A ogni slot una sessione guarda prima le notizie: se c'è
# un evento esce il bonus, altrimenti esce la scheda. Lo slot delle 21:00 è
# riservato all'attualità e resta vuoto se non c'è niente da dire.
# Il funzionamento completo è in docs/03_AGENTE_AUTONOMO.md.
ORARI = ["12:30", "18:30", "21:00"]
SCHEDE_AL_GIORNO = 2          # il terzo post esce solo se c'è una notizia
BONUS_AL_GIORNO = 1

INIZIO = "2026-08-07"    # primo giorno di calendario dopo il lancio del 6 agosto

MEMI = [

# ───────────────────────────── LUNEDÌ ─────────────────────────────
{
 "num": "001", "giorno": "Lunedì", "slot": 0, "categoria": "INTERNET · 2005",
 "titolo": "NONCICLOPEDIA",
 "occhiello": "Il giorno in cui l'Italia difese una parodia di Wikipedia",
 "anno": "2005",
 "creatore": "Progetto wiki collettivo, autori in larga parte anonimi. Nel 2011 il protagonista involontario è Vasco Rossi.",
 "prima_apparizione": "3 novembre 2005, come sito autonomo su MediaWiki — versione italiana del format Uncyclopedia.",
 "origini": "Parodia integrale di Wikipedia: stessa grafica, stessa struttura a voci, contenuto interamente satirico. Il claim del sito è che «Wikipedia è la parodia di un'enciclopedia».",
 "storia": "Diventa la fabbrica di meme testuali dell'internet italiano dell'era forum. Nel 2010 un legale di Vasco Rossi chiede la rimozione della voce sul cantante e i dati degli utenti. Nel 2011 tre amministratori vengono convocati dalla polizia postale: il 3 ottobre lo staff chiude il sito per protesta, oscurando oltre 12.000 voci. In poche ore 150.000 persone si schierano su Facebook. Il 4 ottobre la querela viene ritirata e il sito riapre.",
 "significato": "Il primo grande caso italiano di scontro fra satira online e diritto alla reputazione. Ancora oggi è il precedente che si cita quando qualcuno minaccia querela a una pagina satirica.",
 "chicca": "Il blackout di protesta durò meno di 24 ore: probabilmente la serrata più breve e più efficace della storia del web italiano.",
 "dopo": "Il sito è tuttora attivo: a febbraio 2025 contava 14.482 voci e oltre 2,4 milioni di modifiche complessive.",
 "confidenza": "alta",
 "fonti": ["ilpost.it (3 e 4 ott 2011)", "Wikipedia IT", "Fanpage"],
 "hook": "Nel 2011 l'Italia si è spaccata in due per difendere una parodia di Wikipedia. È durata un giorno. Ha vinto la parodia.",
 "hashtags": "#nonciclopedia #vascorossi #memeteca #internetitaliano #storiadeimeme",
},
{
 "num": "002", "giorno": "Lunedì", "slot": 1, "categoria": "INTERNET · 2020",
 "titolo": "NON CE N'È COVIDDI",
 "occhiello": "Il tormentone che la sua protagonista ha poi rinnegato",
 "anno": "2020",
 "creatore": "Angela Chianello, poi «Angela da Mondello». Protagonista involontaria: non è un meme progettato, è un ritaglio televisivo. Autore del ritaglio virale: ignoto.",
 "prima_apparizione": "Estate 2020, su Canale 5 a «Live – Non è la d'Urso». La data esatta della messa in onda non è documentata in modo univoco; l'esplosione virale è tracciata fra fine luglio e agosto 2020.",
 "origini": "Un'inviata chiede a Chianello, in spiaggia a Mondello, se non tema il contagio. La risposta in siciliano stretto — «non ce n'è coviddi» — arriva insieme ad altri due tormentoni nati nello stesso spezzone: «da Mondello» e «oggi ammare».",
 "storia": "Il ritaglio viene estratto dal contesto TV e rilanciato dalle pagine trash. Nascono remix in autotune, magliette e perfino un videogioco browser amatoriale (documentato dal Giornale di Sicilia il 29 luglio 2020). A settembre 2020 Chianello apre un profilo Instagram ufficiale e supera 100.000 follower in meno di 24 ore. Come controreazione parte l'#AlbertoAngelaChallenge, «in difesa della cultura».",
 "significato": "Si usa per irridere la negazione della realtà davanti all'evidenza: dal negazionismo sanitario a qualunque rimozione ostinata di un problema.",
 "chicca": "Il 9 ottobre 2020 la protagonista pubblica un video di dietrofront: «il virus c'è, siamo messi male, usate la mascherina». Il meme viene rinnegato da chi lo ha involontariamente creato, due mesi dopo il picco.",
 "dopo": "A novembre 2020 gira sulla stessa spiaggia il videoclip della canzone «Non ce n'è»: scattano accertamenti di polizia e carabinieri per occupazione abusiva di area demaniale e violazione delle norme anti-Covid.",
 "confidenza": "alta sul meme, media sulla data di messa in onda",
 "fonti": ["Open (9 ott 2020)", "Sky TG24 (9 nov 2020)", "Tgcom24"],
 "hook": "Il tormentone dell'estate 2020 è durato due mesi. Poi la protagonista ha girato un video per dire che aveva sbagliato. Nessuno se lo ricorda.",
 "hashtags": "#noncenecoviddi #angeladamondello #memeteca #memeitaliani #estate2020",
},
{
 "num": "003", "giorno": "Lunedì", "slot": 2, "categoria": "CINEMA · 1975",
 "titolo": "LA SUPERCAZZOLA",
 "occhiello": "«Tarapìa tapiòco! Prematurata la supercazzola, o scherziamo?»",
 "anno": "1975",
 "creatore": "Ugo Tognazzi (conte Mascetti). Regia di Mario Monicelli, soggetto e sceneggiatura di Pietro Germi, Leonardo Benvenuti, Piero De Bernardi e Tullio Pinelli. Germi ideò il film ma morì nel 1974: i titoli recitano «un film di Pietro Germi», poi «regia di Mario Monicelli».",
 "prima_apparizione": "«Amici miei», nelle sale il 24 ottobre 1975. La gag: Mascetti confonde il vigile Paolini con uno sproloquio nonsensico detto con assoluta serietà.",
 "origini": "L'invenzione del termine è contesa: viene attribuita al cantautore-attore Corrado Lojacono, mentre secondo una testimonianza di Monicelli il meccanismo deriverebbe dalle trovate del cabarettista Marcello Casco, che sfotteva le autorità con conversazioni prive di senso. Il genere ha precedenti in Boccaccio, Rabelais, Swift e Totò.",
 "storia": "È il caso italiano meglio documentato di battuta cinematografica con seconda vita digitale: generatori automatici di supercazzole e persino un linguaggio di programmazione esoterico open source chiamato «Monicelli», su GitHub, con sintassi costruita sul lessico del film.",
 "significato": "Oggi «supercazzola» indica un discorso volutamente involuto e vuoto, costruito per non rispondere. Si usa soprattutto in politica, in azienda e nei talk show. Non è più una citazione: è una categoria di critica pubblica.",
 "chicca": "È entrata nello Zingarelli nel 2015 (edizione 2016): una delle pochissime battute del cinema italiano diventate lemma di dizionario, e l'unica ad aver generato un linguaggio di programmazione funzionante.",
 "dopo": "Dettaglio che quasi nessuno sa: nel primo film Tognazzi dice «supercazzora», con la r. La forma con la l si è imposta nell'uso comune e compare in «Amici miei atto II» — ed è quella entrata nel dizionario.",
 "reperto": {"tipo": "lemma", "bollo": "Il lemma",
   "voce": "supercazzòla", "grammatica": "s. f. (fam., scherz.)",
   "definizione": "discorso senza senso, fatto per confondere l'interlocutore.",
   "fonte": "Voce entrata nello Zingarelli nel 2015, edizione 2016. Ricostruzione tipografica, non riproduzione."},
 "confidenza": "alta",
 "fonti": ["Wikipedia IT", "La Nazione", "github.com/esseks/monicelli"],
 "hook": "Una battuta senza senso del 1975 è finita sullo Zingarelli e ha generato un linguaggio di programmazione vero. Con rispetto parlando.",
 "hashtags": "#supercazzola #amicimiei #monicelli #memeteca #cinemaitaliano",
},

# ───────────────────────────── MARTEDÌ ─────────────────────────────
{
 "num": "004", "giorno": "Martedì", "slot": 0, "categoria": "INTERNET · 2015",
 "titolo": "LE PIÙ BELLE FRASI DI OSHO",
 "tag": "@federicopalmaroli",
 "occhiello": "«I pomodori non sanno più de niente»",
 "anno": "2015",
 "creatore": "Federico Palmaroli, romano, impiegato (Il Post lo indica alla Camera di Commercio, Il Fatto Quotidiano come assicuratore). Il volto è quello del mistico indiano Osho Rajneesh, morto nel 1990 ed estraneo all'operazione.",
 "prima_apparizione": "23 febbraio 2015, pagina Facebook. La prima vignetta recitava: «I pomodori non sanno più de niente».",
 "origini": "Palmaroli si imbatte online in una pagina di seguaci di Osho che pubblicava citazioni autentiche del maestro. Ha l'idea di accostare a quel volto una frase quotidiana in romanesco. Il meccanismo comico è il cortocircuito tra l'aura spirituale dell'immagine e la banalità dialettale della didascalia.",
 "storia": "Crescita esplosiva: in una prima fase circa 5.000 fan al giorno. Ad aprile 2016 la pagina conta 320.000 follower con una media di 3.000 condivisioni per post; a giugno supera i 350.000 «mi piace». Il 7 aprile 2016 esce il libro «Le più belle frasi di Osho. Ma fa 'n po' come cazzo te pare» (MagicPress): ogni meme è accostato a una citazione autentica di Osho sulla stessa lunghezza d'onda.",
 "significato": "«Una frase da Osho» indica oggi, in italiano corrente, una banalità travestita da saggezza. La pagina è diventata nel tempo un osservatorio satirico sulla politica italiana.",
 "chicca": "Palmaroli ha spiegato al Post che l'effetto dipende dall'accento: «quando ci metti anche l'accento romanesco l'effetto è ancora più detonante».",
 "dopo": "Nel gennaio 2021 la pagina viene improvvisamente oscurata da Facebook, con accuse di censura politica e un caso mediatico nazionale. Facebook la ripristina dichiarando che era stata rimossa per errore.",
 "confidenza": "alta",
 "fonti": ["Il Post (23 giu 2016)", "Il Fatto Quotidiano (7 apr 2016)", "AGI"],
 "hook": "Un impiegato romano ha preso la faccia di un mistico indiano morto nel 1990 e ci ha scritto sotto che i pomodori non sanno più de niente. Undici anni dopo è un genere letterario.",
 "hashtags": "#osho #lepiubellefrasidiosho #memeteca #romanesco #memeitaliani",
},
{
 "num": "005", "giorno": "Martedì", "slot": 1, "categoria": "INTERNET · 2019",
 "titolo": "IO SONO GIORGIA",
 "occhiello": "Il remix che doveva affondarla e le ha dato il titolo dell'autobiografia",
 "anno": "2019",
 "creatore": "Il duo mem&j: due ventenni milanesi rimasti sempre anonimi, all'epoca impiegati in zona industriale a Milano. Si definivano autori di musica «tamarra» fatta «da gente che non sa cantare».",
 "prima_apparizione": "26 ottobre 2019: il brano viene suonato per la prima volta al Toilet Club di Milano, locale LGBTQI+ friendly, e caricato su YouTube.",
 "origini": "Il sample viene dal comizio del centrodestra in Piazza San Giovanni a Roma del 19 ottobre 2019: «Io sono Giorgia, sono una donna, sono una madre, sono italiana, sono cristiana». mem&j lo campionano su una base dance e lo rovesciano, inserendo riferimenti a «genitore 1 e genitore 2» e slogan LGBTQI+.",
 "storia": "In poche settimane supera i 6 milioni di visualizzazioni. Tommaso Zorzi è tra i primi amplificatori. Nascono la #SonoGiorgiaChallenge, filtri Instagram, decine di rifacimenti; M¥SS KETA lo mette in scaletta, Malgioglio ne fa una sua versione. Diventa hit da discoteca dell'inverno 2019-2020.",
 "significato": "Nato come satira contro la retorica identitaria, si è svincolato dall'intento originale: oggi è la formula per parodiare qualunque autodefinizione enfatica, e il caso-scuola italiano di backfire comunicativo.",
 "chicca": "Ha dato il titolo all'autobiografia di Meloni, «Io sono Giorgia» (Rizzoli, maggio 2021), che nell'introduzione cita esplicitamente il remix. Meloni ha dichiarato al Corriere: «improvvisamente è come se il mondo si fosse accorto di quello che dico».",
 "dopo": "mem&j hanno scelto di non monetizzare né il brano né il canale, mantenendo lavoro d'ufficio e anonimato. Nel 2021 hanno detto a Open che oggi lo rifarebbero «in modo molto più critico, senza lasciare spazio a manipolazioni».",
 "reperto": {"tipo": "citazione", "bollo": "Il campione",
   "testo": "«Io sono Giorgia, sono una donna, sono una madre, sono italiana, sono cristiana.»",
   "fonte": "Comizio di Piazza San Giovanni, Roma, 19 ottobre 2019 — le nove parole campionate da mem&j. Citazione a fini di critica e discussione (art. 70 L. 633/1941)."},
 "confidenza": "alta",
 "fonti": ["Open (18 mag 2021)", "Sky TG24 (12 nov 2019)", "Il Fatto Quotidiano"],
 "hook": "Due impiegati milanesi hanno campionato un comizio per prenderlo in giro. Il bersaglio ci ha intitolato l'autobiografia. Loro non ci hanno guadagnato un euro, per scelta.",
 "hashtags": "#iosonogiorgia #memj #memeteca #memeitaliani #storiadeimeme",
},
{
 "num": "006", "giorno": "Martedì", "slot": 2, "categoria": "CINEMA · 1976",
 "titolo": "UNA CAGATA PAZZESCA",
 "occhiello": "«Per me… la corazzata Kotiomkin… è una cagata pazzesca!»",
 "anno": "1976",
 "creatore": "Paolo Villaggio (Ugo Fantozzi), anche co-sceneggiatore con Luciano Salce (regista), Leonardo Benvenuti e Piero De Bernardi.",
 "prima_apparizione": "«Il secondo tragico Fantozzi», 1976, regia di Luciano Salce. Scena: il cineforum aziendale imposto dal professor Guidobaldo Maria Riccardelli. Fantozzi si alza, pronuncia la battuta e riceve «92 minuti di applausi».",
 "origini": "Nel film il titolo NON è «Potëmkin» ma «La corazzata Kotiomkin»: non era possibile usare le scene originali di Ejzenštejn, così si scelse la parodia — e anche il regista fu storpiato in «Serghei M. Einstein». La finta corazzata fu girata da Salce sulla Scalea Bruno Zevi a Roma e la pellicola volutamente «maltrattata» per simulare l'invecchiamento.",
 "storia": "L'espressione entra prima nel parlato quotidiano (Il Post la elenca tra «le cose che diciamo per via di Paolo Villaggio», usata per stroncare la cultura-alta-e-noiosa) e poi diventa formato meme: template dedicato su Imgflip, soundboard, GIF e reel. Picchi alla morte di Villaggio, il 3 luglio 2017.",
 "significato": "Stroncatura irriverente di qualunque opera o iniziativa percepita come pretenziosa, noiosa o sopravvalutata. Spesso in coppia con «92 minuti di applausi», usato al contrario per gli elogi eccessivi.",
 "chicca": "Villaggio spiegò nel 2015 il vero senso della battuta: «Non perché fosse davvero una cagata pazzesca, ma perché era un film all'antica e noioso. La corazzata era anche la rivolta degli intellettuali, che non osavano dire una cosa di quel tipo».",
 "dopo": "Nella finzione la Kotiomkin è composta da 18 bobine, per esasperare gli impiegati. L'originale di Ejzenštejn dura 75 minuti.",
 "confidenza": "alta",
 "fonti": ["Wikipedia IT", "Il Post (3 lug 2017)", "Genova24"],
 "hook": "Metà del Paese cita male il titolo del film. Nel film non si chiama Potëmkin: si chiama Kotiomkin. La citazione popolare ha corretto il cinema, non viceversa.",
 "hashtags": "#fantozzi #paolovillaggio #corazzatakotiomkin #memeteca #cinemaitaliano",
},

# ───────────────────────────── MERCOLEDÌ ─────────────────────────────
{
 "num": "007", "giorno": "Mercoledì", "slot": 0, "categoria": "INTERNET · 2007",
 "titolo": "BORIS",
 "tag": "@boris_laserie_italia",
 "tag_ufficiale": False,
 "occhiello": "«A cazzo di cane», «smarmellare», «troppo italiano»",
 "anno": "2007",
 "creatore": "Soggetto di Luca Manzi e Carlo Mazzotta; sceneggiatura di Mattia Torre, Giacomo Ciarrapico e Luca Vendruscolo. I volti dei tormentoni: Francesco Pannofino (René Ferretti), Pietro Sermonti (Stanis La Rochelle), Ninni Bruschetta (Duccio).",
 "prima_apparizione": "16 aprile 2007 su Fox, canale satellitare. La prima stagione va in onda fino al 9 luglio.",
 "origini": "Sitcom meta-televisiva ambientata sul set di una fiction Rai scadente, «Gli occhi del cuore». Doveva intitolarsi «Sampras» — nella finzione è il nome del pesce rosso del regista — ma il nome era già stato acquisito commercialmente da Nike: l'episodio pilota con quel titolo non andò mai in onda.",
 "storia": "Flop di ascolti alla prima messa in onda. Un dirigente Fox Italia lo ha ammesso al Post: «Boris ha avuto pochissimi spettatori ed è diventata di culto grazie al passaparola e alla pirateria». È questo che la rende un fenomeno internet: la serie viene consumata su forum e siti di download, anticipando il modello on-demand. Arriva in chiaro solo due anni e mezzo dopo. Poi Netflix genera una seconda ondata.",
 "significato": "«A cazzo di cane» = fatto senza cura. «Smarmellare» = lavorare in modo tecnicamente sciatto. «Troppo italiano» = la critica snob e autorazzista di Stanis. «Dai dai dai» e «Genio!» = il falso entusiasmo del capo. Sono lessico corrente, non citazioni.",
 "chicca": "Gli sceneggiatori interni alla finzione inventano la «Festa del Grazie» per italianizzare il Ringraziamento americano: la gag che riassume tutta la loro pigrizia creativa, diventata a sua volta citazione ricorrente.",
 "dopo": "Tre stagioni fra 2007 e 2010, poi un film e una quarta stagione su Disney+. Mattia Torre è morto nel 2019.",
 "confidenza": "alta",
 "fonti": ["Il Post (16 feb 2021)", "TheVision", "Wikipedia IT"],
 "hook": "La serie che ha regalato all'italiano parlato più espressioni di qualsiasi altra degli ultimi vent'anni è stata, alla prima messa in onda, un flop totale. L'ha salvata la pirateria.",
 "hashtags": "#boris #renéferretti #acazzodicane #memeteca #serietvitaliane",
},
{
 "num": "008", "giorno": "Mercoledì", "slot": 1, "categoria": "INTERNET · 2023",
 "titolo": "PENSATI PARACULA",
 "occhiello": "Il pandoro, la tuta grigia e le scuse più parodiate d'Italia",
 "anno": "2023",
 "creatore": "Produzione collettiva del web italiano. Catalizzatore riconosciuto: Federico Palmaroli («Le più belle frasi di Osho») con la vignetta «Pensati paracula». Protagonista: Chiara Ferragni.",
 "prima_apparizione": "Il video di scuse esce su Instagram lunedì 18 dicembre 2023. La valanga di meme parte nelle ore successive su X, Instagram e TikTok.",
 "origini": "Il 15 dicembre 2023 l'Antitrust sanziona le società Ferragni (1.075.000 €) e Balocco (420.000 €): quasi 1,5 milioni in tutto. La campagna del «Pandoro Pink Christmas» lasciava intendere che l'acquisto contribuisse a una donazione al Regina Margherita, mentre la donazione era già fissata a prescindere dalle vendite. Il materiale sorgente del meme è il video di scuse — e la tuta grigia, letta dal web come sobrietà penitenziale studiata.",
 "storia": "In poche ore fotomontaggi, parodie, confronti con il video in lacrime di Soumahoro dell'anno prima. «Pensati paracula» è il détournement di «Pensati libera», lo slogan portato sul palco di Sanremo 2023. Il format «scuse in tuta grigia» diventa un template per qualunque scandalo reputazionale.",
 "significato": "Si usa per irridere le scuse pubbliche performative e la beneficenza usata come leva di marketing.",
 "chicca": "Il caso ha prodotto una legge: ne è derivato un intervento normativo sugli obblighi di trasparenza per chi associa beneficenza a operazioni commerciali — il cosiddetto «ddl Ferragni».",
 "dopo": "Il 14 gennaio 2026 il Tribunale di Milano dichiara il non doversi procedere. Non è un'assoluzione nel merito: caduta l'aggravante, il fatto resta truffa semplice, procedibile solo a querela — e la querela del Codacons era già stata rimessa dopo un accordo risarcitorio.",
 "confidenza": "alta",
 "fonti": ["Il Post (15 dic 2023 e 14 gen 2026)", "Secolo d'Italia", "Dire"],
 "hook": "Due parole di una pagina satirica hanno raccontato il caso meglio di tre anni di processo. E la vicenda ha finito per generare una legge.",
 "hashtags": "#pandorogate #chiaraferragni #pensatiparacula #memeteca #memeitaliani",
},
{
 "num": "009", "giorno": "Mercoledì", "slot": 2, "categoria": "CINEMA · 1981",
 "titolo": "IO SO' IO",
 "occhiello": "«Mi dispiace, ma io so' io e voi non siete un cazzo»",
 "anno": "1981",
 "creatore": "Alberto Sordi (marchese Onofrio del Grillo), regia di Mario Monicelli. Ma la battuta NON è materiale di sceneggiatura: è un verso di Giuseppe Gioachino Belli.",
 "prima_apparizione": "«Il marchese del Grillo», nelle sale il 22 dicembre 1981. Il marchese la pronuncia davanti a popolani arrestati in un'osteria.",
 "origini": "Viene dal sonetto romanesco «Li soprani der monno vecchio» di Belli, datato 21 gennaio 1831: «Io sò io, e vvoi nun zete un cazzo». Il film riprende una satira sul potere scritta 150 anni prima. Anche il personaggio ha una base storica: Onofrio del Grillo fu un nobile realmente esistito nella Roma papalina, noto per le burle — anche se separare i fatti dalle leggende è ormai impossibile.",
 "storia": "La frase passa nel linguaggio comune come formula di arroganza di casta ed è tra le dieci battute del cinema italiano entrate nel parlato quotidiano. Online è diventata la didascalia standard dei meme politici, in versione integrale o abbreviata («io so' io»), e clip virale su YouTube, Facebook e TikTok.",
 "significato": "Si usa quasi sempre in chiave critica per denunciare abuso di potere, privilegio, arroganza di chi si sente intoccabile per ruolo o rango. È una scorciatoia retorica del dibattito italiano su caste e disuguaglianze.",
 "chicca": "Il film vinse l'Orso d'argento per la miglior regia a Berlino 1982 e fu il secondo maggior incasso della stagione italiana. Durante le riprese ci furono forti contrasti fra Flavio Bucci e Alberto Sordi: teatro classico contro avanspettacolo e radio.",
 "dopo": "La scena della decapitazione con la ghigliottina fu tagliata nelle successive trasmissioni televisive, lasciando solo l'inquadratura di spalle.",
 "reperto": {"tipo": "citazione", "bollo": "L'originale",
   "testo": "«C'era una vorta un Re cche ddar palazzo / mannò ffora a li popoli st'editto: / Io sò io, e vvoi nun zete un cazzo.»",
   "fonte": "Giuseppe Gioachino Belli, «Li soprani der monno vecchio», 21 gennaio 1831 — 150 anni prima del film. Testo di pubblico dominio."},
 "confidenza": "alta su origine e attribuzione",
 "fonti": ["Wikipedia IT", "Il Giornale", "Babbel Magazine"],
 "hook": "La battuta più citata sul potere in Italia non l'ha scritta uno sceneggiatore nel 1981. L'ha scritta un poeta romano il 21 gennaio 1831.",
 "hashtags": "#ilmarchesedelgrillo #albertosordi #iosoio #memeteca #cinemaitaliano",
},

# ───────────────────────────── GIOVEDÌ ─────────────────────────────
{
 "num": "010", "giorno": "Giovedì", "slot": 0, "categoria": "INTERNET · 2011",
 "titolo": "IL TROTA",
 "occhiello": "Il soprannome che ha inventato una categoria del linguaggio politico",
 "anno": "2011",
 "creatore": "Protagonista involontario: Renzo Bossi, figlio di Umberto Bossi e allora consigliere regionale della Lombardia. Il soprannome non nasce sul web: secondo Il Sussidiario fu il padre a chiamarlo «Trota». La data di coniazione non è documentata.",
 "prima_apparizione": "Come meme: estate-settembre 2011. Il video che innesca tutto è un'intervista a un convegno intitolato «Vecchia TV vs nuova TV» (luglio 2011). L'8 settembre 2011 Quotidiano Nazionale documenta la pagina Facebook «il Trota ha detto», già oltre 20.000 iscritti.",
 "origini": "Incrocio fra un soprannome familiare, un video di pessima performance comunicativa e il contesto politico: il figlio del leader piazzato in Consiglio regionale. Il format della pagina replica le barzellette «Pierino ha detto», attribuendo a Bossi jr. frasi fittizie.",
 "storia": "Propagazione classica del 2011: video YouTube → hashtag #trota su Twitter → pagina Facebook aggregatrice → ripresa dai quotidiani. Il picco assoluto arriva nel 2012 con lo scandalo sui fondi della Lega e la laurea conseguita in Albania.",
 "significato": "«Il Trota» è diventato in italiano un'antonomasia: il figlio incapace piazzato dal padre potente. Sinonimo di nepotismo politico.",
 "chicca": "Bertram Niessen, su Doppiozero, aveva iniziato un pezzo satirico contro Renzo Bossi e si è fermato a metà: ha riconosciuto la vulnerabilità del bersaglio, ha rinunciato all'articolo e ha chiuso scrivendo di essere andato a fare un giro in bicicletta. È una delle pochissime riflessioni pubbliche italiane dell'epoca sul costo umano del meme di massa.",
 "dopo": "Ha lasciato la politica. Oggi è imprenditore agricolo: ha avviato con il fratello un caseificio artigianale.",
 "confidenza": "alta sulla cronologia, media sull'origine del soprannome",
 "fonti": ["Quotidiano Nazionale (8 set 2011)", "Doppiozero", "Il Fatto Quotidiano"],
 "hook": "Un soprannome familiare è diventato in un'estate una parola del vocabolario politico italiano. Nel 2011 qualcuno si chiese già se fosse giusto. Fu l'unico.",
 "hashtags": "#iltrota #renzobossi #memeteca #memeitaliani #storiadeimeme",
},
{
 "num": "011", "giorno": "Giovedì", "slot": 1, "categoria": "INTERNET · 2022",
 "titolo": "TANANAI ULTIMO",
 "tag": "@tananaimusica",
 "occhiello": "Come si vince un festival arrivando venticinquesimo",
 "anno": "2022",
 "creatore": "Alberto Cotta Ramusino, in arte Tananai, classe 1995, di Cologno Monzese. Meme collettivo; tra gli acceleratori riconosciuti la pagina Instagram Socialisti Gaudenti.",
 "prima_apparizione": "Festival di Sanremo 2022, 1-5 febbraio, Rai 1. L'esplosione meme è immediata su Instagram, Twitter e TikTok.",
 "origini": "Due elementi sorgente. L'esibizione della prima serata con «Sesso occasionale», palesemente stonata. E soprattutto l'ultimo posto (25°) accolto con festeggiamenti invece che con imbarazzo, più la battuta dal palco «ci vediamo all'Eurovision, ragazzi», sapendo benissimo di non andarci.",
 "storia": "Il web ribalta la sconfitta in trionfo: meme, edit, cover. Su TikTok «Sesso occasionale» viene reinterpretata anche da Jovanotti. Tananai alimenta lui stesso il meme con autoironia continua (per andare all'Eurovision servirebbe «la rinuncia degli altri 24 cantanti»). Il brano supera 1,4 milioni di stream e i concerti già programmati a Milano e Roma vengono spostati in venue più capienti.",
 "significato": "È il caso-scuola italiano dell'ultimo posto come vittoria social. Si usa per chi trasforma un fallimento pubblico in capitale reputazionale grazie all'autoironia — e come prova che in epoca social la classifica conta meno della conversazione che generi.",
 "chicca": "Prima di arrivare a Sanremo la canzone si intitolava «Not for us». E la copertina del singolo mostrava un preservativo arancione.",
 "dopo": "Rivincita completa: torna a Sanremo nel 2023 con «Tango» e arriva quinto. Nel frattempo «La dolce vita» con Fedez e Mara Sattei è tra i tormentoni dell'anno.",
 "confidenza": "alta",
 "fonti": ["Open (12 feb 2022)", "Fanpage", "Il Fatto Quotidiano"],
 "hook": "È arrivato venticinquesimo su venticinque e ha festeggiato. Un anno dopo è arrivato quinto. Il pubblico non premia chi vince: premia chi non finge.",
 "hashtags": "#tananai #sanremo2022 #sessooccasionale #memeteca #musicaitaliana",
},
{
 "num": "012", "giorno": "Giovedì", "slot": 2, "categoria": "CINEMA · 1954",
 "titolo": "MACCARONE M'HAI PROVOCATO",
 "occhiello": "«E io ti distruggo adesso, io me te magno!»",
 "anno": "1954",
 "creatore": "Alberto Sordi nel ruolo di Nando Mericoni, in arte «Santi Bailor». Regia di Steno; Sordi figurava anche tra gli sceneggiatori. Il personaggio non nasce con questo film: era già apparso in «Un giorno in pretura» (1953) e fu inventato dall'aiuto regista Lucio Fulci.",
 "prima_apparizione": "«Un americano a Roma», nelle sale il 10 dicembre 1954. Nando, ossessionato dal mito americano, rifiuta la cucina italiana e prova a cenare con latte, marmellata e senape — poi cede davanti a un piatto di maccheroni.",
 "origini": "Parzialmente non documentate. Le fonti attendibili non confermano né il numero di piatti che Sordi avrebbe mangiato né una scrittura preventiva della battuta. Una ricostruzione (Velvet Cinema, 2023) la attribuisce a un momento di set durante la sessione fotografica, ma non è confermata dalle voci enciclopediche: va presa con cautela.",
 "storia": "È il più longevo meme gastronomico italiano: GIF, short e reel su YouTube, Instagram, TikTok e Threads, e citazione standard nei contenuti food. Nessuna data di nascita documentata: la diffusione è continua, alimentata dalla natura visiva della scena, formato perfetto per le clip brevi.",
 "significato": "Si usa scherzosamente per la resa golosa davanti al cibo, e più in generale per chi cede a ciò che diceva di rifiutare. È anche l'emblema del contrasto tra esterofilia posticcia e identità italiana.",
 "chicca": "Nel film compare in un ruolo minore Ursula Andress, e Lucio Fulci appare nella scena del party. Sul set furono fotografati anche i figli di Steno: Enrico e Carlo Vanzina.",
 "dopo": "Nel 2008 il film è entrato nella lista dei «100 film italiani da salvare». A Narni c'è un murale dedicato a Sordi con questa battuta.",
 "confidenza": "media — film e datazione certi, retroscena della battuta non confermato",
 "fonti": ["Wikipedia IT/EN", "Velvet Cinema (2023)", "Corriere dell'Umbria"],
 "hook": "Settant'anni fa un romano fingeva di essere americano e si arrendeva a un piatto di pasta. È ancora la GIF più usata d'Italia sotto le foto di cibo.",
 "hashtags": "#albertosordi #unamericanoaroma #maccarone #memeteca #cinemaitaliano",
},

# ───────────────────────────── VENERDÌ ─────────────────────────────
{
 "num": "013", "giorno": "Venerdì", "slot": 0, "categoria": "INTERNET · 2011",
 "titolo": "ANDREA DIPRÈ",
 "tag": "@andreadipreshow",
 "occhiello": "L'avvocato critico d'arte che ha inventato il trash italiano post-social",
 "anno": "2011",
 "creatore": "Andrea Diprè, nato a Tione di Trento il 9 novembre 1974, laureato in Giurisprudenza a Trento, autoproclamato critico d'arte. È insieme creatore dei propri contenuti e oggetto del meme.",
 "prima_apparizione": "Come fenomeno virale, dal 2011-2012 con il passaggio a YouTube. Il momento di svolta memetica è l'intervista del gennaio 2013 all'artista Osvaldo Paniccia, indicata da Know Your Meme come il video che lo consacra.",
 "origini": "Non nasce su internet ma in televisione. Comincia intorno al 2001 su emittenti locali, poi Telepadania e La 9 con «Le scelte di Andrea Diprè», recensendo opere di artisti di provincia. Passa a RAI2 e al Maurizio Costanzo Show. Dal 2005 al 2012 affitta canali Sky dedicati.",
 "storia": "La svolta è lo YouTube Poop italiano: il contrasto fra il tono vocale bassissimo dell'anziano Paniccia e l'eccitazione dell'intervistatore genera un'ondata di remix. Passaggio decisivo per la notorietà negativa: «Mi manda Raitre» del 20 ottobre 2011, in cui un inviato sotto copertura si finge artista e smaschera la vendita di spazi televisivi.",
 "significato": "È la figura fondativa del trash italiano post-social. Abito blu, camicia bianca, cravatta rossa, espressione fissa: identità visiva riconoscibilissima e continuamente parodiata. Il suo nome è sinonimo di intervistatore che dà dignità apparente a contenuti degradanti.",
 "chicca": "Prima di diventare leghista, nel 1998 si era candidato con partiti di centro-sinistra.",
 "dopo": "Dal 2015 i contenuti virano stabilmente sul materiale per adulti. Link – Idee per la televisione lo descrive oggi come intrappolato tra il personaggio che ha creato e la propria irrilevanza.",
 "confidenza": "media-alta — alcuni dettagli sono riportati come voci anche dalle fonti",
 "fonti": ["Know Your Meme", "Link – Idee per la televisione", "Occhio di Salerno"],
 "hook": "Prima di TikTok, prima del trash da algoritmo, c'era un avvocato trentino in cravatta rossa che intervistava chiunque con la faccia di chi sta parlando con Picasso.",
 "hashtags": "#andreadipre #memeteca #trashitaliano #youtubepoop #storiadeimeme",
},
{
 "num": "014", "giorno": "Venerdì", "slot": 1, "categoria": "INTERNET · 2016",
 "titolo": "ANDIAMO A COMANDARE",
 "tag": "@rovazzi",
 "occhiello": "Il momento in cui il meme italiano è diventato industria discografica",
 "anno": "2016",
 "creatore": "Fabio Rovazzi, all'epoca videomaker e non cantante: «non so cantare, non ho mai cantato in vita mia se non nel coro delle medie». Base musicale di Merk & Kremont.",
 "prima_apparizione": "Il videoclip esce sui suoi canali il 28 febbraio 2016; su Spotify dal 18 marzo, su iTunes a giugno per Newtopia/Universal.",
 "origini": "Il titolo viene da un video virale preesistente in cui un uomo trasandato su un trattore diceva «in tuta andiamo a comandare». Rovazzi trova comica l'espressione sgrammaticata e ci costruisce sopra un brano: la canzone è letteralmente la trasformazione di un meme in prodotto pop.",
 "storia": "Andamento anomalo e ben documentato. Il caricamento iniziale fa circa 500.000 visualizzazioni e poi si blocca. L'esplosione arriva mesi dopo, a maggio 2016, con picchi di 500-600.000 views al giorno. A luglio è vicino ai 30 milioni. Dal 24 giugno entra in rotazione radiofonica, diventa il tormentone dell'estate, arriva al numero 1 e ottiene il quintuplo disco di platino.",
 "significato": "«Andiamo a comandare» è entrata nel parlato come formula ironica di spavalderia auto-derisoria. Il caso è lo spartiacque: il momento in cui in Italia il meme smette di essere sottocultura e diventa direttamente industria discografica.",
 "chicca": "Rovazzi temeva che il pubblico radiofonico, privo del contesto visivo ironico, lo prendesse sul serio. E ha ammesso: «è successo tutto in modo scherzoso, non siamo partiti con l'intenzione di fare un disco di platino».",
 "dopo": "Ha consolidato la carriera con «Tutto molto interessante» (2016) e «Faccio quello che voglio» (2017), passando poi al cinema e alla conduzione.",
 "confidenza": "alta su date e numeri, media sull'identità del video-sorgente",
 "fonti": ["Rockit (intervista)", "Wikipedia EN", "Giornale di Sicilia"],
 "hook": "Un videomaker che non sapeva cantare ha preso una frase sgrammaticata detta da uno sconosciuto su un trattore e ci ha fatto cinque dischi di platino.",
 "hashtags": "#rovazzi #andiamoacomandare #memeteca #tormentoni #musicaitaliana",
},
{
 "num": "015", "giorno": "Venerdì", "slot": 2, "categoria": "INTERNET · anni 2000",
 "titolo": "BIMBOMINKIA",
 "occhiello": "L'insulto dei forum finito sullo Zingarelli e sulla Treccani",
 "anno": "2000s",
 "creatore": "Ignoto. Wikipedia IT attribuisce la coniazione a utenti del provider NGI frequentatori di community di gaming online, in particolare MMORPG come World of Warcraft. Non esiste un singolo autore documentato.",
 "prima_apparizione": "Coniazione nei primi anni 2000 su forum e community di gaming italiani. La prima attestazione documentata nell'italiano scritto è del 2007, secondo lo Zingarelli 2014.",
 "origini": "Neologismo nativo del web italiano dell'era forum. Crasi di «bimbo» + «minchia», con la sostituzione spregiativa del digramma «ch» con la «k» — sostituzione che è essa stessa una parodia della grafia usata dai soggetti descritti.",
 "storia": "Dai forum di gaming si propaga ai forum generalisti, poi a MSN Messenger, Netlog, Facebook e YouTube. Nella prima fase identifica gli adolescenti con errori grammaticali, anglicismi e abbigliamento ispirato all'estetica emo. Poi si estende a chiunque appaia infantile online. Nonciclopedia ne fa una delle sue voci-simbolo. La consacrazione è lessicografica: Zingarelli 2014 e vocabolario Treccani.",
 "significato": "Treccani lo definisce «giovane utente dei siti di relazione sociale» con scarsa competenza linguistica, limitata profondità culturale e scrittura enfatica fatta di grafie simboliche, abbreviazioni ed emoticon. Nell'uso attuale si è ormai sganciato dall'età anagrafica.",
 "chicca": "È uno dei pochissimi meme linguistici nati sui forum italiani ad avere un lemma sia sulla Treccani sia sullo Zingarelli. Meme molto più virali e più mediatici non ce l'hanno mai fatta.",
 "dopo": "Il termine è sopravvissuto alla morte dei forum ed è passato a Facebook, YouTube e TikTok.",
 "reperto": {"tipo": "lemma", "bollo": "Il lemma",
   "voce": "bimbominkia", "grammatica": "s. m. e f. (spreg.)",
   "definizione": "giovane utente dei siti di relazione sociale, di scarsa competenza linguistica.",
   "fonte": "Vocabolario Treccani, sezione Neologismi. Ricostruzione tipografica, non riproduzione."},
 "confidenza": "alta sull'attestazione, bassa sull'attribuzione a NGI",
 "fonti": ["Treccani – Neologismi", "Wikipedia IT", "Wikizionario"],
 "hook": "Nato per insultare i tredicenni che scrivevano con la k. Finito, vent'anni dopo, sul vocabolario Treccani. Xkè no.",
 "hashtags": "#bimbominkia #memeteca #internetitaliano #annizero #storiadeimeme",
},

# ───────────────────────────── SABATO ─────────────────────────────
{
 "num": "016", "giorno": "Sabato", "slot": 0, "categoria": "INTERNET · 2015",
 "titolo": "ER FAINA",
 "tag": "@damiano_er_faina",
 "occhiello": "«A regà, buongiorno» — il commento di pancia diventato format",
 "anno": "2015",
 "creatore": "Damiano Coccia, nato a Roma nel 1988. Si presenta come netturbino; Fanpage segnala che il dato potrebbe far parte del personaggio.",
 "prima_apparizione": "Il primo video YouTube è uno sfogo contro l'ex fidanzata — data non documentata. La popolarità di massa parte con la pagina Facebook, attiva dal 2015.",
 "origini": "Il soprannome «Er Faina» glielo diede un prete della parrocchia dove giocava a calcio, che lo considerava furbo e opportunista: si era fatto mettere in porta nella squadra più forte. Il format è nato da un video personale, non da un progetto editoriale.",
 "storia": "A novembre 2015 Vice Italia lo fotografa con oltre 400.000 fan. Il video simbolo dell'epoca fa 769.000 visualizzazioni e 17.000 condivisioni. Il salto editoriale arriva col libro «A regà bongiorno» (Mondadori Electa, novembre 2016). Quello televisivo nel 2019 con Temptation Island Vip: secondo Il Fatto fu Maria De Filippi a invitarlo dopo che i suoi commenti sul programma erano diventati popolarissimi.",
 "significato": "Il format è codificato: apre con «buongiorno regà», si accende una sigaretta e commenta l'attualità — i video durano il tempo di una sigaretta. Vice Italia lo classifica come esempio di «propaganda gentista»: intrattenimento che veicola con l'ironia messaggi populisti. Oggi «parlare come Er Faina» indica il commento di pancia in romanesco su qualsiasi tema.",
 "chicca": "Nel maggio 2020 il ministro Francesco Boccia sporse denuncia dopo un video in cui Er Faina lo derideva per un orologio costoso.",
 "dopo": "Ha superato il milione di follower complessivi, con oltre 850.000 su Instagram, spostando l'attività da Facebook a Instagram e YouTube.",
 "confidenza": "alta sui numeri, bassa sulla data del primo video",
 "fonti": ["Vice Italia (nov 2015)", "Il Fatto Quotidiano (19 ago 2020)", "Fanpage"],
 "hook": "La durata dei suoi video non è una scelta editoriale: è quanto dura una sigaretta. È il format più onesto della storia dei social italiani.",
 "hashtags": "#erfaina #damianococcia #memeteca #romanesco #memeitaliani",
},
{
 "num": "017", "giorno": "Sabato", "slot": 1, "categoria": "INTERNET · 2015",
 "titolo": "IL PACCO DA GIÙ",
 "occhiello": "Casa Surace, nonna Rosetta e il meme italiano che non prendeva in giro nessuno",
 "anno": "2015",
 "creatore": "Il collettivo Casa Surace, amici e coinquilini fra Napoli e Sala Consilina (Salerno). Volto-icona: nonna Rosetta, nata il 25 marzo 1933 a San Giorgio a Cremano — nonna reale di Beppe Polito, non un'attrice ingaggiata.",
 "prima_apparizione": "Il collettivo nasce nel 2015; i video circolano nativamente su Facebook e YouTube.",
 "origini": "Il materiale sorgente è la vita domestica meridionale reale — la casa, la cucina, i rapporti tra nonna e nipoti — filmata in modo volutamente casalingo. Il nucleo che diventa meme è la contrapposizione Nord/Sud vista dai fuorisede, e in particolare «il pacco da giù»: il pacco di cibo che le famiglie del Sud spediscono ai figli emigrati al Nord.",
 "storia": "Fenomeno virale nativo di Facebook, con un pubblico intergenerazionale. Il sito ufficiale dichiara oltre 4 milioni di follower e più di un miliardo di visualizzazioni. Il «pacco da giù» tracima nel linguaggio comune e poi nel mainstream: due libri per Sperling & Kupfer e, nel 2020, «Staisciupacco», un servizio che spedisce davvero pacchi agroalimentari del Sud. Il meme che si fa impresa.",
 "significato": "È il segno linguistico condiviso dell'esperienza del fuorisede meridionale: nostalgia, cura familiare a distanza, orgoglio del Sud. Uno dei rari casi di meme italiano di massa a base non satirica ma sentimentale.",
 "chicca": "I video di nonna Rosetta sono stati tradotti in più lingue e hanno avuto una circolazione autonoma in Cina, dove la figura della nonna del Sud Italia è diventata popolare.",
 "dopo": "Nonna Rosetta è morta il 18 novembre 2022, a 89 anni. Il cordoglio nazionale si è raccolto attorno a una frase diventata epitaffio collettivo: «E mo' chi lo manda il pacco da giù?».",
 "confidenza": "alta",
 "fonti": ["casasurace.com", "Editoriale Domani (nov 2022)", "Tgcom24"],
 "hook": "Quasi tutti i grandi meme italiani nascono per prendere in giro qualcuno. Questo no. Questo è nato da una nonna vera che spediva cibo ai nipoti.",
 "hashtags": "#casasurace #nonnarosetta #paccodagiu #memeteca #fuorisede",
},
{
 "num": "018", "giorno": "Sabato", "slot": 2, "categoria": "INTERNET · 2016",
 "titolo": "#CIAONE",
 "occhiello": "Un tweet di sette parole diventato neologismo Treccani",
 "anno": "2016",
 "creatore": "Il tweet che innesca il fenomeno è di Ernesto Carbone, allora deputato del Partito Democratico. La parola in sé è precedente e non ha un inventore documentato.",
 "prima_apparizione": "17 aprile 2016 su Twitter, la sera del referendum sulle trivelle.",
 "origini": "«Ciaone» è l'accrescitivo colloquiale di «ciao», usato come saluto sprezzante. Treccani ne segnala una popolarizzazione precedente nel film «Confusi e felici» (2014), in una battuta di Caterina Guzzanti. Il salto a meme politico avviene però online: al referendum non si raggiunge il quorum e Carbone twitta «Prima dicevano quorum. Poi 40. Poi 35. Ora per loro l'importante è partecipare #ciaone».",
 "storia": "Trending topic immediato e doppia ondata: il rilancio ironico dei sostenitori del governo Renzi e la reazione indignata di chi giudica il tono irridente verso gli elettori. ANSA, Sky TG24 e Il Fatto Quotidiano lo coprono come caso politico, non come curiosità linguistica. Treccani lo registra tra i neologismi del 2016.",
 "significato": "Liquidazione sarcastica di un avversario o di un fallimento altrui — l'equivalente italiano di un «bye» sprezzante. Nel lessico politico è rimasto come etichetta di un intero stile comunicativo.",
 "chicca": "È uno dei rari casi in cui un hashtag partito da un singolo tweet politico finisce codificato in un vocabolario ufficiale: Treccani lo registra come neologismo, con doppia funzione di interiezione e sostantivo maschile.",
 "dopo": "Carbone ha lasciato il PD nel 2019 per seguire Renzi in Italia Viva. La parola è sopravvissuta all'episodio ed è oggi lessico comune.",
 "reperto": {"tipo": "lemma", "bollo": "Il lemma",
   "voce": "ciaóne", "grammatica": "inter. e s. m.",
   "definizione": "forma di saluto che esprime ironia o scherno.",
   "fonte": "Treccani, neologismi 2016. Ricostruzione tipografica, non riproduzione."},
 "confidenza": "alta sul tweet e sulla codificazione Treccani",
 "fonti": ["Treccani – Neologismi", "ANSA (17 apr 2016)", "Sky TG24"],
 "hook": "Sette parole scritte da un deputato la sera di un referendum. Risultato: una parola nuova sul vocabolario e un'etichetta politica che dura da dieci anni.",
 "hashtags": "#ciaone #memeteca #internetitaliano #treccani #storiadeimeme",
},

# ─────────────────── DOMENICA · SPECIALE TV & PUBBLICITÀ ───────────────────
{
 "num": "019", "giorno": "Domenica", "slot": 0, "categoria": "TV & PUBBLICITÀ · 2017",
 "titolo": "L'ASTEROIDE DEL BUONDÌ",
 "tag": "@buondimotta",
 "occhiello": "«Possa colpirmi un asteroide se esiste»",
 "anno": "2017",
 "creatore": "Campagna ideata da Saatchi & Saatchi per Bauli/Motta; direttore creativo Alessandro Orlandi. Protagoniste: una bambina e sua madre.",
 "prima_apparizione": "28 agosto 2017, in TV e online. La bambina descrive una colazione «leggera ma invitante»; la madre risponde «Non esiste una colazione così, cara. Possa un asteroide colpirmi se esiste» — e viene istantaneamente centrata da un meteorite.",
 "origini": "Nasce come attacco deliberato agli stereotipi della pubblicità alimentare italiana, la famiglia perfetta in stile Mulino Bianco. I creativi hanno rivendicato l'intento, descrivendo l'operazione come «un asteroide sui cliché». Seguirono una seconda versione con il padre e, nel dicembre 2022, un capitolo con la fatina.",
 "storia": "È il caso italiano meglio misurato di pubblicità diventata meme. In una settimana la pagina Facebook del brand passa da 42.000 a 51.000 follower (+21%) e il video supera 1,4 milioni di visualizzazioni. L'analisi di sentiment rilevò il 59,2% di tono ironico su Twitter: il pubblico non discuteva il prodotto, produceva contenuti derivati. Circolò l'hashtag #mandaunasteroide, e Taffo intervenne con le sue risposte sarcastiche.",
 "significato": "Il meteorite Buondì è la metafora standard, sui social italiani, della punizione istantanea per chi dice una sciocchezza o sfida la sorte.",
 "chicca": "Nonostante la percezione di uno scandalo unanime, i dati dicono il contrario: su Facebook il sentiment positivo (44%) superava nettamente il negativo (30,8%). Ci furono comunque segnalazioni all'Antitrust e all'Istituto dell'Autodisciplina Pubblicitaria.",
 "dopo": "La strategia seriale è proseguita per anni, confermando che la polemica era il piano, non l'incidente.",
 "reperto": {"tipo": "citazione", "bollo": "La battuta",
   "testo": "«Non esiste una colazione così, cara. Possa un asteroide colpirmi se esiste.»",
   "fonte": "Spot Buondì Motta, 28 agosto 2017, Saatchi & Saatchi. Citazione a fini di critica e discussione (art. 70 L. 633/1941)."},
 "confidenza": "alta",
 "fonti": ["Inside Marketing", "Artribune (set 2017)", "Artribune (dic 2022)"],
 "hook": "Domenica è giorno di TV e pubblicità. Cominciamo dallo spot che ha ucciso una madre in prima serata per vendere le merendine — e ci è riuscito.",
 "hashtags": "#buondi #asteroide #memeteca #pubblicitaitaliana #spotcult",
},
{
 "num": "020", "giorno": "Domenica", "slot": 1, "categoria": "TV & PUBBLICITÀ · anni '80",
 "titolo": "CAPRA! CAPRA! CAPRA!",
 "tag": "@vittoriosgarbi",
 "occhiello": "L'insulto scelto per non farsi più querelare",
 "anno": "1989",
 "creatore": "Vittorio Sgarbi. Non è una battuta scritta: è un intercalare televisivo autoprodotto.",
 "prima_apparizione": "Non databile a un singolo episodio. L'origine è collocata a fine anni Ottanta, nel periodo in cui Sgarbi era ospite fisso del Maurizio Costanzo Show. Snodo documentato: il 23 marzo 1989 una docente stronca una sua poesia definendolo «un asino poetico»; la replica offensiva gli costa una multa da 60 milioni di lire.",
 "origini": "Retroscena dichiarato dallo stesso Sgarbi: dopo la valanga di querele per diffamazione, sostituì gli insulti volgari con «capra» perché non gli procurava cause legali. Lo ha spiegato in diretta a DiMartedì il 6 novembre 2019: «capra» non ha connotazione fortemente negativa, crea familiarità tra generazioni, e gli deriva da un ricordo d'infanzia — uno zio lo usava perché la capra è animale ignorante.",
 "storia": "Dalla TV generalista il tormentone è migrato integralmente online: compilation ufficiali su Mediaset Infinity, pagine di scoperta dedicate su TikTok, GIF su Tenor, remix e mashup su YouTube. Sgarbi stesso ha alimentato il fenomeno pubblicando fotografie con capre vere. La natura ritmica e ripetitiva lo rende materiale ideale per l'audio-meme.",
 "significato": "Si usa quasi sempre in chiave autoironica per bollare l'ignoranza altrui nelle discussioni online, ed è l'icona dello scontro televisivo urlato all'italiana.",
 "chicca": "Il record documentato è del 17 aprile 2019, a «Live – Non è la d'Urso»: «capra» pronunciato 24 volte consecutive.",
 "dopo": "Sgarbi ha dichiarato che sono i giovani a chiedergli espressamente di dirlo. La sopravvivenza del tormentone dipende ormai dal pubblico digitale, non da quello televisivo che l'ha generato.",
 "confidenza": "alta su origine e diffusione, media sulla prima volta assoluta",
 "fonti": ["QuiFinanza", "Secolo d'Italia (nov 2019)", "Mediaset Infinity"],
 "hook": "Non l'ha scelto perché suonava bene. L'ha scelto perché era l'unico insulto che non gli costava una causa. Il diritto civile italiano ha prodotto un tormentone.",
 "hashtags": "#sgarbi #capra #memeteca #tvitaliana #tormentoni",
},
{
 "num": "021", "giorno": "Domenica", "slot": 2, "categoria": "TV & PUBBLICITÀ · 1985",
 "titolo": "L'UOMO DEL MONTE HA DETTO SÌ",
 "tag": "@delmonteitalia",
 "occhiello": "Il verdetto insindacabile più citato d'Italia (che oggi usiamo al negativo)",
 "anno": "1985",
 "creatore": "Campagna internazionale Del Monte ideata da McCann Erickson. Protagonista: l'attore britannico Osmond Brian Jackson (Bolton, 1931 – 8 luglio 2022), scelto dopo che un attore americano aveva ottenuto test negativi con il pubblico.",
 "prima_apparizione": "La campagna internazionale parte nel 1985 e prosegue fino al 1991; lo slogan originale è «The man from Del Monte, he say yes!». In Italia i primi spot sono del 1986.",
 "origini": "Nasce come dispositivo di certificazione: un'autorità esterna che approva il prodotto. L'uomo in completo di lino chiaro e panama arriva in idrovolante nelle piantagioni e dà il suo verdetto. Del Monte cercava «un uomo bianco, dall'aspetto cosmopolita, sopra i 40 anni» di cui le consumatrici si fidassero.",
 "storia": "Circa 25 spot in 30-34 paesi; Jackson dovette pronunciare la frase in 29 lingue diverse, sotto contratto per cinque spot l'anno. In Italia la frase diventa proverbiale e sopravvive alla campagna: online circola soprattutto nella variante negativa «L'uomo del Monte ha detto no», formula di bocciatura secca.",
 "significato": "Sancisce ironicamente un'approvazione o, molto più spesso, un rifiuto definitivo da parte di un'autorità: capo, banca, arbitro, pubblica amministrazione. È la formula italiana del verdetto insindacabile.",
 "chicca": "Jackson si sentì incasellato dal ruolo, pur ammettendo che gli aveva rilanciato la carriera: lavorò poi per BMW, Gucci, MasterCard, Mercedes e Barclays. Prima di fare l'attore era stato fotografo nella Marina militare britannica.",
 "dopo": "La campagna è stata criticata a posteriori per il suo impianto coloniale: un'autorità europea che approva il lavoro di braccianti africani e ispanici.",
 "reperto": {"tipo": "citazione", "bollo": "Lo slogan",
   "testo": "«The man from Del Monte, he say yes!»",
   "fonte": "Campagna internazionale Del Monte, 1985-1991, McCann Erickson. Lo slogan originale, prima della traduzione italiana. Citazione a fini di critica (art. 70 L. 633/1941)."},
 "confidenza": "media-alta",
 "fonti": ["Wikipedia EN", "Il Messaggero (lug 2022)", "Tgcom24"],
 "hook": "Lo slogan diceva sì. L'Italia lo usa da quarant'anni per dire no. È forse l'unico caso in cui un Paese intero ha invertito il senso di una pubblicità.",
 "hashtags": "#uomodelmonte #delmonte #memeteca #pubblicitaitaliana #anni80",
},

    # ─────────────────────────────────────────────────────── scheda 022
    {"num": "022", "giorno": "Lunedì", "slot": 1, "categoria": "INTERNET · 2012",
     "titolo": "LERCIO",
     "occhiello": "«Lo sporco che fa notizia»: la parodia del giornalismo "
                  "diventata test di realtà",
     "anno": "2012",
     "tag": "@lercio.it",
     "creatore": "Collettivo nato su idea di Michele Incollu dal gruppo della "
                 "pagina Facebook «Acido Lattico», a sua volta erede della "
                 "comunità del blog «La Palestra» di Daniele Luttazzi. Una "
                 "ventina di autori sparsi per l'Italia, quasi tutti con un "
                 "altro mestiere.",
     "prima_apparizione": "Ottobre 2012, come pagina che imita la grafica del "
                          "quotidiano gratuito Leggo: dal nome storpiato nasce "
                          "«Lercio».",
     "origini": "Parodia del giornalismo sensazionalista: titoli costruiti con "
                "gli stessi cliché e la stessa impostazione forzata dei "
                "giornali veri, applicati a notizie inventate. Tre notizie "
                "inedite al giorno — un articolo lungo e due breaking news — "
                "scelte in riunione e riviste più volte prima di uscire.",
     "storia": "Il salto è del gennaio 2013: «Errore nel sistema operativo: "
               "Radio Maria trasmette i Megadeth» viene ripresa come vera da "
               "Repubblica XL. Da lì il meccanismo si ripete: l'ex ministra "
               "Kyenge ricevette insulti per una proposta mai esistita. Nel "
               "2018 la «grammatica lercia» finisce in un articolo "
               "accademico peer-reviewed. Oggi: 1,5 milioni di follower su "
               "Facebook, un milione su Instagram.",
     "significato": "«Sembra un titolo di Lercio» è entrato nel linguaggio "
                    "comune come test di realtà: si dice di una notizia vera "
                    "così assurda da sembrare inventata. La satira che "
                    "funziona da unità di misura del giornalismo.",
     "chicca": "La redazione è la stessa dell'ottobre 2012: nessun nuovo "
               "ingresso in più di dieci anni, per non diluire lo stile. "
               "Le età vanno dai 27 ai 50 anni.",
     "dopo": "Una ventina di autori continua a scriverlo come secondo lavoro, "
             "o meglio come hobby: nessuno vive di Lercio, e il tono è "
             "rimasto quello del primo giorno.",
     "reperto": {"tipo": "citazione", "bollo": "Il titolo",
                 "testo": "«Errore nel sistema operativo: Radio Maria "
                          "trasmette i Megadeth»",
                 "fonte": "Lercio, gennaio 2013 — ripreso come vero da "
                          "Repubblica XL"},
     "confidenza": "alta",
     "fonti": ["Il Post (14 ott 2021)", "Treccani, Lingua italiana"],
     "hook": "Nel 2013 un giornale vero ha ripreso come vera la notizia che "
             "Radio Maria trasmetteva i Megadeth. L'aveva inventata una "
             "redazione che di mestiere fa altro.",
     "hashtags": "#lercio #satira #memeteca #giornalismo #internetitaliano"},

    # ─────────────────────────────────────────────────────── scheda 023
    {"num": "023", "giorno": "Lunedì", "slot": 2, "categoria": "INTERNET · 2006",
     "titolo": "SPINOZA",
     "tag": "@spinozait",
     "occhiello": "La battuta con la firma: il forum che ha trasformato i "
                  "commenti in una redazione",
     "anno": "2006",
     "creatore": "Alessandro Bonino apre il blog a metà anni Duemila; con "
                 "Stefano Andreoli diventa il progetto collettivo che "
                 "conosciamo. Le battute arrivano dal «Laboratorio permanente "
                 "di satira» del forum, aperto a chiunque.",
     "prima_apparizione": "Il blog nasce tra il 2005 e il 2006 — le fonti "
                          "discordano sull'anno. Il boom arriva nella "
                          "primavera 2008, con le elezioni politiche.",
     "origini": "Bonino: «Quando i commentatori hanno cominciato a inondare "
                "il sito di battute papabili di pubblicazione abbiamo "
                "lanciato il forum». Dal marzo 2009 le battute si propongono "
                "lì, migliaia di utenti; le migliori vengono selezionate, "
                "assemblate e pubblicate una a una, ciascuna con il nome "
                "dell'autore.",
     "storia": "Miglior blog italiano ai Macchianera Awards nel 2009 e nel "
               "2010, Premio Satira di Forte dei Marmi nel 2010. L'8 novembre "
               "2010 Roberto Benigni lo omaggia in diretta a «Vieni via con "
               "me». Seguono cinque libri tra il 2010 e il 2014, prima con "
               "Aliberti e poi con Rizzoli.",
     "significato": "La battuta secca sull'attualità, firmata: ogni riga è di "
                    "qualcuno, non del marchio. È il formato che ha "
                    "anticipato la satira social italiana, quando ancora si "
                    "chiamava «lasciare un commento».",
     "chicca": "Il riconoscimento più alto non fu un premio: fu Benigni che "
               "in prima serata, su Rai 3, lesse le battute del sito davanti "
               "a milioni di spettatori.",
     "dopo": "Il forum resta il vivaio: prima si è autori lì, poi in prima "
             "pagina. Il meccanismo — proposta aperta, selezione, firma — "
             "non è mai cambiato.",
     "reperto": {"tipo": "citazione", "bollo": "Il metodo",
                 "testo": "«Quando i commentatori hanno cominciato a inondare "
                          "il sito di battute papabili di pubblicazione "
                          "abbiamo lanciato il forum»",
                 "fonte": "Alessandro Bonino, intervista ad Apogeonline"},
     "confidenza": "media-alta: le fonti discordano sull'anno di nascita "
                   "(2005 per Apogeonline, 2006 per Wikipedia)",
     "fonti": ["Wikipedia IT, Spinoza (blog)", "Apogeonline, intervista a Bonino"],
     "hook": "Prima dei social c'era un forum dove migliaia di sconosciuti "
             "proponevano battute sull'attualità. Le migliori finivano in "
             "prima pagina, con nome e cognome.",
     "hashtags": "#spinoza #satira #memeteca #blogitaliani #internetitaliano"},
    # ─────────────────────────────────────────────────────── scheda 024
    {"num": "024", "giorno": "Martedì", "slot": 1, "categoria": "POLITICA · 2014",
     "titolo": "ENRICO STAI SERENO",
     "occhiello": "La rassicurazione che da dieci anni significa il suo "
                  "contrario",
     "anno": "2014",
     "creatore": "Matteo Renzi, allora segretario del PD. Il destinatario era "
                 "Enrico Letta, presidente del Consiglio del suo stesso "
                 "partito.",
     "prima_apparizione": "Gennaio 2014: Renzi la pronuncia in televisione, "
                          "ospite di Daria Bignardi. Poche settimane dopo, a "
                          "metà febbraio, Letta sale al Quirinale a rassegnare "
                          "le dimissioni e Renzi prende il suo posto.",
     "origini": "I due erano legati da un patto di reciproco sostegno che la "
                "stampa battezzò «patto della schiacciatina», dal cibo con cui "
                "fu suggellato. La rassicurazione pubblica arrivò mentre il "
                "sostegno interno a Letta si stava già sgretolando: è questo "
                "scarto tra la frase e i fatti ad averla resa memorabile.",
     "storia": "Il passaggio di consegne del febbraio 2014 fu raccontato come "
               "uno dei più gelidi della storia repubblicana, e «stai sereno» "
               "diventò da subito sinonimo di sgambetto in arrivo. Nel libro "
               "«Avanti» (2017) Renzi provò a riprendersi la frase: «L'idea "
               "che Stai sereno sia una fregatura mi ferisce… Semplicemente "
               "perché non è vero». Non funzionò: l'uso ironico era ormai "
               "irreversibile.",
     "significato": "Dire «stai sereno» a un italiano, oggi, è annunciargli "
                    "che sta per succedergli qualcosa. È il caso più pulito "
                    "di antifrasi istituzionalizzata: una parola che "
                    "l'esperienza collettiva ha capovolto in modo permanente.",
     "chicca": "Il «patto della schiacciatina»: l'accordo di reciproco "
               "sostegno tra Renzi e Letta prese il nome dalla focaccia "
               "toscana con cui i due lo avevano suggellato.",
     "dopo": "Nel 2022, di nuovo l'uno contro l'altro sulle alleanze "
             "elettorali, i giornali raccontarono la lite ripartendo da lì: "
             "otto anni dopo, «stai sereno» era ancora il titolo. Certe "
             "frasi non si dimettono.",
     "reperto": {"tipo": "citazione", "bollo": "La frase",
                 "testo": "«Enrico stai sereno»",
                 "fonte": "Matteo Renzi, gennaio 2014, in tv da Daria "
                          "Bignardi"},
     "confidenza": "media-alta: il contesto e le conseguenze sono documentati, "
                   "la data esatta della battuta no",
     "fonti": ["Il Messaggero (2022)", "Affaritaliani (dal libro «Avanti»)",
               "il Giornale"],
     "hook": "«Stai sereno», gli disse in tv. Un mese dopo quello non era più "
             "presidente del Consiglio. Da allora la frase significa l'esatto "
             "contrario di quello che dice.",
     "hashtags": "#staisereno #renzi #memeteca #politicaitaliana #memeitaliani"},
    # ─────────────────────────────────────────────────────── scheda 025
    {"num": "025", "giorno": "Lunedì", "slot": 3, "categoria": "CINEMA · 1978",
     "titolo": "MI SI NOTA DI PIÙ",
     "occhiello": "La domanda che l'Italia si fa da mezzo secolo prima di "
                  "ogni invito",
     "anno": "1978",
     "creatore": "Nanni Moretti, che in «Ecce bombo» scrive, dirige e "
                 "interpreta Michele Apicella, il nevrotico più citato del "
                 "cinema italiano.",
     "prima_apparizione": "«Ecce bombo», 1978. La scena è una telefonata: "
                          "Michele, indeciso se presentarsi a un invito, "
                          "chiede consiglio su come farsi notare di più.",
     "origini": "La battuta esatta è: «Mi si nota di più se vengo e me ne sto "
                "in disparte o se non vengo per niente?». Non è una domanda "
                "sull'andare o meno: è una domanda su come essere guardati, "
                "ed è per questo che non invecchia. Il narcisismo travestito "
                "da timidezza, in diciassette parole.",
     "storia": "È il caso più lungo di battuta migrata dal cinema alla "
               "politica: Fini la usa in un dibattito a Bologna nel 2010, "
               "Veltroni su Berlusconi nel 2013, Gasparri nel 2016, Carfagna "
               "nel 2018, e nel luglio 2020 il presidente del Consiglio "
               "Conte la cita sulle tensioni del centrodestra — "
               "quarantadue anni dopo il film.",
     "significato": "Serve a deridere chi minaccia di non presentarsi "
                    "sperando che la sua assenza pesi: in politica è "
                    "l'accusa standard a chi diserta un voto o un vertice. "
                    "Nel parlato comune copre ogni dilemma di presenza, "
                    "dalla riunione al gruppo WhatsApp.",
     "chicca": "Dallo stesso film viene l'altro tormentone immortale, "
               "«faccio cose, vedo gente»: Romano Prodi lo citò già nel "
               "maggio 1996. Un solo film, due formule permanenti "
               "dell'italiano.",
     "dopo": "La scena vive una seconda vita come GIF e reaction: la faccia "
             "di Moretti al telefono è diventata la risposta standard a "
             "qualunque invito ricevuto con ambivalenza.",
     "reperto": {"tipo": "citazione", "bollo": "La battuta",
                 "testo": "«Mi si nota di più se vengo e me ne sto in "
                          "disparte o se non vengo per niente?»",
                 "fonte": "Michele Apicella in «Ecce bombo» (Nanni Moretti, "
                          "1978)"},
     "confidenza": "alta",
     "fonti": ["Sky TG24 (8 lug 2020)", "Movieplayer"],
     "hook": "Nel 1978 un uomo al telefono chiese se si notava di più "
             "andando a una festa e restando in disparte, o non andando "
             "affatto. L'Italia non ha ancora smesso di chiederselo.",
     "hashtags": "#eccebombo #nannimoretti #memeteca #cinemaitaliano "
                 "#misinotadipiu"},
    # ─────────────────────────────────────────────────────── scheda 026
    {"num": "026", "giorno": "Lunedì", "slot": 4, "categoria": "INTERNET · 2025",
     "titolo": "ITALIAN BRAINROT",
     "occhiello": "Il fenomeno «italiano» del 2025: fatto altrove, in un "
                  "italiano che non esiste",
     "anno": "2025",
     "creatore": "Il capostipite «Tralalero Tralala» esce a inizio gennaio "
                 "2025 dall'account TikTok @eZburger401, poi bandito dalla "
                 "piattaforma: il padre del più grande fenomeno «italiano» "
                 "dell'anno non ha un nome. L'attribuzione esatta resta "
                 "contesa.",
     "prima_apparizione": "Gennaio 2025, TikTok: uno squalo con tre scarpe "
                          "Nike e una voce italiana sintetica. Il primo "
                          "repost documentato è dell'8 gennaio; quello del 13 "
                          "gennaio supera i 17 milioni di riproduzioni in tre "
                          "mesi.",
     "origini": "Il formato: immagini generate dall'AI di animali fusi con "
                "oggetti, narrate da una voce sintetica maschile che declama "
                "filastrocche sgrammaticate in un finto italiano. «Brain "
                "rot» era stata la parola dell'anno Oxford del 2024: il "
                "filone italiano ne è diventato il caso di scuola.",
     "storia": "In poche settimane nasce un universo: Bombardiro Crocodilo "
               "(metà febbraio), Brr Brr Patapim (fine marzo), la variante "
               "indonesiana Tung Tung Tung Sahur. Seguono versioni "
               "balcaniche e tedesche con la stessa struttura. I marketer "
               "paragonano la coerenza dell'universo a un franchise, e "
               "marchi come Ryanair e Loewe ne adottano l'estetica nelle "
               "campagne.",
     "significato": "È il primo meme «italiano» fatto da non italiani, in un "
                    "italiano che non esiste: l'italianità ridotta a suono. "
                    "E contiene il paradosso che riguarda questa pagina: la "
                    "voce Wikipedia sul fenomeno cita New York Times, "
                    "Guardian e Daily Dot. Nessuna fonte italiana.",
     "chicca": "L'account che ha inventato tutto è stato bandito da TikTok: "
               "il fenomeno da miliardi di visualizzazioni è ufficialmente "
               "orfano.",
     "dopo": "Il formato si è fatto industria — giochi, gadget, pubblicità — "
             "mentre in Italia il dibattito resta diviso tra chi lo "
             "considera il degrado definitivo e chi la prima avanguardia "
             "interamente algoritmica.",
     "reperto": {"tipo": "citazione", "bollo": "Il capostipite",
                 "testo": "«Tralalero Tralala» — uno squalo con tre scarpe "
                          "Nike e una voce italiana finta",
                 "fonte": "TikTok, gennaio 2025"},
     "confidenza": "media-alta: la genesi esatta è contesa, le date dei "
                   "repost sono documentate",
     "fonti": ["Know Your Meme", "La Scimmia Pensa (25 apr 2025)",
               "Wikipedia EN"],
     "hook": "Il più grande fenomeno italiano del 2025 non è stato fatto da "
             "italiani e non parla italiano vero. Il mondo lo chiama "
             "comunque italian brainrot.",
     "hashtags": "#italianbrainrot #tralalerotralala #memeteca "
                 "#bombardirocrocodilo #internetitaliano"},
    # ─────────────────────────────────────────────────────── scheda 027
    {"num": "027", "giorno": "Lunedì", "slot": 5, "categoria": "TV · 1990",
     "titolo": "IL GABIBBO",
     "tag": "@striscialanotizia",
     "occhiello": "Il pupazzo rosso che l'America ha inseguito per quindici "
                  "anni in tribunale",
     "anno": "1990",
     "creatore": "Antonio Ricci, per Striscia la notizia. La voce è di "
                 "Lorenzo Beccati, autore televisivo genovese; dentro il "
                 "costume c'era il mimo Gero Caldarelli.",
     "prima_apparizione": "1° ottobre 1990, a Striscia la notizia.",
     "origini": "Il nome viene dal genovese «gabibbu»: in origine gli "
                "scaricatori del porto di Massaua, in Eritrea, poi epiteto "
                "ironico-dispregiativo per i non liguri. Ricci prende la "
                "parola e la capovolge: il «gabibbo» diventa la maschera "
                "rossa più riconoscibile della TV italiana.",
     "storia": "Nel 2002 la Western Kentucky University accusa Mediaset di "
               "aver copiato la sua mascotte Big Red e chiede 250 milioni "
               "di dollari. Seguono quindici anni di processi: il tribunale "
               "di Ravenna respinge nel 2007, la Corte d'appello di Bologna "
               "conferma nel 2011, la Cassazione chiude nel 2017: il "
               "Gabibbo non è un plagio. Il paradosso: nel 1991 Ricci "
               "stesso, a Novella 2000, aveva detto ironicamente di essersi "
               "ispirato proprio a Big Red.",
     "significato": "È l'inviato-pupazzo che dà del tu al potere: la "
                    "denuncia travestita da carnevale, formula unica della "
                    "TV italiana. E il suo lessico genovese — «besugo», "
                    "rivolto a chi non capisce — è entrato nel vocabolario "
                    "nazionale degli insulti affettuosi.",
     "chicca": "Caldarelli era alto un metro e cinquantatré; il costume un "
               "metro e sessantacinque. Il Gabibbo ha sempre guardato il "
               "mondo attraverso la propria bocca.",
     "dopo": "Trentacinque anni dopo è ancora in onda, sopravvissuto a ogni "
             "conduttore e a ogni causa: nessun personaggio televisivo "
             "italiano ha avuto una carriera così lunga senza mai mostrare "
             "il volto.",
     "reperto": {"tipo": "citazione", "bollo": "La confessione",
                 "testo": "«Il Gabibbo è il figlio illegittimo dell'omino "
                          "Michelin»",
                 "fonte": "Antonio Ricci, Novella 2000, 1991"},
     "confidenza": "alta sulla vicenda giudiziaria, media sulla data esatta "
                   "del debutto",
     "fonti": ["Vice Italia", "L'Angolo di Phil"],
     "hook": "Un'università americana ha chiesto 250 milioni di dollari a un "
             "pupazzo rosso genovese. Ci sono voluti quindici anni di "
             "processi per decidere chi aveva inventato cosa.",
     "hashtags": "#gabibbo #striscialanotizia #memeteca #tvitaliana #anni90"},
    # ─────────────────────────────────────────────────────── scheda 028
    {"num": "028", "giorno": "Lunedì", "slot": 6,
     "categoria": "TV & PUBBLICITÀ · 1957",
     "titolo": "CAROSELLO",
     "occhiello": "La preistoria di tutti i tormentoni italiani: "
                  "settemiladuecento scenette e una nazione a letto dopo",
     "anno": "1957",
     "creatore": "La RAI, che ammette la pubblicità in televisione solo "
                 "travestita da spettacolo. Tra i registi delle scenette: "
                 "Federico Fellini, Sergio Leone, Pupi Avati.",
     "prima_apparizione": "3 febbraio 1957, ogni sera dalle 20:50 alle 21:00.",
     "origini": "La regola del formato: prima la scenetta — comica, musicale, "
                "animata — e il prodotto solo in coda. Da quel vincolo "
                "nascono personaggi piu' longevi delle campagne: Calimero "
                "per il detersivo Ava, Carmencita e il Caballero per il "
                "caffe' Paulista, Ernesto Calindri per il Cynar, Nino "
                "Manfredi per Lavazza.",
     "storia": "Vent'anni di onda quotidiana, oltre 7.200 episodi. Chiude il "
               "1° gennaio 1977, accusato di essere «diseducativo». "
               "Nessun programma italiano ha mai piu' generato cosi' tanto "
               "lessico condiviso per abitante.",
     "significato": "E' la fucina originaria del tormentone italiano: mezzo "
                    "vocabolario pubblicitario nazionale nasce li'. E «a "
                    "letto dopo Carosello» resta l'orologio dell'infanzia di "
                    "tre generazioni: il programma come unita' di misura del "
                    "tempo.",
     "chicca": "Andava in onda tutti i giorni dell'anno tranne due: il "
               "Venerdi' Santo e il 2 novembre, il giorno dei morti.",
     "dopo": "I personaggi sono sopravvissuti al programma — Calimero e' "
             "ancora in circolazione — e il formato scenetta-piu'-prodotto "
             "e' l'antenato diretto di quello che oggi chiamiamo branded "
             "content.",
     "reperto": {"tipo": "citazione", "bollo": "La formula",
                 "testo": "«A letto dopo Carosello»",
                 "fonte": "La formula serale delle famiglie italiane, "
                          "1957-1977"},
     "confidenza": "alta",
     "fonti": ["Quotidiano.net", "Il Sole 24 Ore (3 gen 2014)"],
     "hook": "Per vent'anni l'Italia ha avuto un solo orologio serale: dieci "
             "minuti di scenette, poi i bambini a letto. Era pubblicita'. "
             "E' diventata memoria collettiva.",
     "hashtags": "#carosello #memeteca #pubblicitaitaliana #tvitaliana "
                 "#storiadellatv"},
    # ─────────────────────────────────────────────────────── scheda 029
    {"num": "029", "giorno": "Martedì", "slot": 1, "categoria": "TV · 1991",
     "titolo": "NON È LA RAI",
     "occhiello": "Il pomeriggio che l'Italia non ha mai smesso di "
                  "canticchiare",
     "anno": "1991",
     "creatore": "Gianni Boncompagni, con Irene Ghergo. Regia e scenografie "
                 "dello stesso Boncompagni.",
     "prima_apparizione": "9 settembre 1991, dallo Studio 1 del Centro "
                          "Palatino di Roma, sulle reti Fininvest: prima "
                          "Canale 5, poi Italia 1. Ultima puntata il 30 "
                          "giugno 1995.",
     "origini": "Decine di adolescenti, giochi, canzoni e balletti nel primo "
                "pomeriggio. Alla conduzione si alternano Enrica Bonaccorti "
                "e Paolo Bonolis, poi dalla terza stagione Ambra Angiolini: "
                "sedici anni, guidata in diretta da Boncompagni attraverso "
                "un auricolare.",
     "storia": "Tre milioni di spettatori al giorno all'uscita da scuola. "
               "Lancia Claudia Gerini, Sabrina Impacciatore, Antonella "
               "Elia e una generazione di volti televisivi; associazioni di "
               "genitori e Telefono Azzurro lo accusano di sessualizzare le "
               "protagoniste. Chiude il 30 giugno 1995, al culmine del "
               "successo.",
     "significato": "L'auricolare di Ambra è diventato la metafora italiana "
                    "definitiva del parlare con parole d'altri: «chi ti "
                    "parla nell'auricolare?» si dice ancora a chi recita un "
                    "copione altrui. E il programma è il culto rétro per "
                    "eccellenza della TV italiana.",
     "chicca": "«T'appartengo», il disco d'esordio di Ambra, vendette "
               "370.000 copie con tre dischi di platino. E quando nel 2020 "
               "Mediaset Extra rimise le repliche in onda di notte, "
               "diventarono un rito collettivo.",
     "dopo": "La sigla e i balletti vivono una terza vita su TikTok, "
             "tramandati da chi non era nato: il caso più pulito di "
             "tormentone transgenerazionale della TV italiana.",
     "reperto": {"tipo": "citazione", "bollo": "L'auricolare",
                 "testo": "«Le suggerivo battute terribili, irriferibili, e "
                          "lei doveva fingere che niente accadesse»",
                 "fonte": "Gianni Boncompagni su Ambra Angiolini"},
     "confidenza": "alta",
     "fonti": ["ANSA (5 lug 2025)", "nss G-Club"],
     "hook": "Una sedicenne conduceva davanti a tre milioni di spettatori "
             "mentre un uomo le dettava ogni parola nell'orecchio. L'Italia "
             "ci ha messo trent'anni a decidere cosa pensarne.",
     "hashtags": "#nonelarai #ambra #memeteca #tvitaliana #anni90"},
    # ─────────────────────────────────────────────────────── scheda 030
    {"num": "030", "giorno": "Martedì", "slot": 2,
     "categoria": "TV & PUBBLICITÀ · 1966",
     "titolo": "IL LOGORIO DELLA VITA MODERNA",
     "occhiello": "Un tavolino in mezzo al traffico, e la parola che da "
                  "sessant'anni descrive lo stress italiano",
     "anno": "1966",
     "creatore": "La campagna Cynar con Ernesto Calindri (1909-1999): "
                 "attore di teatro e di cinema dal 1935, il commissario "
                 "Malvasia di «Totòtruffa 62».",
     "prima_apparizione": "1966, a Carosello. La campagna andrà avanti fino "
                          "al 1984: quasi vent'anni con la stessa scena.",
     "origini": "L'immagine è una sola, ripetuta fino a diventare icona: un "
                "tavolino apparecchiato al centro di una strada trafficata, "
                "Calindri in doppiopetto che legge il giornale e sorseggia "
                "l'amaro al carciofo, imperturbabile. Poi lo slogan: "
                "«contro il logorìo della vita moderna».",
     "storia": "La campagna marchia Calindri a vita: nella memoria pubblica "
               "cancella una carriera di prima fila, cominciata nel 1935 e "
               "passata anche per «I bambini ci guardano» di De Sica nel "
               "1943. Il testimonial divora l'attore.",
     "significato": "«Logorio della vita moderna» è entrato nel lessico come "
                    "definizione ironica dello stress prima ancora che "
                    "«stress» diventasse parola comune. E il tavolino nel "
                    "traffico resta la vignetta archetipa della calma "
                    "nell'assedio: l'antenato italiano di ogni meme sulla "
                    "serenità apparente nel disastro.",
     "chicca": "L'uomo che per vent'anni ha impersonato la calma contro il "
               "traffico aveva debuttato al cinema trent'anni prima dello "
               "spot: il volto pubblicitario più longevo d'Italia era un "
               "attore vero prestato al carciofo.",
     "dopo": "Lo slogan è sopravvissuto alla campagna e quasi al prodotto: "
             "si cita ancora oggi, spesso senza sapere da dove venga — il "
             "destino dei tormentoni perfetti.",
     "reperto": {"tipo": "citazione", "bollo": "Lo slogan",
                 "testo": "«Contro il logorìo della vita moderna»",
                 "fonte": "Campagna Cynar con Ernesto Calindri, 1966-1984"},
     "confidenza": "alta",
     "fonti": ["Il Post", "70-80.it"],
     "hook": "Un signore in doppiopetto beveva l'amaro a un tavolino "
             "apparecchiato in mezzo al traffico. Sessant'anni dopo è "
             "ancora il modo italiano di dire «calma, nonostante tutto».",
     "hashtags": "#cynar #carosello #memeteca #pubblicitaitaliana "
                 "#vitamoderna"},
    # ─────────────────────────────────────────────────────── scheda 031
    {"num": "031", "giorno": "Martedì", "slot": 3,
     "categoria": "INTERNET & POLITICA · 2022",
     "titolo": "IL PARTITO CAPIBARA",
     "occhiello": "Il meme che ha smesso di essere un meme e ha cominciato a "
                  "raccogliere firme",
     "anno": "2022",
     "creatore": "L'animatore più visibile è Davide Dibitonto, in rete "
                 "xenodibi. Il partito però l'etichetta la rifiuta: si "
                 "definisce «uno strumento politico open source», «né capi, "
                 "né fondatori».",
     "tag": "@partito.capibara",
     "prima_apparizione": "Dal 6 settembre all'8 ottobre 2022, nelle storie "
                          "di Instagram: le «Elezioni Iperstizionali», un "
                          "torneo fra otto liste immaginarie votato con "
                          "le reaction. Vinse il Partito "
                          "Xenocomunista dei Post-Lavoratori.",
     "origini": "Nel 2021 i capibara scesero in massa nei giardini di "
                "Nordelta, quartiere di lusso recintato alle porte di Buenos "
                "Aires, tirato su nel 1999 sulla palude dove vivevano da "
                "sempre. I residenti chiesero di rimuoverli; internet si "
                "schierò col roditore: enorme, placido, seduto dove non "
                "dovrebbe.",
     "storia": "Finita la finta campagna, la battuta non si è sgonfiata: "
               "si è organizzata. Dai gruppi meme ai collettivi in carne e "
               "ossa in cinque città, fino al raduno di Padova del 24 giugno "
               "2026. Oggi l'account ha quasi sedicimila follower e il "
               "partito dichiara diecimila firme.",
     "significato": "È il caso italiano più limpido di «iperstizione»: una "
                    "finzione che, diffondendosi abbastanza, si costruisce "
                    "da sola le condizioni per diventare vera. Il "
                    "riferimento teorico è Mark Fisher, che i loro "
                    "manifesti ribaltano di continuo. E il capibara rende "
                    "simpatica una richiesta che a parole suonerebbe "
                    "estremista.",
     "chicca": "La patrimoniale che propongono è del 100% oltre i 6.660.000 "
               "euro: il tetto alla ricchezza scritto col numero della "
               "bestia.",
     "dopo": "La raccolta firme è partita davvero. Per presentare le liste "
             "ne servono circa 112.500: il salto dalla reaction al "
             "modulo col timbro è la parte non ancora fatta.",
     "reperto": {"tipo": "citazione", "bollo": "Il manifesto",
                 "testo": "«È più facile immaginare la remigrazione che il "
                          "week-end lungo»",
                 "fonte": "Partito Capibara, 2026 — da Mark Fisher"},
     "confidenza": "alta",
     "fonti": ["Pagella Politica (6 lug 2026)", "Open (11 giu 2026)",
               "Adnkronos"],
     "hook": "Nel 2022 otto partiti inesistenti si sono sfidati nei "
             "sondaggi delle storie di Instagram. Quattro anni dopo il "
             "vincitore ha un simbolo, dei collettivi e diecimila firme.",
     "hashtags": "#partitocapibara #capibara #memeteca #memeitaliani "
                 "#politicaitaliana"},
]


LIMITE_INSTAGRAM = 2200
MARGINE = 20   # Instagram conta in unità UTF-16: ogni emoji fuori dal BMP vale 2


def lunghezza_instagram(testo):
    """Conta come conta Instagram, non come conta Python."""
    return sum(2 if ord(c) > 0xFFFF else 1 for c in testo)


# ─────────────────────────────────────────────────────────────────────── tag
# Il campo facoltativo "tag" mette la menzione dell'AUTORE nella caption, sotto
# il blocco CREATORE. Tre regole, tutte imparate a caro prezzo:
#
#   1. Si tagga l'autore, mai il bersaglio. La 005 racconta un remix nato per
#      sfottere Meloni: taggarla non sarebbe attribuzione, sarebbe provocazione.
#      Un archivio perde autorevolezza nel momento in cui sembra cercare la rissa.
#   2. L'account va VERIFICATO aprendolo, non dedotto dal nome. Cercando quello
#      di Palmaroli abbiamo trovato "osho_lepiubellefrasi": privato, 10 follower,
#      un omonimo. Taggarlo sarebbe stata una misattribuzione su una pagina che
#      vende accuratezza.
#   3. Se l'account non esiste o non e' verificabile, il campo resta vuoto e non
#      succede niente. Meglio nessun tag che un tag sbagliato.
#
# Menzione in caption, non tag sulla foto: notifica lo stesso, e Instagram
# guarda con meno sospetto le menzioni testuali rispetto alle etichette
# sistematiche sulle immagini.
def _riga_tag(m):
    """La riga del tag sotto CREATORE.

    Regola di Luigi, 25 agosto 2026: in ogni post si tagga. Se l'account
    ufficiale non esiste si tagga la pagina non ufficiale attiva piu' seguita.
    In quel caso pero' NON si scrive «Su Instagram», che affermerebbe il
    falso: si dice che e' la pagina piu' seguita sul tema. Un archivio che
    vive di verifiche non puo' spacciare una fan page per l'originale — e
    soprattutto non si tagga mai un account che finge di ESSERE il soggetto.
    """
    if not m.get("tag"):
        return ""
    if m.get("tag_ufficiale") is False:
        return f"\nLa pagina piu' seguita sul tema: {m['tag']}"
    return f"\nSu Instagram: {m['tag']}"


def costruisci_caption(m):
    """Compone la caption Instagram (limite 2.200 caratteri)."""
    fonti = " · ".join(m["fonti"])
    return (
        f"{m['titolo']} — {m['hook']}\n\n"
        f"📅 PRIMA APPARIZIONE\n{m['prima_apparizione']}\n\n"
        f"👤 CREATORE\n{m['creatore']}"
        + _riga_tag(m)
        + "\n\n"
        f"🧬 ORIGINI\n{m['origini']}\n\n"
        f"📈 COME È DIVENTATO MEME\n{m['storia']}\n\n"
        f"💡 COSA SIGNIFICA\n{m['significato']}\n\n"
        f"🔎 LA CHICCA\n{m['chicca']}\n\n"
        f"⏭ COS'È SUCCESSO DOPO\n{m['dopo']}\n\n"
        f"Mandala a chi se la ricorda.\n\n"
        f"— Scheda n. {m['num']} · Fonti: {fonti}\n"
        f"Segui {BRAND['handle']}\n\n"
        f"{m['hashtags']}"
    )


def coda(esclusi=()):
    """Ordine di pubblicazione: la domenica è monografica (TV e pubblicità),
    gli altri giorni pescano dal resto. Ritorna la lista dei numeri scheda."""
    import datetime as _dt

    esclusi = set(esclusi)
    tv = [m["num"] for m in MEMI
          if m["categoria"].startswith("TV") and m["num"] not in esclusi]
    resto = [m["num"] for m in MEMI
             if not m["categoria"].startswith("TV") and m["num"] not in esclusi]
    giorno = _dt.date.fromisoformat(INIZIO)
    ordine = []
    while tv or resto:
        pesca = tv if giorno.weekday() == 6 and tv else resto
        if not pesca:                      # domenica senza schede TV rimaste
            pesca = resto or tv
        for _ in range(SCHEDE_AL_GIORNO):
            if pesca:
                ordine.append(pesca.pop(0))
        giorno += _dt.timedelta(days=1)
    return ordine


def calendario(esclusi=(), inizio=None):
    """Ritorna [(data, ora, scheda)] seguendo `coda`."""
    import datetime as _dt

    per_num = {m["num"]: m for m in MEMI}
    giorno = _dt.date.fromisoformat(inizio or INIZIO)
    fuori = []
    i = 0
    nums = coda(esclusi)
    while i < len(nums):
        for ora in ORARI[:SCHEDE_AL_GIORNO]:
            if i < len(nums):
                fuori.append((giorno, ora, per_num[nums[i]]))
                i += 1
        giorno += _dt.timedelta(days=1)
    return fuori
