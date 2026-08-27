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
    "«Renzi stai sereno»": "e' gia' in archivio come scheda 024 ENRICO STAI "
                           "SERENO. Il confronto normalizzato non lo "
                           "riconosce perche' cambia il nome: tolto a mano",
}


# Chiavi: nome di lavoro → appunto di partenza (da verificare, non da citare)
CANDIDATI = {
    # ── internet italiano, era forum e primo Facebook ───────────────────────
    "Er Trenta": "presunto meme universitario romano — verificare se esiste davvero",
    "Ciao sono Filippo Champagne": "personaggio del web anni 2000 — da verificare",
    "Giacomo Trave / 'Bella zio'": "tormentone da verificare",
    "Il Signoraggio": "complottismo economico diventato tormentone da forum",
    "«Che vor dì?» / Er Faina II": "eventuale seconda scheda sul personaggio",
    "iPantellas / Favij": "generazione YouTube 2013-2015",
    "«Sto ca**o» di Vasco Rossi a Sanremo": "da verificare",
    "«Sei un mito» / Alessandro Borghese": "verificare se è meme o solo tormentone TV",
    "Barbara d'Urso e il 'cuore'": "gestualità diventata meme",

    # ── internet italiano recente ───────────────────────────────────────────
    "Il pandoro-gate: gli sviluppi 2026": "eventuale aggiornamento della scheda 008",
    "«Non è normale che sia normale»": "da verificare",
    "Cateno De Luca": "sindaco-meme, verificare la documentazione",
    "Er Pipa / neomelodici su TikTok": "da verificare",
    "Il tormentone «Ambaradan»": "verificare origine storica (Amba Aradam) e uso online",
    "«Vabbè, ciao» di Rocco Siffredi": "da verificare",
    "I Ferragnez come format": "distinguere dal pandoro-gate",
    "Il meme di Sinner e il 'mai una gioia'": "verificare se esiste come meme",
    "«Poi però» / Mario Giordano": "toni da talk show diventati meme",
    "La 'sciura' milanese": "archetipo, verificare la documentazione",
    "Rosa Chemical a Sanremo 2023": "verificare se esiste come meme e non solo cronaca",
    "Il 'nonno' di TikTok Italia": "da identificare e verificare",

    # ── cinema e televisione ────────────────────────────────────────────────
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
    "«No Martini, no party»": "campagna anni 90",
    "«Che mondo sarebbe senza Nutella»": "verificare la datazione",
    "«Ava come lava»": "pubblicità storica",
    "«Ricco, mi fai impazzire» / Ferrero Rocher": "anni 80-90",
    "«Chi vuol essere miliardario» e Gerry Scotti": "Meme Award 2023 al personaggio più memato",
    "«Sarabanda» e la Zorro": "verificare",
    "«Domenica In» e i tormentoni della TV di stato": "restringere a un caso documentato",
    "«Ok il prezzo è giusto» / Iva Zanicchi": "verificare",
    "Il jingle Amaro Montenegro": "verificare",
    "«Casa Vianello» / «Mammina cara»": "verificare la battuta ricorrente",
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
