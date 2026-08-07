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
from contenuti import MEMI

# Chiavi: nome di lavoro → appunto di partenza (da verificare, non da citare)
CANDIDATI = {
    # ── internet italiano, era forum e primo Facebook ───────────────────────
    "Er Trenta": "presunto meme universitario romano — verificare se esiste davvero",
    "Ciao sono Filippo Champagne": "personaggio del web anni 2000 — da verificare",
    "Giacomo Trave / 'Bella zio'": "tormentone da verificare",
    "Il Cinepanettone come genere-meme": "Boldi/De Sica, sfottò ricorrente online",
    "Lercio": "testata satirica dal 2012, notizie false verosimili",
    "Spinoza.it": "dal 2006, battuta come forma editoriale con firma dell'autore",
    "Il Signoraggio": "complottismo economico diventato tormentone da forum",
    "«Renzi stai sereno»": "Renzi a Letta, dicembre 2013 — verificare la datazione",
    "«Che vor dì?» / Er Faina II": "eventuale seconda scheda sul personaggio",
    "Frank Matano / Le Iene scherzi telefonici": "primo YouTube italiano",
    "Willwoosh (Guglielmo Scilla)": "primo youtuber italiano di massa, 2009",
    "iPantellas / Favij": "generazione YouTube 2013-2015",
    "«Sto ca**o» di Vasco Rossi a Sanremo": "da verificare",
    "Il Grande Fratello 1 e 'Cristina Plevani'": "2000, nascita del reality italiano",
    "«Sei un mito» / Alessandro Borghese": "verificare se è meme o solo tormentone TV",
    "Barbara d'Urso e il 'cuore'": "gestualità diventata meme",

    # ── internet italiano recente ───────────────────────────────────────────
    "Italian brainrot": "2025, fenomeno ITALIANO documentato solo da fonti straniere "
                        "(NYT, Guardian, Daily Dot). Scheda ad alto potenziale",
    "Il pandoro-gate: gli sviluppi 2026": "eventuale aggiornamento della scheda 008",
    "«Non è normale che sia normale»": "da verificare",
    "Cateno De Luca": "sindaco-meme, verificare la documentazione",
    "Er Pipa / neomelodici su TikTok": "da verificare",
    "«Mi consenta» di Berlusconi": "tormentone storico, verificare la prima volta",
    "Il tormentone «Ambaradan»": "verificare origine storica (Amba Aradam) e uso online",
    "«Vabbè, ciao» di Rocco Siffredi": "da verificare",
    "I Ferragnez come format": "distinguere dal pandoro-gate",
    "Il meme di Sinner e il 'mai una gioia'": "verificare se esiste come meme",
    "«Poi però» / Mario Giordano": "toni da talk show diventati meme",
    "La 'sciura' milanese": "archetipo, verificare la documentazione",
    "Rosa Chemical a Sanremo 2023": "verificare se esiste come meme e non solo cronaca",
    "Il 'nonno' di TikTok Italia": "da identificare e verificare",

    # ── cinema e televisione ────────────────────────────────────────────────
    "«Mi si nota di più se vengo e me ne sto in disparte»": "Moretti, Ecce Bombo 1978",
    "«Le donne ci guardano» / Ecce Bombo": "verificare quale battuta ha fatto scuola",
    "«Ho fatto tredici!» / Totò": "verificare",
    "«A me gli occhi, please»": "Gigi Proietti, 1976 — verificare la seconda vita online",
    "«Come è profondo il mare»": "Dalla, uso ironico online",
    "«Bella zio» / Verdone «Un sacco bello»": "1980",
    "«Che c'ho la faccia da fesso?» / Verdone": "da verificare",
    "«Sono un uomo di mondo» / Totò": "verificare la battuta esatta e il film",
    "«Fantozzi subisce»": "la formula narrativa come meme",
    "«Il Gattopardo: se vogliamo che tutto rimanga com'è»": "uso politico della citazione",
    "«L'anno che verrà»": "da verificare",
    "Ricky Memphis / Notte prima degli esami": "verificare",
    "«Che fai, mi cacci?» / Il Divo": "da verificare",
    "Boris: seconda scheda su «la qualità»": "il lessico della serie dà per più schede",

    # ── TV e pubblicità (le domeniche) ──────────────────────────────────────
    "Carosello": "1957-1977, la preistoria del formato pubblicitario italiano",
    "«No Martini, no party»": "campagna anni 90",
    "«Che mondo sarebbe senza Nutella»": "verificare la datazione",
    "«Ava come lava»": "pubblicità storica",
    "«Contro il logorio della vita moderna» / Cynar": "Calindri, anni 60-70",
    "«Ricco, mi fai impazzire» / Ferrero Rocher": "anni 80-90",
    "Il Gabibbo": "1990, Striscia la notizia",
    "«Chi vuol essere miliardario» e Gerry Scotti": "Meme Award 2023 al personaggio più memato",
    "«Sarabanda» e la Zorro": "verificare",
    "Non è la Rai": "1991-1995, culto e archivio",
    "«Domenica In» e i tormentoni della TV di stato": "restringere a un caso documentato",
    "«Ok il prezzo è giusto» / Iva Zanicchi": "verificare",
    "Il jingle Amaro Montenegro": "verificare",
    "«Casa Vianello» / «Mammina cara»": "verificare la battuta ricorrente",
    "Sanremo: la standing ovation di Benigni 2020": "verificare se è meme",
}


def gia_fatti():
    """I titoli già presenti in archivio, normalizzati per il confronto."""
    return {m["titolo"].lower() for m in MEMI}


def prossimo_candidato(saltati=()):
    """Il primo candidato non ancora lavorato. `saltati` sono quelli scartati
    in sessioni precedenti perché non verificabili."""
    fatti = gia_fatti()
    saltati = {s.lower() for s in saltati}
    for nome, appunto in CANDIDATI.items():
        if nome.lower() in fatti or nome.lower() in saltati:
            continue
        return nome, appunto
    return None, None


def prossimo_numero():
    """Il numero da assegnare alla prossima scheda."""
    return f"{max(int(m['num']) for m in MEMI) + 1:03d}"


if __name__ == "__main__":
    nome, appunto = prossimo_candidato()
    print(f"scaletta: {len(CANDIDATI)} candidati, {len(MEMI)} schede già scritte")
    print(f"prossimo numero: {prossimo_numero()}")
    print(f"prossimo candidato: {nome}\n  {appunto}")
