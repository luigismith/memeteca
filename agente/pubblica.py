# -*- coding: utf-8 -*-
"""
MEMETECA — orchestratore.

    python pubblica.py genera            # rigenera tutte le slide in ../assets
    python pubblica.py esporta           # scrive calendario + caption in ../docs
    python pubblica.py prossimo          # mostra la prossima scheda in coda
    python pubblica.py pubblica          # pubblica la prossima scheda su Instagram
    python pubblica.py pubblica --prova  # simula, senza chiamare le API

Lo stato (che cosa è già uscito) sta in `stato.json`, accanto a questo file:
è l'unica cosa che va conservata fra un'esecuzione e l'altra.
"""

# Console Windows in cp1252: senza questo, un accento fa morire lo script.
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")
import argparse
import datetime as dt
import json
import os
import pathlib
import sys

from contenuti import (BRAND, LIMITE_INSTAGRAM, MARGINE, MEMI, ORARI,
                       SCHEDE_AL_GIORNO,
                       calendario, coda, costruisci_caption, lunghezza_instagram)

QUI = pathlib.Path(__file__).parent
ASSETS = QUI.parent / "assets"
DOCS = QUI.parent / "docs"
STATO = QUI / "stato.json"

GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]


# ─────────────────────────────────────────────────────────────────── stato
def leggi_stato():
    if STATO.exists():
        return json.loads(STATO.read_text(encoding="utf-8"))
    return {"pubblicate": [], "storico": []}


def salva_stato(s):
    STATO.write_text(json.dumps(s, ensure_ascii=False, indent=2), encoding="utf-8")


def fuso_italiano():
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo("Europe/Rome")
    except Exception:                      # runner senza tzdata
        return dt.timezone(dt.timedelta(hours=2))


def oggi_italiano():
    return dt.datetime.now(fuso_italiano()).date().isoformat()


def uscite_di_oggi():
    """Quante schede della collana sono gia' uscite oggi (ora italiana).
    I post fuori collana non contano: hanno un budget loro."""
    oggi = oggi_italiano()
    n = 0
    for v in leggi_stato().get("storico", []):
        if v.get("num") == "fuori collana":
            continue
        quando = str(v.get("quando", ""))
        if quando.startswith(oggi):
            n += 1
    return n


def prossima_scheda():
    """La prima della coda non ancora pubblicata (la coda tiene la domenica
    monografica anche se la frequenza giornaliera cambia)."""
    fatte = set(leggi_stato()["pubblicate"])
    per_num = {m["num"]: m for m in MEMI}
    for num in coda(fatte):
        if num not in fatte:
            return per_num[num]
    return None


# ─────────────────────────────────────────────────────────────── operazioni
def cmd_genera(_):
    import grafica
    grafica.genera(MEMI, ASSETS)
    print(f"\n{len(MEMI) * 3} slide in {ASSETS}")


def cmd_esporta(_):
    DOCS.mkdir(parents=True, exist_ok=True)

    # calendario
    GIORNI_IT = ["lunedì", "martedì", "mercoledì", "giovedì",
                 "venerdì", "sabato", "domenica"]
    righe = ["# MEMETECA — calendario editoriale", "",
             f"**{BRAND['handle']}** · {BRAND['payoff']}", "",
             f"Slot: {', '.join(ORARI)}. Due schede al giorno, la terza uscita "
             "solo se c'è una notizia che l'archivio può illuminare.",
             "La domenica è monografica: TV e pubblicità.", "",
             "Questo calendario è **indicativo**: l'ordine è quello della coda, "
             "ma ogni slot lo decide la sessione guardando prima le notizie "
             "(vedi `03_AGENTE_AUTONOMO.md`).", "",
             "| Data | Ora | N. | Scheda | Categoria |",
             "|---|---|---|---|---|"]
    fatte = set(leggi_stato()["pubblicate"])
    domani = (dt.date.today() + dt.timedelta(days=1)).isoformat()
    for data, ora, m in calendario(esclusi=fatte, inizio=domani)[:20]:
        righe.append(f"| {GIORNI_IT[data.weekday()]} {data.strftime('%d/%m')} | {ora} | "
                     f"{m['num']} | **{m['titolo']}** | {m['categoria']} |")
    (DOCS / "01_CALENDARIO.md").write_text("\n".join(righe) + "\n", encoding="utf-8")

    # caption
    out = ["# MEMETECA — le 21 caption della settimana 1", "",
           "Ogni caption sta sotto il limite Instagram di 2.200 caratteri.",
           "Copia e incolla, oppure lascia fare allo script di pubblicazione.", ""]
    for m in MEMI:
        c = costruisci_caption(m)
        out += [f"---", "",
                f"## {m['num']} · {m['titolo']}",
                f"*{m['categoria']} — "
                f"{lunghezza_instagram(c)} caratteri — affidabilità fonti: {m['confidenza']}*", "",
                "```", c, "```", ""]
    (DOCS / "02_CAPTION.md").write_text("\n".join(out), encoding="utf-8")
    print(f"Scritti {DOCS/'01_CALENDARIO.md'} e {DOCS/'02_CAPTION.md'}")


def cmd_prossimo(_):
    m = prossima_scheda()
    if not m:
        print("Coda esaurita: servono nuove schede.")
        return
    prima = calendario(esclusi=set(leggi_stato()["pubblicate"]),
                       inizio=(dt.date.today() + dt.timedelta(days=1)).isoformat())[0]
    print(f"Prossima: n. {m['num']} — {m['titolo']} "
          f"({prima[0].strftime('%d/%m')}, {prima[1]})")
    print(f"\n{costruisci_caption(m)}")


def cmd_pubblica(args):
    gia = uscite_di_oggi()
    if gia >= SCHEDE_AL_GIORNO and not args.forza:
        print(f"Oggi sono gia' uscite {gia} schede (tetto: {SCHEDE_AL_GIORNO}). "
              "Non pubblico: il terzo post esce solo se c'e' una notizia, "
              "e in quel caso e' un fuori collana.")
        return

    m = prossima_scheda()
    if not m:
        print("Coda esaurita: nessuna scheda da pubblicare.")
        sys.exit(2)

    base = (args.base_url or os.environ.get("MEMETECA_BASE_URL", "")).rstrip("/")
    urls = [f"{base}/{m['num']}_{i}.jpg" for i in (1, 2, 3)]
    caption = costruisci_caption(m)

    if args.prova:
        print(f"[PROVA] scheda {m['num']} — {m['titolo']}")
        for u in urls:
            print("  ", u)
        print(f"   caption: {lunghezza_instagram(caption)} caratteri "
          f"(limite Instagram {LIMITE_INSTAGRAM})")
        return

    if not base:
        sys.exit("Serve MEMETECA_BASE_URL (o --base-url): la Graph API scarica le "
                 "immagini da un URL pubblico, non accetta upload diretti.")

    from instagram import Instagram
    ig = Instagram()
    post_id = ig.pubblica_carosello(urls, caption)

    # LO STATO SI SALVA SUBITO, prima di qualunque altra cosa.
    # Il 7 agosto la 005 e' stata pubblicata e poi la run e' fallita sul commento
    # con le fonti: il post era online ma lo stato non lo sapeva, e la corsa
    # successiva l'avrebbe ripubblicata identica. Una volta che un post e' uscito
    # non si torna indietro, quindi registrarlo viene prima di tutto il resto.
    s = leggi_stato()
    s["pubblicate"].append(m["num"])
    s["storico"].append({"num": m["num"], "titolo": m["titolo"],
                         "post_id": post_id,
                         "quando": dt.datetime.now(dt.timezone.utc).isoformat()})
    salva_stato(s)
    print(f"Pubblicata scheda {m['num']} — {m['titolo']} (post {post_id})")

    # Il commento con le fonti e' un di piu': le fonti stanno gia' nella caption.
    # Se fallisce (per esempio perche' al token manca il permesso sui commenti)
    # lo diciamo e tiriamo dritto, senza far fallire una pubblicazione riuscita.
    try:
        ig.commenta(post_id, "Fonti verificate: " + " · ".join(m["fonti"]))
    except Exception as e:
        print(f"::warning::Commento con le fonti non pubblicato: {e}")


def main():
    p = argparse.ArgumentParser(description="MEMETECA")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("genera").set_defaults(fn=cmd_genera)
    sub.add_parser("esporta").set_defaults(fn=cmd_esporta)
    sub.add_parser("prossimo").set_defaults(fn=cmd_prossimo)
    pp = sub.add_parser("pubblica")
    pp.add_argument("--prova", action="store_true", help="simula senza chiamare le API")
    pp.add_argument("--base-url", help="URL pubblico della cartella assets")
    pp.add_argument("--forza", action="store_true",
                    help="pubblica anche se il tetto giornaliero e' gia' stato raggiunto")
    pp.set_defaults(fn=cmd_pubblica)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
