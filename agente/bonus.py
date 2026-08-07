# -*- coding: utf-8 -*-
"""
MEMETECA — post bonus «fuori collana».

Un post extra, oltre ai due del calendario, quando la giornata lo merita davvero.
Non è una scheda: è la pagina che guarda l'attualità dalla sua feritoia, cioè
l'archivio. Palette invertita — carta scura, inchiostro chiaro — per distinguerlo
a colpo d'occhio nella griglia.

Le regole editoriali su quando si pubblica e quando si desiste stanno in
docs/07_POST_BONUS.md e non sono negoziabili: nel dubbio non si pubblica.

Uso:

    from bonus import DATI_ESEMPIO, genera, caption
    percorsi = genera(dati, "../assets")     # 3 jpg 1080x1350
    testo    = caption(dati)                 # caption pronta, sotto i 2.200

Il dizionario `dati` vuole queste chiavi:

    slug        identificativo per i nomi file, es. "guccini"
    titolo      il titolo grande in copertina
    sottotitolo riga sotto il titolo (facoltativa), es. "1940 — 2026"
    etichetta   il chip rosso, es. "In memoria", "L'attualità", "Anniversario"
    occhiello   la citazione o frase in corsivo sotto il filetto
    apertura    il gancio: perché questa notizia riguarda l'archivio
    blocchi     lista di 2-4 dict {titolo, testo} — il corpo, slide 2 e 3
    riquadro    dict {testo} messo in evidenza su fondo pieno (facoltativo)
    chiusura    la riga finale della caption, quella che resta
    fonti       lista di fonti verificate, minimo due indipendenti
    hashtag     massimo 5, specifici
"""

# Console Windows in cp1252: senza questo, un accento fa morire lo script.
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")
import pathlib

from playwright.sync_api import sync_playwright

import grafica
from contenuti import BRAND, LIMITE_INSTAGRAM, MARGINE, lunghezza_instagram

QUI = pathlib.Path(__file__).parent

LUTTO = {
    "carta": "#14110F",
    "inchiostro": "#EFE7D8",
    "rosso": "#E0553E",
    "grigio": "#8A8073",
    "carta_scura": "#0D0B0A",
}


# ────────────────────────────────────────────────────────────────── caption
def caption(d):
    parti = [f"{d['titolo']} — {d['apertura']}", ""]
    for b in d["blocchi"]:
        parti += [b["titolo"].upper(), b["testo"], ""]
    if d.get("riquadro"):
        parti += [d["riquadro"]["testo"], ""]
    parti += [d["chiusura"], ""]
    if d.get("congedo"):
        parti += [d["congedo"], ""]
    parti += [f"— {collana(d)} · Fonti: {' · '.join(d['fonti'])}",
              f"Segui {BRAND['handle']}", "",
              " ".join(d["hashtag"][:5])]
    return "\n".join(parti)


def verifica(d):
    """Controlli minimi prima di pubblicare. Solleva se qualcosa non torna."""
    problemi = []
    if len(d.get("fonti", [])) < 2:
        problemi.append("servono almeno due fonti indipendenti")
    if len(d.get("hashtag", [])) > 5:
        problemi.append("massimo 5 hashtag (limite Instagram da dicembre 2025)")
    if not 2 <= len(d.get("blocchi", [])) <= 4:
        problemi.append("servono da 2 a 4 blocchi")
    n = lunghezza_instagram(caption(d))
    if n > LIMITE_INSTAGRAM - MARGINE:
        problemi.append(f"caption troppo lunga: {n} caratteri")
    if problemi:
        raise ValueError("Post bonus non pubblicabile:\n  - " + "\n  - ".join(problemi))
    return n


# ────────────────────────────────────────────────────────────────── le slide
def _css():
    C = LUTTO
    return (grafica.BASE_CSS
            .replace(BRAND["colori"]["carta"], "__CARTA__")
            .replace(BRAND["colori"]["inchiostro"], C["inchiostro"])
            .replace("__CARTA__", C["carta"])
            .replace(BRAND["colori"]["rosso"], C["rosso"])
            .replace("opacity:.06", "opacity:.10"))


def collana(d):
    """L'etichetta in alto a destra. Il manifesto non e' «fuori collana»:
    e' il post che spiega la collana, e scriverci sopra il contrario
    sarebbe l'unico errore che un archivio non puo' permettersi."""
    return d.get("collana", "Fuori collana")


def _testata(dx):
    return (f'<div class="testata z"><span class="marchio">{BRAND["nome"]}</span>'
            f'<span class="num">{dx}</span></div>')


def slide_1(d):
    C = LUTTO
    sotto = ""
    if d.get("sottotitolo"):
        sotto = (f'<div class="z" style="font-family:\'Archivo\';font-weight:900;'
                 f'font-size:44px;letter-spacing:.04em;margin:26px 0 34px;'
                 f'color:{C["rosso"]};">{grafica._e(d["sottotitolo"])}</div>')
    return f"""<div class="slide">
  <div class="grana"></div>
  {_testata(collana(d))}
  <div class="z" style="margin-top:56px;">
    <span class="chip">{grafica._e(d['etichetta'])}</span></div>
  <div class="z" style="flex:1;min-height:44px;"></div>
  <div class="z titolone" data-fit="164" data-min="44"
       style="height:430px;">{grafica._e(d['titolo'])}</div>
  {sotto}
  <div class="z serif" data-fit="56" data-min="30"
       style="height:200px;max-width:880px;margin-bottom:54px;"
       >{grafica._e(d['occhiello'])}</div>
  <div class="z corpo" data-fit="27" data-min="20"
       style="height:150px;max-width:880px;opacity:.8;
              border-left:5px solid {C['rosso']};padding-left:22px;margin-bottom:30px;"
       >{grafica._e(grafica._taglia(d['apertura'], 200))}</div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span>
    <span>Scorri &nbsp;›&nbsp;›&nbsp;›</span></div>
</div>"""


def _blocco(b, altezza):
    return (f'<div><div class="etichetta">{grafica._e(b["titolo"])}</div>'
            f'<div class="corpo" data-fit="30" data-min="19" style="height:{altezza}px;">'
            f'{grafica._e(b["testo"])}</div></div>')


def slide_2(d):
    C = LUTTO
    blocchi = d["blocchi"][:2]
    corpo = "".join(_blocco(b, 380) for b in blocchi)
    riq = ""
    if d.get("riquadro"):
        riq = (f'<div style="background:{C["inchiostro"]};color:{C["carta"]};'
               f'padding:34px 38px;"><div class="corpo" data-fit="29" data-min="20" '
               f'style="height:170px;">{grafica._e(d["riquadro"]["testo"])}</div></div>')
    return f"""<div class="slide">
  <div class="grana"></div>
  {_testata(collana(d))}
  <div class="z etichetta" style="margin:32px 0 6px;">{grafica._e(collana(d))}</div>
  <h2 class="z titolone" data-fit="66" data-min="38"
      style="height:150px;flex:none;margin-bottom:36px;">{grafica._e(d['titolo'])}</h2>
  <div class="z" style="flex:1;display:flex;flex-direction:column;
       padding-bottom:22px;">
    <div style="display:flex;flex-direction:column;gap:38px;">{corpo}</div>
    <div style="flex:1;min-height:32px;"></div>
    {riq}
  </div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span>
    <span>{grafica._e(d.get('sottotitolo', ''))}</span></div>
</div>"""


def slide_3(d):
    C = LUTTO
    resto = d["blocchi"][2:]
    corpo = "".join(_blocco(b, 330) for b in resto) if resto else ""
    chius = (f'<div><div class="etichetta">Perché lo raccontiamo</div>'
             f'<div class="serif" data-fit="50" data-min="30" style="height:330px;">'
             f'{grafica._e(d["chiusura"])}</div></div>')
    return f"""<div class="slide">
  <div class="grana"></div>
  {_testata(collana(d))}
  <div class="z" style="flex:1;display:flex;flex-direction:column;
       justify-content:space-between;padding:38px 0 22px;">
    {corpo}
    {chius}
    <div style="font-size:18px;line-height:1.5;color:{C['grigio']};">
      Fonti verificate: {grafica._e(' · '.join(d['fonti']))}</div>
  </div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span>
    <span>{grafica._e(BRAND['payoff'])}</span></div>
</div>"""


def genera(d, cartella):
    """Renderizza le 3 slide. Ritorna i percorsi."""
    verifica(d)
    cartella = pathlib.Path(cartella)
    cartella.mkdir(parents=True, exist_ok=True)
    css = _css()
    percorsi = []
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--force-color-profile=srgb"])
        pg = br.new_page(viewport={"width": grafica.W, "height": grafica.H},
                         device_scale_factor=1)
        for i, fn in enumerate((slide_1, slide_2, slide_3), start=1):
            doc = f"<!doctype html><meta charset='utf-8'><style>{css}</style>{fn(d)}"
            pg.set_content(doc, wait_until="load")
            pg.evaluate(grafica.AUTOFIT)
            pg.wait_for_timeout(60)
            out = cartella / f"{d['slug']}_{i}.jpg"
            pg.screenshot(path=str(out), type="jpeg", quality=93)
            percorsi.append(str(out))
            print(f"  ✓ slide {i}")
        br.close()
    return percorsi


# Esempio reale: il fuori collana pubblicato il 6 agosto 2026.
DATI_ESEMPIO = {
    "slug": "guccini",
    "titolo": "FRANCESCO GUCCINI",
    "sottotitolo": "1940 — 2026",
    "congedo": "Mandala a chi se la ricorda.",
    "etichetta": "In memoria",
    "occhiello": "«Anche Dante è stato letto da cani e porci»",
    "apertura": "Un meme su Guccini non esiste. In compenso esiste il contrario: "
                "internet che decide chi era, e lui che risponde una volta sola, benissimo.",
    "blocchi": [
        {"titolo": "Il fatto",
         "testo": "È morto il 6 agosto 2026, a 86 anni. Bologna ha proclamato "
                  "il lutto cittadino per il giorno dei funerali."},
        {"titolo": "Quando internet lo diede per morto",
         "testo": "Il 19 ottobre 2014 Matteo Renzi dice da Barbara d'Urso che Guccini "
                  "è il suo cantautore preferito. Poche ore dopo circola un tweet "
                  "attribuito a Stefano Fassina, falso, fabbricato con un generatore "
                  "di tweet contraffatti. L'autore si autodenuncia il giorno stesso. "
                  "La bufala continua a circolare lo stesso, per anni."},
        {"titolo": "La risposta",
         "testo": "Palermo, 10 maggio 2019. Gli chiedono di Salvini che si dichiara "
                  "suo fan. Guccini: «Se le mie canzoni piacciono a Matteo Salvini, "
                  "non ho alcuna responsabilità. Con le dovute differenze, anche "
                  "Dante è stato letto da cani e porci»."},
    ],
    "chiusura": "Una frase sola, detta una volta. È il motivo per cui non gli "
                "serviva un meme.",
    "fonti": ["Open (6 ago 2026)", "Il Fatto Quotidiano (10 mag 2019)",
              "Giornalettismo (2014)"],
    "hashtag": ["#francescoguccini", "#guccini", "#memeteca", "#lalocomotiva",
                "#storiadeimeme"],
}


if __name__ == "__main__":
    n = verifica(DATI_ESEMPIO)
    print(f"caption: {n} caratteri su {LIMITE_INSTAGRAM}\n")
    print(caption(DATI_ESEMPIO))
