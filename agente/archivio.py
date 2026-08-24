# -*- coding: utf-8 -*-
"""
MEMETECA — il sito-archivio pubblico.

Genera ../index.html per GitHub Pages: l'archivio completo delle schede,
consultabile e linkabile, con il rimando al profilo Instagram. È il canale
di crescita gratuito: chi cerca l'origine di un meme italiano trova la
scheda, e da lì la pagina.

    python archivio.py
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import html
import json
import pathlib

from contenuti import BRAND, MEMI

# Sul sito vanno SOLO le schede gia' uscite su Instagram: il repository e'
# pubblico e la coda di domani non deve fare spoiler.
_stato = json.loads((pathlib.Path(__file__).parent / "stato.json")
                    .read_text(encoding="utf-8"))
USCITE = [m for m in MEMI if m["num"] in set(_stato.get("pubblicate", []))]

QUI = pathlib.Path(__file__).parent
IG = "https://www.instagram.com/memeteca_italiana/"


def _e(t):
    return html.escape(str(t))


def carta(m):
    return f"""<article class="carta">
  <a href="{IG}" target="_blank" rel="noopener">
    <img src="assets/{m['num']}_1.jpg" alt="{_e(m['titolo'])} — scheda {m['num']}" loading="lazy">
  </a>
  <div class="carta-testo">
    <span class="cat">{_e(m.get('categoria', ''))}</span>
    <h2>{_e(m['titolo'])}</h2>
    <p>{_e(m['occhiello'])}</p>
  </div>
</article>"""


def genera():
    schede = "\n".join(carta(m) for m in reversed(USCITE))
    n = len(USCITE)
    pagina = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MEMETECA — l'archivio ragionato del meme italiano</title>
<meta name="description" content="Chi l'ha fatto, quando è apparso, cosa significa: {n} schede sui meme italiani, ogni affermazione su due fonti verificate.">
<meta property="og:title" content="MEMETECA — l'archivio ragionato del meme italiano">
<meta property="og:description" content="{n} schede verificate: chi, quando, perché. Le fonti in fondo a ogni post.">
<meta property="og:image" content="https://luigismith.github.io/memeteca/assets/manifesto_1.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;900&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {{ --carta:#EFE7D8; --inchiostro:#14110F; --rosso:#C8402E; --grigio:#6E6558; }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:var(--carta); color:var(--inchiostro);
         font-family:'Space Grotesk',sans-serif; }}
  header {{ max-width:1100px; margin:0 auto; padding:64px 24px 40px; }}
  .marchio {{ font-family:'Archivo'; font-weight:900; font-size:clamp(42px,8vw,96px);
              letter-spacing:-.03em; line-height:.9; text-transform:uppercase; }}
  .filo {{ height:5px; background:var(--rosso); margin:26px 0; }}
  .payoff {{ font-size:clamp(16px,2.4vw,22px); max-width:640px; line-height:1.45; }}
  .payoff b {{ color:var(--rosso); }}
  .cta {{ display:inline-block; margin-top:26px; background:var(--inchiostro);
          color:var(--carta); text-decoration:none; font-family:'Archivo';
          font-weight:700; padding:14px 26px; letter-spacing:.06em;
          text-transform:uppercase; font-size:14px; }}
  .cta:hover {{ background:var(--rosso); }}
  main {{ max-width:1100px; margin:0 auto; padding:16px 24px 80px;
          display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr));
          gap:28px; }}
  .carta img {{ width:100%; display:block; border:1px solid rgba(20,17,15,.15); }}
  .carta-testo {{ padding:12px 2px; }}
  .cat {{ font-size:11px; letter-spacing:.18em; text-transform:uppercase;
          color:var(--rosso); font-weight:700; }}
  .carta h2 {{ font-family:'Archivo'; font-weight:900; font-size:20px;
               text-transform:uppercase; letter-spacing:-.01em; margin:4px 0; }}
  .carta p {{ font-size:14px; color:var(--grigio); line-height:1.4; }}
  footer {{ border-top:1px solid rgba(20,17,15,.2); padding:40px 24px 60px; }}
  footer .dentro {{ max-width:1100px; margin:0 auto; font-size:14px;
                    color:var(--grigio); line-height:1.6; max-width:640px; }}
  footer a {{ color:var(--rosso); }}
</style>
</head>
<body>
<header>
  <div class="marchio">Memeteca</div>
  <div class="filo"></div>
  <p class="payoff">L'archivio ragionato del meme italiano. Chi l'ha fatto,
  quando è apparso la prima volta, cosa significa oggi — <b>ogni affermazione
  su almeno due fonti verificate</b>, scritte in fondo a ogni post.
  {n} schede, due al giorno.</p>
  <a class="cta" href="{IG}" target="_blank" rel="noopener">Seguici su Instagram →</a>
</header>
<main>
{schede}
</main>
<footer><div class="dentro">
  <p><b>Il metodo.</b> Se un meme non regge alla verifica, non esce: nella
  prima settimana abbiamo scartato più di cinquanta candidati su settantuno.
  Non ripubblichiamo il materiale di nessuno: ogni slide è scritta qui.</p>
  <p style="margin-top:14px;">Le schede escono su
  <a href="{IG}">@memeteca_italiana</a>.</p>
</div></footer>
</body>
</html>"""
    dest = QUI.parent / "index.html"
    dest.write_text(pagina, encoding="utf-8", newline="\n")
    print(f"{dest} — {n} schede")


if __name__ == "__main__":
    genera()
