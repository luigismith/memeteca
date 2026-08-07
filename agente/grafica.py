# -*- coding: utf-8 -*-
"""
MEMETECA — generatore degli asset grafici.
Ogni scheda produce un carosello di 3 slide 1080x1350 (4:5).
Le immagini sono ORIGINALI (tipografiche): nessun materiale protetto da copyright
viene ricaricato, il che rende la pagina pubblicabile senza rischi di takedown.
"""

# Console Windows in cp1252: senza questo, un accento fa morire lo script.
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")
import base64
import html
import pathlib
import re

from playwright.sync_api import sync_playwright

from contenuti import BRAND

QUI = pathlib.Path(__file__).parent
FONT_DIR = QUI / "fonts"
W, H = 1080, 1350

C = BRAND["colori"]

# Riduce il corpo tipografico finché il testo non entra nel suo contenitore.
AUTOFIT = """
() => {
  document.querySelectorAll('[data-fit]').forEach(el => {
    let size = parseFloat(el.dataset.fit);
    const min = parseFloat(el.dataset.min || '16');
    el.style.fontSize = size + 'px';
    let guard = 0;
    while ((el.scrollHeight > el.clientHeight + 1 || el.scrollWidth > el.clientWidth + 1)
           && size > min && guard < 400) {
      size -= 1; guard++;
      el.style.fontSize = size + 'px';
    }
    // il box smette di essere una gabbia e si stringe sul testo reale
    el.style.height = 'auto';
    el.style.maxHeight = 'none';
  });
  return true;
}
"""


def _font(nome):
    dati = base64.b64encode((FONT_DIR / nome).read_bytes()).decode()
    return f"url(data:font/woff2;base64,{dati}) format('woff2')"


def _css_fonts():
    faces = [
        ("Archivo", 400, "archivo-latin-400-normal.woff2"),
        ("Archivo", 500, "archivo-latin-500-normal.woff2"),
        ("Archivo", 700, "archivo-latin-700-normal.woff2"),
        ("Archivo", 900, "archivo-latin-900-normal.woff2"),
        ("Space Grotesk", 400, "space-grotesk-latin-400-normal.woff2"),
        ("Space Grotesk", 500, "space-grotesk-latin-500-normal.woff2"),
        ("Space Grotesk", 700, "space-grotesk-latin-700-normal.woff2"),
        ("Instrument Serif", 400, "instrument-serif-latin-400-normal.woff2"),
    ]
    out = "".join(
        f"@font-face{{font-family:'{f}';font-weight:{w};font-style:normal;src:{_font(n)};}}"
        for f, w, n in faces
    )
    out += (
        "@font-face{font-family:'Instrument Serif';font-weight:400;font-style:italic;"
        f"src:{_font('instrument-serif-latin-400-italic.woff2')};}}"
    )
    return out


GRANA = (
    "url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'>"
    "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4'/>"
    "<feColorMatrix type='saturate' values='0'/></filter>"
    "<rect width='220' height='220' filter='url(%23n)' opacity='0.5'/></svg>\")"
)


def _taglia(testo, limite):
    """Tronca al confine di frase più vicino sotto il limite."""
    testo = (testo or "").strip()
    if len(testo) <= limite:
        return testo
    pezzo = testo[:limite]
    for sep in (". ", "; ", " — ", ", "):
        i = pezzo.rfind(sep)
        if i > limite * 0.55:
            return pezzo[: i + 1].rstrip(" ,;—")
    return pezzo.rsplit(" ", 1)[0] + "…"


def _e(t):
    """Escape + corsivo per le virgolette caporali."""
    t = html.escape(t or "")
    return re.sub(r"«([^»]*)»", r"<i>«\1»</i>", t)


BASE_CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box;}}
{_css_fonts()}
body{{width:{W}px;height:{H}px;overflow:hidden;
  font-family:'Space Grotesk',sans-serif;color:{C['inchiostro']};
  background:{C['carta']};-webkit-font-smoothing:antialiased;}}
.slide{{position:relative;width:{W}px;height:{H}px;padding:72px 76px;
  display:flex;flex-direction:column;}}
.grana{{position:absolute;inset:0;background-image:{GRANA};opacity:.06;
  pointer-events:none;mix-blend-mode:multiply;}}
.vignetta{{position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(115% 85% at 50% 0%,rgba(0,0,0,0) 52%,rgba(20,17,15,.10) 100%);}}
.z{{position:relative;z-index:2;}}
.testata{{display:flex;justify-content:space-between;align-items:center;
  border-bottom:3px solid {C['inchiostro']};padding-bottom:15px;
  font-weight:700;font-size:21px;letter-spacing:.22em;text-transform:uppercase;}}
.testata .marchio{{font-family:'Archivo';font-weight:900;letter-spacing:.16em;}}
.testata .num{{color:{C['rosso']};}}
.pie{{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;
  border-top:3px solid {C['inchiostro']};padding-top:17px;
  font-size:18px;letter-spacing:.12em;text-transform:uppercase;font-weight:500;
  color:{C['grigio']};}}
.pie b{{color:{C['inchiostro']};letter-spacing:.18em;}}
i{{font-family:'Instrument Serif';font-style:italic;font-size:1.05em;}}
.etichetta{{font-family:'Archivo';font-weight:900;font-size:19px;letter-spacing:.2em;
  text-transform:uppercase;color:{C['rosso']};margin-bottom:12px;}}
.chip{{display:inline-block;background:{C['rosso']};color:{C['carta']};
  font-family:'Archivo';font-weight:900;font-size:20px;letter-spacing:.2em;
  padding:11px 19px 9px;text-transform:uppercase;}}
.titolone{{font-family:'Archivo';font-weight:900;line-height:.86;
  letter-spacing:-.03em;text-transform:uppercase;overflow:hidden;display:block;
  /* aria a destra: con la crenatura negativa i grotteschi pesanti
     arrivano a filo del bordo e sembrano tagliati */
  padding-right:26px;}}
.serif{{font-family:'Instrument Serif';line-height:1.2;overflow:hidden;}}
.anno-fantasma{{position:absolute;right:-34px;bottom:96px;z-index:1;
  font-family:'Archivo';font-weight:900;font-size:320px;line-height:.8;
  color:{C['inchiostro']};opacity:.042;letter-spacing:-.04em;}}
.corpo{{line-height:1.4;overflow:hidden;font-weight:400;}}

/* Il «reperto»: un frammento dell'originale, o una sua ricostruzione tipografica.
   Sta nella parte alta della copertina, dove prima c'era il vuoto. */
.reperto{{position:relative;z-index:2;border:3px solid {C['inchiostro']};
  background:{C['carta_scura']};padding:26px 30px 24px;margin-top:34px;
  max-width:900px;}}
.reperto .bollo{{position:absolute;top:-13px;left:24px;background:{C['rosso']};
  color:{C['carta']};font-family:'Archivo';font-weight:900;font-size:16px;
  letter-spacing:.2em;text-transform:uppercase;padding:5px 12px 4px;}}
.reperto .fonte{{margin-top:16px;font-size:17px;line-height:1.4;
  color:{C['grigio']};}}
.lemma{{font-family:'Instrument Serif';font-size:52px;line-height:1.15;}}
.lemma b{{font-family:'Archivo';font-weight:900;font-size:.78em;
  letter-spacing:-.01em;}}
.lemma i{{font-size:.62em;color:{C['grigio']};}}
.reperto img{{display:block;width:100%;height:auto;border:2px solid {C['inchiostro']};}}
"""


def _reperto(m):
    """Blocco facoltativo in copertina.

    Tre forme, in ordine di preferenza:
      lemma      la voce di dizionario, per i meme entrati nei vocabolari
      citazione  la frase originale, trattata come reperto tipografico
      immagine   un fotogramma o uno screenshot reale, che va fornito a mano
                 (vedi docs/08_REPERTI.md: breve, attribuito, art. 70 L. 633/1941)
    """
    r = m.get("reperto")
    if not r:
        return ""
    tipo = r.get("tipo")

    if tipo == "immagine":
        percorso = FONT_DIR.parent.parent / "reperti" / r["file"]
        if not percorso.exists():           # niente file, niente reperto
            return ""
        dati = base64.b64encode(percorso.read_bytes()).decode()
        mime = "image/png" if percorso.suffix.lower() == ".png" else "image/jpeg"
        dentro = f'<img src="data:{mime};base64,{dati}" alt="">'
    elif tipo == "lemma":
        dentro = (f'<div class="lemma"><b>{_e(r["voce"])}</b> '
                  f'<i>{_e(r["grammatica"])}</i><br>{_e(r["definizione"])}</div>')
    else:
        dentro = (f'<div class="serif" data-fit="46" data-min="28" '
                  f'style="height:190px;">{_e(r["testo"])}</div>')

    return (f'<div class="reperto"><span class="bollo">{_e(r.get("bollo", "Reperto"))}'
            f'</span>{dentro}'
            f'<div class="fonte">{_e(r["fonte"])}</div></div>')


def slide_copertina(m):
    return f"""<div class="slide">
  <div class="grana"></div><div class="vignetta"></div>
  <div class="anno-fantasma">{_e(m['anno'])}</div>
  <div class="testata z"><span class="marchio">{BRAND['nome']}</span>
    <span class="num">Scheda n. {m['num']}</span></div>
  <div class="z" style="margin-top:56px;"><span class="chip">{_e(m['categoria'])}</span></div>
  {_reperto(m)}
  <div class="z" style="flex:1;min-height:44px;"></div>
  <div class="z titolone" data-fit="164" data-min="44"
       style="height:430px;">{_e(m['titolo'])}</div>
  <div class="z" style="width:180px;height:9px;background:{C['inchiostro']};margin:42px 0 32px;"></div>
  <div class="z serif" data-fit="56" data-min="30"
       style="height:200px;max-width:880px;margin-bottom:54px;">{_e(m['occhiello'])}</div>
  <div class="z corpo" data-fit="27" data-min="20"
       style="height:130px;max-width:880px;color:{C['inchiostro']};opacity:.78;
              border-left:5px solid {C['rosso']};padding-left:22px;margin-bottom:30px;"
       >{_e(_taglia(m['hook'], 190))}</div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span>
    <span>Scorri &nbsp;›&nbsp;›&nbsp;›</span></div>
</div>"""


def slide_scheda(m):
    righe = [
        ("Prima apparizione", _taglia(m["prima_apparizione"], 230), 200),
        ("Creatore", _taglia(m["creatore"], 230), 200),
        ("Origini", _taglia(m["origini"], 330), 250),
        ("Come è diventato meme", _taglia(m["storia"], 330), 250),
    ]
    blocchi = ""
    for et, txt, h in righe:
        blocchi += f"""<div>
      <div class="etichetta">{et}</div>
      <div class="corpo" data-fit="31" data-min="19" style="height:{h}px;">{_e(txt)}</div></div>"""
    return f"""<div class="slide">
  <div class="grana"></div><div class="vignetta"></div>
  <div class="testata z"><span class="marchio">{BRAND['nome']}</span>
    <span class="num">Scheda n. {m['num']}</span></div>
  <!-- Instagram può far partire il carosello dalla slide 2 («seconda chance»):
       quindi la 2 deve reggere da sola, con il nome del meme in evidenza. -->
  <div class="z etichetta" style="margin:32px 0 6px;">La scheda</div>
  <h2 class="z titolone" data-fit="66" data-min="38"
      style="height:150px;flex:none;margin-bottom:22px;">{_e(m['titolo'])}</h2>
  <div class="z" style="flex:1;display:flex;flex-direction:column;
       justify-content:space-between;padding-bottom:22px;">{blocchi}</div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span><span>{_e(m['anno'])}</span></div>
</div>"""


def slide_significato(m):
    sig = _taglia(m["significato"], 340)
    chi = _taglia(m["chicca"], 320)
    dopo = _taglia(m["dopo"], 240)
    return f"""<div class="slide">
  <div class="grana"></div><div class="vignetta"></div>
  <div class="testata z"><span class="marchio">{BRAND['nome']}</span>
    <span class="num">Scheda n. {m['num']}</span></div>
  <div class="z" style="flex:1;display:flex;flex-direction:column;
       justify-content:space-between;padding:38px 0 22px;">
    <div>
      <div class="etichetta">Cosa significa</div>
      <div class="serif" data-fit="54" data-min="30" style="height:330px;">{_e(sig)}</div>
    </div>
    <div style="background:{C['inchiostro']};color:{C['carta']};padding:34px 38px;">
      <div style="font-family:'Archivo';font-weight:900;font-size:19px;letter-spacing:.2em;
        text-transform:uppercase;opacity:.6;margin-bottom:14px;">La chicca</div>
      <div class="corpo" data-fit="30" data-min="20" style="height:170px;">{_e(chi)}</div>
    </div>
    <div>
      <div class="etichetta">Cos'è successo dopo</div>
      <div class="corpo" data-fit="28" data-min="19" style="height:150px;">{_e(dopo)}</div>
    </div>
    <div style="font-size:18px;line-height:1.5;color:{C['grigio']};">
      Fonti verificate: {_e(' · '.join(m['fonti']))}</div>
  </div>
  <div class="pie z"><span><b>{BRAND['handle']}</b></span>
    <span>{_e(BRAND['payoff'])}</span></div>
</div>"""


SLIDES = [slide_copertina, slide_scheda, slide_significato]


def genera(memi, cartella):
    """Renderizza tutte le slide. Ritorna {num: [percorsi]}."""
    cartella = pathlib.Path(cartella)
    cartella.mkdir(parents=True, exist_ok=True)
    risultati = {}
    with sync_playwright() as p:
        br = p.chromium.launch(args=["--force-color-profile=srgb"])
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for m in memi:
            percorsi = []
            for i, fn in enumerate(SLIDES, start=1):
                doc = f"<!doctype html><meta charset='utf-8'><style>{BASE_CSS}</style>{fn(m)}"
                pg.set_content(doc, wait_until="load")
                pg.evaluate(AUTOFIT)
                pg.wait_for_timeout(60)
                out = cartella / f"{m['num']}_{i}.jpg"
                pg.screenshot(path=str(out), type="jpeg", quality=93)
                percorsi.append(str(out))
            risultati[m["num"]] = percorsi
            print(f"  ✓ scheda {m['num']} — {m['titolo']}")
        br.close()
    return risultati


if __name__ == "__main__":
    import sys
    from contenuti import MEMI

    dest = sys.argv[1] if len(sys.argv) > 1 else str(QUI.parent / "assets")
    genera(MEMI, dest)
