# -*- coding: utf-8 -*-
"""
MEMETECA — FUORI COLLANA: Francesco Guccini (1940-2026).

Non è una scheda meme: un meme documentato su Guccini non esiste, e inventarlo
sarebbe la cosa peggiore che questa pagina possa fare. È un fuori collana su
quel poco di Guccini che è passato davvero da internet — e su come lui lo prese.

Palette invertita rispetto alle schede ordinarie: carta scura, inchiostro chiaro.
"""
import pathlib

from playwright.sync_api import sync_playwright

import grafica
from contenuti import BRAND, lunghezza_instagram

QUI = pathlib.Path(__file__).parent

# ─────────────────────────────────────────────────────────────── palette lutto
LUTTO = {
    "carta": "#14110F",
    "inchiostro": "#EFE7D8",
    "rosso": "#E0553E",
    "grigio": "#8A8073",
    "carta_scura": "#0D0B0A",
}

DATI = {
    "titolo": "FRANCESCO GUCCINI",
    "anni": "1940 — 2026",
    "occhiello": "«Anche Dante è stato letto da cani e porci»",
    "hook": "Un meme su Guccini non esiste. In compenso esiste il contrario: "
            "internet che decide chi era, e lui che risponde una volta sola, benissimo.",

    "morte": "È morto oggi, 6 agosto 2026, a 86 anni. Bologna ha proclamato "
             "il lutto cittadino per il giorno dei funerali.",

    "bufala_t": "Quando internet lo diede per morto",
    "bufala": "Il 19 ottobre 2014 Matteo Renzi dice da Barbara d'Urso che Guccini è il suo "
              "cantautore preferito. Poche ore dopo circola un tweet attribuito a Stefano "
              "Fassina: «Renzi dice che il suo cantautore preferito è Guccini! In questo "
              "momento Guccini si sta rivoltando nella tomba!». Il tweet è falso, fabbricato "
              "con un generatore di tweet contraffatti. L'autore, Andrea Laudadio, si "
              "autodenuncia il giorno stesso e chiede scusa a Fassina. La bufala continua a "
              "circolare lo stesso, per anni.",
    "bufala_nota": "Giornalettismo, all'epoca, la spiegò in una riga: «troppo verosimile "
                   "per essere verificata, troppo succulenta perché venga voglia di farlo».",

    "canzone_t": "La canzone che non gli apparteneva più",
    "canzone": "«La locomotiva» è diventata negli anni il karaoke involontario della destra "
               "italiana. Salvini nel 2019 a Matrix: «a 16 anni suonavo La locomotiva». "
               "Meloni chiude un intervento ad Atreju citando «Cirano» e lo invita "
               "personalmente: lui declina, e dirà che ne aveva travisato il significato. "
               "Il 2 ottobre 2023 Roberto Vannacci la canta al karaoke di Radio Rock e "
               "liquida l'obiezione con «la musica non ha colore politico».",

    "risposta_t": "La risposta",
    "risposta": "Palermo, 10 maggio 2019, conservatorio Scarlatti. Gli chiedono di Salvini "
                "che si dichiara suo fan. Guccini: «Se le mie canzoni piacciono a Matteo "
                "Salvini, non ho alcuna responsabilità. Con le dovute differenze, anche "
                "Dante è stato letto da cani e porci».",

    "fonti": ["Il Post", "Open (6 ago 2026)", "Il Fatto Quotidiano (10 mag 2019)",
              "Giornalettismo (2014)", "ANSA"],
}

CAPTION = f"""Un meme su Francesco Guccini non esiste.

L'abbiamo cercato prima di scrivere: Know Your Meme, Wikipedia, i principali siti italiani di debunking. Niente. Questa pagina scheda i meme e non se li inventa: oggi niente scheda, un fuori collana.

Perché una cosa, di Guccini, da internet è passata davvero — ed è il contrario di un meme. Non è lui a diventare materiale della rete: è la rete che prova a decidere chi era.

È morto oggi, 6 agosto 2026, a 86 anni. Bologna ha proclamato il lutto cittadino per il giorno dei funerali.

📰 QUANDO INTERNET LO DIEDE PER MORTO
Il 19 ottobre 2014 Matteo Renzi dice da Barbara d'Urso che Guccini è il suo cantautore preferito. Poche ore dopo circola un tweet attribuito a Stefano Fassina: «Renzi dice che il suo cantautore preferito è Guccini! In questo momento Guccini si sta rivoltando nella tomba!». Il tweet è falso, fabbricato con un generatore di tweet contraffatti. L'autore, Andrea Laudadio, si autodenuncia il giorno stesso e chiede scusa a Fassina. La bufala continua a circolare lo stesso. Giornalettismo la spiegò in una riga: «troppo verosimile per essere verificata, troppo succulenta perché venga voglia di farlo».

🚂 LA CANZONE CHE NON GLI APPARTENEVA PIÙ
«La locomotiva» è diventata il karaoke involontario della destra italiana. Salvini nel 2019 a Matrix: «a 16 anni suonavo La locomotiva». Meloni chiude un intervento ad Atreju citando «Cirano» e lo invita personalmente: lui declina, e dirà che ne aveva travisato il significato. Il 2 ottobre 2023 Roberto Vannacci la canta al karaoke di Radio Rock: «la musica non ha colore politico».

🎤 LA RISPOSTA
Palermo, 10 maggio 2019. Gli chiedono di Salvini che si dichiara suo fan. Guccini: «Se le mie canzoni piacciono a Matteo Salvini, non ho alcuna responsabilità. Con le dovute differenze, anche Dante è stato letto da cani e porci».

Una frase sola, detta una volta. È il motivo per cui non gli serviva un meme.

— Fuori collana · Fonti: Open · Il Fatto Quotidiano · Giornalettismo · ANSA
Segui {BRAND['handle']}

#francescoguccini #guccini #lalocomotiva #cantautori #memeteca #culturapop #internetitaliano #bologna #musicaitaliana #storiadeimeme"""


# ─────────────────────────────────────────────────────────────────── le slide
def slide_1():
    C = grafica.C
    return f"""<div class="slide">
  <div class="grana"></div>
  <div class="testata z"><span class="marchio">{BRAND['nome']}</span>
    <span class="num">Fuori collana</span></div>
  <div class="z" style="margin-top:56px;"><span class="chip">In memoria</span></div>
  <div class="z" style="flex:1;min-height:44px;"></div>
  <div class="z titolone" data-fit="164" data-min="44"
       style="height:430px;">{grafica._e(DATI['titolo'])}</div>
  <div class="z" style="font-family:'Archivo';font-weight:900;font-size:44px;
       letter-spacing:.04em;margin:26px 0 34px;color:{C['rosso']};">{DATI['anni']}</div>
  <div class="z serif" data-fit="56" data-min="30"
       style="height:200px;max-width:880px;margin-bottom:54px;"
       >{grafica._e(DATI['occhiello'])}</div>
  <div class="z corpo" data-fit="27" data-min="20"
       style="height:150px;max-width:880px;opacity:.8;
              border-left:5px solid {C['rosso']};padding-left:22px;margin-bottom:30px;"
       >{grafica._e(DATI['hook'])}</div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span>
    <span>Scorri &nbsp;›&nbsp;›&nbsp;›</span></div>
</div>"""


def slide_2():
    C = grafica.C
    return f"""<div class="slide">
  <div class="grana"></div>
  <div class="testata z"><span class="marchio">{BRAND['nome']}</span>
    <span class="num">Fuori collana</span></div>
  <div class="z" style="flex:1;display:flex;flex-direction:column;
       justify-content:space-between;padding:40px 0 22px;">
    <div>
      <div class="etichetta">Il fatto</div>
      <div class="corpo" data-fit="30" data-min="21" style="height:130px;"
        >{grafica._e(DATI['morte'])}</div>
    </div>
    <div>
      <div class="etichetta">{grafica._e(DATI['bufala_t'])}</div>
      <div class="corpo" data-fit="30" data-min="19" style="height:430px;"
        >{grafica._e(DATI['bufala'])}</div>
    </div>
    <div style="background:{C['inchiostro']};color:{C['carta']};padding:34px 38px;">
      <div class="corpo" data-fit="29" data-min="20" style="height:150px;"
        >{grafica._e(DATI['bufala_nota'])}</div>
    </div>
  </div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span><span>2014</span></div>
</div>"""


def slide_3():
    C = grafica.C
    return f"""<div class="slide">
  <div class="grana"></div>
  <div class="testata z"><span class="marchio">{BRAND['nome']}</span>
    <span class="num">Fuori collana</span></div>
  <div class="z" style="flex:1;display:flex;flex-direction:column;
       justify-content:space-between;padding:40px 0 22px;">
    <div>
      <div class="etichetta">{grafica._e(DATI['canzone_t'])}</div>
      <div class="corpo" data-fit="30" data-min="19" style="height:400px;"
        >{grafica._e(DATI['canzone'])}</div>
    </div>
    <div>
      <div class="etichetta">{grafica._e(DATI['risposta_t'])}</div>
      <div class="serif" data-fit="46" data-min="28" style="height:330px;"
        >{grafica._e(DATI['risposta'])}</div>
    </div>
    <div style="font-size:18px;line-height:1.5;color:{C['grigio']};">
      Fonti verificate: {grafica._e(' · '.join(DATI['fonti']))}</div>
  </div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span>
    <span>{grafica._e(BRAND['payoff'])}</span></div>
</div>"""


def genera(cartella):
    cartella = pathlib.Path(cartella)
    cartella.mkdir(parents=True, exist_ok=True)
    grafica.C = LUTTO                      # palette invertita
    grafica.BASE_CSS = grafica.BASE_CSS    # ricostruita sotto
    css = _css_lutto()
    percorsi = []
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--force-color-profile=srgb"])
        pg = br.new_page(viewport={"width": grafica.W, "height": grafica.H},
                         device_scale_factor=1)
        for i, fn in enumerate((slide_1, slide_2, slide_3), start=1):
            pg.set_content(f"<!doctype html><meta charset='utf-8'><style>{css}</style>{fn()}",
                           wait_until="load")
            pg.evaluate(grafica.AUTOFIT)
            pg.wait_for_timeout(60)
            out = cartella / f"guccini_{i}.jpg"
            pg.screenshot(path=str(out), type="jpeg", quality=93)
            percorsi.append(str(out))
            print(f"  ✓ slide {i}")
        br.close()
    return percorsi


def _css_lutto():
    """Stessa grammatica delle schede, colori invertiti."""
    C = LUTTO
    return grafica.BASE_CSS \
        .replace(grafica.BRAND["colori"]["carta"], "__CARTA__") \
        .replace(grafica.BRAND["colori"]["inchiostro"], C["inchiostro"]) \
        .replace("__CARTA__", C["carta"]) \
        .replace(grafica.BRAND["colori"]["rosso"], C["rosso"]) \
        .replace("opacity:.06", "opacity:.10")


if __name__ == "__main__":
    print(f"caption: {lunghezza_instagram(CAPTION)} caratteri (limite 2200)")
    genera(QUI.parent / "assets")
