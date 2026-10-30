# -*- coding: utf-8 -*-
"""
MEMETECA — la scaletta dei candidati.

Le schede non si scrivono più tutte in anticipo: si preparano poco prima di
uscire. Questo file non contiene schede, contiene **candidati**: nomi con una
riga di appunto, da verificare al momento.

Ogni voce è un'ipotesi, non un fatto. La sessione che la lavora deve:
  1. verificare che il meme esista davvero, con almeno DUE fonti indipendenti
  2. scartarlo senza rimpianti se non regge — la ricerca della prima settimana
     ha buttato oltre 50 candidati su 71, ed è il motivo per cui l'archivio
     è credibile
  3. scrivere la scheda completa e appenderla a MEMI in contenuti.py

`prossimo_candidato()` restituisce il primo non ancora lavorato.
"""

# Console Windows in cp1252: senza questo, un accento fa morire lo script.
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")
import re
import unicodedata

from contenuti import MEMI

# Scartati con motivo, 27 agosto 2026. Restano scritti perche' la prossima
# sessione non li ricerchi da capo: uno scarto documentato vale quanto una
# scheda. Non tornano in CANDIDATI.
SCARTATI = {
    "«Non ce la posso fare» / Er Brasiliano": "cercata il 23 ottobre 2026: "
        "nessuna fonte documenta la frase come meme, ne' da dove venga. "
        "Quello che le fonti documentano di Massimiliano Minnocci sono le "
        "minacce a una giornalista in diretta televisiva nel 2019 e una "
        "vicenda giudiziaria del 2025. Scartata due volte: non c'e' il "
        "fatto, e il personaggio non e' noto per una battuta",
    "«Sto ca**o» di Vasco Rossi a Sanremo": "cercata il 23 ottobre 2026: "
        "nessuna fonte riporta una frase del genere a Sanremo, ne' nel 1982 "
        "ne' nel 1983. Cercando pero' e' venuta fuori la cosa vera — la "
        "leggenda dell'ultimo posto, nata dall'elenco in ordine alfabetico "
        "del 1982 — ed e' diventata la scheda 060. REGOLA: un appunto "
        "sbagliato puo' comunque indicare il punto giusto dove scavare",
    "Il Tapiro d'oro": "cercato il 23 ottobre 2026 come candidato di "
        "riserva, mai entrato in CANDIDATI. Scartato: tutte le fonti sulla "
        "nascita del premio sono l'archivio di Striscia la notizia e i siti "
        "che lo ricopiano, e su quando Staffelli abbia preso il posto del "
        "Gabibbo quell'archivio e Wikipedia non vanno d'accordo. Una fonte "
        "sola, per quanto autorevole, e' la fonte interessata",
    "Barbara d'Urso e il 'cuore'": "stessa cosa di «Barbara d'Urso e il "
        "«col cuore»», gia' in questa lista: la voce era entrata due volte in "
        "CANDIDATI con due titoli diversi, e prossimo_candidato() non la "
        "filtrava perche' confronta le stringhe. Scartata il 16 ottobre 2026 "
        "per lo stesso motivo della prima volta: solo fonti di gossip. "
        "REGOLA: uno scarto vale per il fatto, non per il titolo con cui lo "
        "si e' scritto",
    "«Non è normale che sia normale»": "le fonti ci sono e sono solide: e' "
        "lo slogan della campagna contro la violenza sulle donne lanciata "
        "nel 2018 da Mara Carfagna. Proprio per questo non entra: non e' un "
        "tormentone, e' una frase di una campagna sui femminicidi. "
        "Schedarla in un archivio di tormentoni la sminuirebbe, e il "
        "registro di MEMETECA non e' quello. Scarto editoriale, non di "
        "documentazione",
    "«No Martini, no party»": "la campagna Martini con George Clooney "
        "esiste e lo spot e' del 2000, ma le uniche fonti sono YouTube, "
        "Pinterest e blog: niente di editoriale che dati la campagna o "
        "documenti la vita italiana della frase. Stesso motivo del jingle "
        "Amaro Montenegro. Riprendibile con una fonte seria",
    "«Che fai, mi cacci?» / Il Divo": "cercata: nessuna fonte collega la "
        "battuta al film di Sorrentino (2008) ne' a una frase vera di "
        "Andreotti. Le raccolte di citazioni del film non la riportano",
    "Il jingle Amaro Montenegro": "lo slogan «sapore vero» esiste ed e' "
        "degli anni Ottanta, ma le fonti sono blog e archivi di spot che "
        "si contraddicono sulla data (1980 o 1983) e non c'e' niente di "
        "editoriale. Riprendibile se salta fuori una fonte che dati la "
        "campagna",
    "«Sarabanda» e la Zorro": "il programma e' documentato benissimo "
        "(Italia 1, 8 settembre 1997 - 20 febbraio 2004, oltre 1700 "
        "puntate), ma la scheda avrebbe bisogno di una frase o di un "
        "formato preciso, e sulla «Zorro» non ho trovato niente che la "
        "descriva. Una scheda su un programma intero non e' una scheda: "
        "riprendibile se salta fuori la documentazione del gioco",
    "«Vabbè, ciao» di Rocco Siffredi": "cercata: nessuna fonte documenta la "
        "frase come meme o tormentone. Quello che salta fuori cercandola e' "
        "la denuncia per molestie di una giornalista (2024), cioe' cronaca "
        "giudiziaria su una persona viva: non e' materiale d'archivio e "
        "schedarlo somiglierebbe a uno sfottio",
    "«Bella zio» / Verdone «Un sacco bello»": "l'appunto attribuiva la "
        "battuta a «Un sacco bello» (1980). Cercata: le fonti sul film "
        "(MYmovies, Davinotti, Bietti) elencano le battute celebri e questa "
        "non c'e'. Il gergo esiste, il film no: e' un ricordo, non un fatto. "
        "Vedi anche la voce «Giacomo Trave / 'Bella zio'» qui sotto: e' lo "
        "stesso vicolo cieco preso da un'altra parte",
    "Ferrero Rocher / «Ambasciatore, lei ci sta viziando»": "lo spot esiste "
        "ed e' documentato, ma e' BRITANNICO: girato per il Regno Unito nel "
        "1993, dove e' diventato un tormentone parodiato per decenni (Il "
        "Post, 3 mag 2018). La frase italiana che tutti citano e' una "
        "ritraduzione, e non sono riuscito a trovarne due fonti che ne "
        "fissino il testo esatto e la messa in onda italiana. Riprendibile "
        "se salta fuori l'archivio dello spot italiano",
    "Barbara d'Urso e il «col cuore»": "il tormentone esiste, ma le uniche "
        "fonti sono siti di gossip che lo raccontano di sfuggita: nessuna "
        "ricostruzione di quando nasce ne' di come diventa meme. In piu' "
        "sarebbe una scheda sul bersaglio e non sull'autore di un formato",
    "Er Trenta": "nessuna fonte: non risulta documentato da nessuna parte, "
                 "ne' come meme ne' come tormentone universitario",
    "Ciao sono Filippo Champagne": "esiste ed e' documentato (Il Messaggero, "
                                   "MonzaToday), ma e' un personaggio del "
                                   "presente, non un meme, e l'appunto lo "
                                   "datava agli anni 2000: falso. In piu' la "
                                   "notorieta' si regge su ludopatia e alcol, "
                                   "e schedarlo somiglierebbe a uno sfottio",
    "Giacomo Trave / 'Bella zio'": "«bella zio» e' gergo documentato, ma il "
                                   "nome dell'inventore no: nessuna fonte "
                                   "collega l'espressione a una persona",
    "Il Signoraggio": "i fatti storici reggono (Auriti 1923-2006, cattedra "
                      "di diritto internazionale a Teramo, il SIMEC "
                      "sequestrato a Guardiagrele nell'agosto 2000), ma la "
                      "parte che serve a noi — che sia diventato un "
                      "tormentone da forum — sta quasi solo su blog. "
                      "Riprendibile se salta fuori una fonte seria",
    "Il caso Marrazzo": "proposto da Luigi il 29 agosto 2026, scartato lo "
                        "stesso giorno per DUE motivi. Il primo: come meme "
                        "non esiste — nessuna fonte documenta un tormentone "
                        "o un formato nato da quella vicenda, c'e' solo "
                        "cronaca (luglio 2009, il video dei carabinieri in "
                        "via Gradoli, la condanna dei quattro militari nel "
                        "novembre 2018). Il secondo, che pesa di piu' e "
                        "vale anche se un giorno saltasse fuori una fonte: "
                        "e' una storia di ricatto con una vittima di reato, "
                        "e la donna trans coinvolta e' morta in un incendio "
                        "pochi mesi dopo. Schedarla sarebbe rovistare in una "
                        "vicenda privata finita male sotto forma di "
                        "intrattenimento — la definizione esatta di «cercare "
                        "la rissa». NON si riprende",
    "«Renzi stai sereno»": "e' gia' in archivio come scheda 024 ENRICO STAI "
                           "SERENO. Il confronto normalizzato non lo "
                           "riconosce perche' cambia il nome: tolto a mano",
}


# Chiavi: nome di lavoro → appunto di partenza (da verificare, non da citare)
# 12 ottobre 2026: la lista si sta svuotando. Delle voci rimaste, molte
# sono «da verificare» e cadono alla prima ricerca, e le schede 054 e 055
# (STICAZZI, BUONGIORNISSIMO KAFFE') le ho prese da fuori, cercando casi
# documentati che non fossero gia' in archivio. Non e' una violazione della
# regola: la regola dice di non SCEGLIERE leggendo CANDIDATI a occhio, per
# non riscrivere schede gia' pubblicate — il controllo contro i doppioni
# resta prossimo_candidato() piu' _controlla_doppioni(). Aggiungere voci
# nuove alla lista, con le fonti gia' trovate, e' il modo di tenerla viva.
CANDIDATI = {
    # ── 30 ottobre 2026. Le schede 062, 063 e 064 (BLOB, QUELLI DELLA NOTTE,
    # MAI DIRE GOL) le ho prese di nuovo da fuori lista, e non a caso: la
    # categoria TV era rimasta con una sola scheda in coda, e coda() la
    # domenica pesca li'. Quando una categoria si svuota non basta scrivere
    # schede, bisogna scriverne di quella categoria. Queste tre lasciano
    # aperta la stessa vena — la televisione italiana che faceva i meme prima
    # che si chiamassero cosi' — e qui sotto ci sono le prossime.
    "«Non capisco ma mi adeguo» / Ferrini": "la battuta ha una scheda madre "
        "(063) ma una vita propria: verificare se regge da sola",
    "Striscia la notizia e il Gabibbo in politica": "la 027 copre il "
        "personaggio, non gli usi politici — verificare che esistano fonti",
    "«Drive In» (1983)": "Antonio Ricci, Italia 1: la fabbrica di tormentoni "
        "prima di Mai dire gol — verificare date e personaggi su due fonti",
    # ── trovate il 16 ottobre 2026 cercando fuori lista, con le fonti ──────
    # ── internet italiano, era forum e primo Facebook ───────────────────────
    "Er Trenta": "presunto meme universitario romano — verificare se esiste davvero",
    "Ciao sono Filippo Champagne": "personaggio del web anni 2000 — da verificare",
    "Giacomo Trave / 'Bella zio'": "tormentone da verificare",
    "Il Signoraggio": "complottismo economico diventato tormentone da forum",
    "«Che vor dì?» / Er Faina II": "eventuale seconda scheda sul personaggio",
    "«Sei un mito» / Alessandro Borghese": "verificare se è meme o solo tormentone TV",

    # ── internet italiano recente ───────────────────────────────────────────
    "Il pandoro-gate: gli sviluppi 2026": "eventuale aggiornamento della scheda 008",
    "«Non è normale che sia normale»": "da verificare",
    "Cateno De Luca": "sindaco-meme, verificare la documentazione",
    "«Vabbè, ciao» di Rocco Siffredi": "da verificare",
    "I Ferragnez come format": "distinguere dal pandoro-gate",
    "Il meme di Sinner e il 'mai una gioia'": "verificare se esiste come meme",
    "Rosa Chemical a Sanremo 2023": "verificare se esiste come meme e non solo cronaca",
    "Il 'nonno' di TikTok Italia": "da identificare e verificare",

    # ── cinema e televisione ────────────────────────────────────────────────
        "«Le donne ci guardano» / Ecce Bombo": "verificare quale battuta ha fatto scuola",
    "«Ho fatto tredici!» / Totò": "verificare",
    "«Come è profondo il mare»": "Dalla, uso ironico online",
    "«Bella zio» / Verdone «Un sacco bello»": "1980",
    "«Che c'ho la faccia da fesso?» / Verdone": "da verificare",
    "«Fantozzi subisce»": "la formula narrativa come meme",
    "«Che fai, mi cacci?» / Il Divo": "da verificare",
    "Boris: seconda scheda su «la qualità»": "il lessico della serie dà per più schede",

    # ── TV e pubblicità (le domeniche) ──────────────────────────────────────
    "«No Martini, no party»": "campagna anni 90",
    "«Ricco, mi fai impazzire» / Ferrero Rocher": "anni 80-90",
    "«Chi vuol essere miliardario» e Gerry Scotti": "Meme Award 2023 al personaggio più memato",
    "«Sarabanda» e la Zorro": "verificare",
    "«Domenica In» e i tormentoni della TV di stato": "restringere a un caso documentato",
    "Il jingle Amaro Montenegro": "verificare",
    "Sanremo: la standing ovation di Benigni 2020": "verificare se è meme",
}


def _norm(t):
    """Riduce un titolo alla sua sostanza, per confrontarlo con un candidato.
    «Mi si nota di piu' se vengo e me ne sto in disparte» e la scheda
    «MI SI NOTA DI PIU'» sono la stessa cosa; il confronto secco no."""
    t = unicodedata.normalize("NFC", t).lower()
    t = re.sub(r"[«»\"'’`.,;:!?()\-–—/]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# Candidati che restano validi ANCHE se un titolo simile e' gia' in archivio:
# sono seconde schede volute sullo stesso soggetto, non doppioni.
BIS = {"«Che vor dì?» / Er Faina II", "Boris: seconda scheda su «la qualità»"}


def gia_fatti():
    """I titoli già presenti in archivio, normalizzati per il confronto."""
    return {_norm(m["titolo"]) for m in MEMI}


def stantii():
    """I candidati che corrispondono a una scheda gia' scritta.

    27 agosto 2026: una sessione ha letto CANDIDATI a occhio e ha riscritto
    cinque schede che esistevano gia' — LERCIO, MI SI NOTA DI PIU', ITALIAN
    BRAINROT, SPINOZA, IL GABIBBO. CANDIDATI e' una lista statica: non si
    sfoltisce da sola quando una voce viene lavorata. Chi cerca un candidato
    passa da prossimo_candidato(), mai dal dizionario nudo."""
    fatti = gia_fatti()
    fuori = []
    for nome in CANDIDATI:
        if nome in BIS:
            continue
        n = _norm(nome)
        if any(t and (t in n or n in t) for t in fatti):
            fuori.append(nome)
    return fuori


def prossimo_candidato(saltati=()):
    """Il primo candidato non ancora lavorato. `saltati` sono quelli scartati
    in sessioni precedenti perché non verificabili."""
    esclusi = set(stantii()) | set(SCARTATI) | {s for s in saltati}
    saltati_n = {_norm(s) for s in saltati}
    for nome, appunto in CANDIDATI.items():
        if nome in esclusi or _norm(nome) in saltati_n:
            continue
        return nome, appunto
    return None, None


def prossimo_numero():
    """Il numero da assegnare alla prossima scheda."""
    return f"{max(int(m['num']) for m in MEMI) + 1:03d}"


if __name__ == "__main__":
    nome, appunto = prossimo_candidato()
    print(f"scaletta: {len(CANDIDATI)} candidati, {len(MEMI)} schede già scritte")
    fermi = stantii()
    if fermi:
        print(f"da togliere (già schedati): {', '.join(fermi)}")
    print(f"prossimo numero: {prossimo_numero()}")
    print(f"prossimo candidato: {nome}\n  {appunto}")
