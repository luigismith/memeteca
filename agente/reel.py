# -*- coding: utf-8 -*-
"""
MEMETECA — il generatore di Reel.

Il carosello trattiene chi ci vede gia'. Il Reel e' l'unico formato che Instagram
distribuisce sistematicamente a chi NON ci segue: e' la sola leva di crescita a
freddo che possiamo produrre da soli.

Stessa identita' tipografica delle slide, formato verticale 1080x1920, ritmo
serrato: la prima battuta deve fermare il pollice entro il primo secondo.

    python reel.py 005            # genera ../assets/reel_005.mp4
    python reel.py 005 --battute  # stampa solo il testo delle battute

Il video esce COMPLETO di musica: la traccia originale di musica.py
(assets/musica_reel.wav, rigenerabile), sintetizzata da noi — quindi senza
diritti altrui ne' rights management. Se il wav manca viene messa una traccia
silenziosa. La codifica finale segue la ricetta validata con l'API dei Reel:
720x1280, H.264 main, GOP chiuso, niente B-frame, niente edit list.
"""

# Console Windows in cp1252: senza questo, un accento fa morire lo script.
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

from playwright.sync_api import sync_playwright

import grafica
from contenuti import BRAND, MEMI

QUI = pathlib.Path(__file__).parent
C = BRAND["colori"]

# Rendiamo piu' grandi del formato finale: lo zoom lento ritaglia dentro questo
# margine, cosi' il movimento non sgrana mai.
W, H = 1350, 2400
W_OUT, H_OUT = 720, 1280   # 1080x1920 a durata piena viene rifiutato dall'API
FPS = 30

# L'interfaccia di Instagram copre la fascia bassa e il bordo destro: il testo
# vive nell'80% centrale, altrimenti finisce sotto i pulsanti.
MARGINE_ALTO = 300
MARGINE_BASSO = 520


def _e(t):
    import html
    return html.escape(str(t))


def battute(m):
    """Le battute del Reel. Ognuna e' (etichetta, testo, secondi, stile).

    Il gancio si spezza in due: la prima frase ferma il pollice, la seconda e'
    la svolta. Tre frasi in una schermata sola non si leggono, si scorrono."""
    frasi = _frasi(m["hook"])
    amo = frasi[0]
    svolta = frasi[1] if len(frasi) > 1 else ""

    b = [("", amo, 3.4, "gancio")]
    if svolta:
        b.append(("", svolta, 3.0, "svolta"))
    b += [
        (m.get("categoria", ""), m["titolo"], 2.6, "titolo"),
        ("Prima apparizione", _taglia(m["prima_apparizione"], 150), 3.8, "corpo"),
        ("Chi l'ha fatto", _taglia(m["creatore"], 150), 3.8, "corpo"),
        ("La chicca", _taglia(m["chicca"], 165), 4.2, "corpo"),
        ("Cosa significa oggi", _taglia(m["significato"], 150), 3.8, "corpo"),
        ("", f"Scheda n. {m['num']}", 2.8, "chiusa"),
    ]
    return b


def _frasi(t):
    """Spezza in frasi senza inciampare nelle abbreviazioni con il punto."""
    t = " ".join(str(t).split())
    pezzi = re.split(r"(?<=[.!?])\s+(?=[A-ZÈÉÀÌÒÙ«])", t)
    return [x.strip() for x in pezzi if x.strip()]


def _taglia(t, limite):
    t = " ".join(str(t).split())
    if len(t) <= limite:
        return t
    tagliato = t[:limite]
    if "." in tagliato[limite // 2:]:
        return tagliato[:tagliato.rfind(".") + 1]
    return tagliato[:tagliato.rfind(" ")] + "…"


def _html(etichetta, testo, stile, m):
    corpi = {
        "gancio":  ("Archivo", 900, 96, 1.06, C["inchiostro"], C["carta"]),
        "svolta":  ("Archivo", 900, 96, 1.06, C["carta"], C["inchiostro"]),
        "titolo":  ("Archivo", 900, 132, 0.94, C["carta"], C["inchiostro"]),
        "corpo":   ("Archivo", 500, 58, 1.32, C["inchiostro"], C["carta"]),
        "chiusa":  ("Archivo", 700, 54, 1.2, C["carta"], C["inchiostro"]),
    }
    famiglia, peso, corpo, interlinea, colore, fondo = corpi[stile]
    maiuscolo = "text-transform:uppercase;letter-spacing:-.02em;" if stile == "titolo" else ""

    etichetta_html = (
        f'<div class="etichetta">{_e(etichetta)}</div>' if etichetta else ""
    )
    # nella chiusa il richiamo al profilo e' l'elemento principale
    if stile == "chiusa":
        centro = (f'<div class="handle">{_e(BRAND["handle"])}</div>'
                  f'<div class="payoff">l\'archivio ragionato del meme italiano</div>'
                  f'<div class="coda">{_e(testo)}</div>')
    else:
        minimo = {"titolo": 78, "gancio": 56, "svolta": 56}.get(stile, 34)
        centro = (f'<div class="testo" data-fit="{corpo}" data-min="{minimo}">'
                  f'{_e(testo)}</div>')

    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>
{grafica._css_fonts()}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  width:{W}px; height:{H}px; background:{fondo}; color:{colore};
  font-family:'Archivo',sans-serif;
  display:flex; flex-direction:column; justify-content:center;
  padding:{MARGINE_ALTO}px 110px {MARGINE_BASSO}px 110px;
}}
.etichetta {{
  font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:34px;
  letter-spacing:.22em; text-transform:uppercase;
  color:{C['rosso']}; margin-bottom:44px;
}}
.testo {{
  font-family:'{famiglia}',sans-serif; font-weight:{peso};
  font-size:{corpo}px; line-height:{interlinea}; {maiuscolo}
  max-height:{H - MARGINE_ALTO - MARGINE_BASSO - 120}px; overflow:hidden;
  padding-right:26px;
}}
.handle {{ font-family:'Space Grotesk',sans-serif; font-weight:700;
  font-size:76px; letter-spacing:-.01em; }}
.payoff {{ font-family:'Instrument Serif',serif; font-style:italic;
  font-size:52px; color:{C['grigio']}; margin-top:26px; }}
.coda {{ font-family:'Space Grotesk',sans-serif; font-size:34px;
  letter-spacing:.16em; text-transform:uppercase;
  color:{C['rosso']}; margin-top:70px; }}
.filo {{ position:absolute; left:110px; right:110px; height:5px;
  background:{C['rosso']}; }}
.alto {{ top:{MARGINE_ALTO - 70}px; }}
.marchio {{ position:absolute; left:110px; bottom:{MARGINE_BASSO - 90}px;
  font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:32px;
  letter-spacing:.24em; color:{colore}; opacity:.55; }}
</style></head><body>
<div class="filo alto"></div>
{etichetta_html}
{centro}
<div class="marchio">MEMETECA</div>
</body></html>"""


def _fotogrammi(m, cartella):
    """Una PNG per battuta."""
    fatti = []
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={"width": W, "height": H},
                         device_scale_factor=1)
        for i, (etichetta, testo, secondi, stile) in enumerate(battute(m), 1):
            pg.set_content(_html(etichetta, testo, stile, m))
            pg.evaluate(grafica.AUTOFIT)
            f = cartella / f"b{i:02d}.png"
            pg.screenshot(path=str(f))
            fatti.append((f, secondi))
            print(f"  battuta {i}/{len(battute(m))}")
        br.close()
    return fatti


def _clip(png, secondi, dest):
    """Zoom lentissimo: il movimento tiene l'occhio, senza distrarre."""
    n = int(secondi * FPS)
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-loop", "1", "-framerate", str(FPS), "-i", str(png),
        "-vf", (f"zoompan=z='min(zoom+0.00035,1.09)':d={n}"
                f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                f":s={W_OUT}x{H_OUT}:fps={FPS},format=yuv420p"),
        "-t", f"{secondi}", "-c:v", "libx264", "-preset", "medium",
        "-crf", "18", str(dest),
    ], check=True)


def genera(m, cartella):
    cartella = pathlib.Path(cartella)
    cartella.mkdir(parents=True, exist_ok=True)
    uscita = cartella / f"reel_{m['num']}.mp4"

    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        clip = []
        for i, (png, secondi) in enumerate(_fotogrammi(m, tmp), 1):
            c = tmp / f"c{i:02d}.mp4"
            _clip(png, secondi, c)
            clip.append(c)

        elenco = tmp / "elenco.txt"
        elenco.write_text("".join(f"file '{c}'\n" for c in clip), encoding="utf-8")

        muto = tmp / "muto.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat",
                        "-safe", "0", "-i", str(elenco), "-c", "copy", str(muto)],
                       check=True)

        musica = cartella / "musica_reel.wav"
        sorgente_audio = (["-i", str(musica)] if musica.exists()
                          else ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"])
        con_audio = tmp / "con_audio.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(muto),
            *sorgente_audio, "-map", "0:v", "-map", "1:a",
            "-c:v", "libx264", "-profile:v", "main", "-pix_fmt", "yuv420p",
            "-crf", "21", "-r", str(FPS), "-g", "60", "-sc_threshold", "0",
            "-bf", "0", "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
            "-ac", "2", "-af", "aresample=first_pts=0", "-shortest",
            "-movflags", "+faststart", str(con_audio),
        ], check=True)
        # remux senza edit list: l'API dei Reel li rifiuta
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(con_audio),
            "-c", "copy", "-movflags", "+faststart", "-use_editlist", "0",
            str(uscita),
        ], check=True)

    return uscita


def _durata(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", str(f)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: python reel.py <numero scheda> [--battute]")
    num = sys.argv[1].zfill(3)
    m = next((x for x in MEMI if x["num"] == num), None)
    if not m:
        sys.exit(f"scheda {num} non trovata")

    if "--battute" in sys.argv:
        for i, (et, t, s, st) in enumerate(battute(m), 1):
            print(f"[{i}] {s:.1f}s · {st}" + (f" · {et}" if et else ""))
            print(f"    {t}\n")
        tot = sum(s for _, _, s, _ in battute(m))
        print(f"durata totale: {tot:.1f}s")
    else:
        if not shutil.which("ffmpeg"):
            sys.exit("serve ffmpeg")
        f = genera(m, QUI.parent / "assets")
        print(f"\n{f}  ({_durata(f):.1f}s)")
