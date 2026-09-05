# -*- coding: utf-8 -*-
"""
MEMETECA — pubblica il Reel di una scheda via API.

Il video sta in assets/reel_<num>.mp4 nel repository (servito da GitHub
Pages) e contiene gia' la traccia musicale originale generata da musica.py:
niente libreria di Instagram, niente rights management.

    python pubblica_reel.py 021
"""
import sys as _sys
for _f in (_sys.stdout, _sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

import datetime as dt
import json
import os
import pathlib
import sys

import requests

from contenuti import BRAND, MEMI
from instagram import Instagram

QUI = pathlib.Path(__file__).parent
STATO = QUI / "stato.json"
# 29 agosto 2026: era "_v5", e non serviva a niente.
#
# Il suffisso nasceva dalla teoria dei «percorsi bruciati»: si credeva che
# Meta ricordasse gli URL falliti e li rifiutasse per sempre, ignorando la
# query string, quindi a ogni tentativo si ricopiava lo stesso video su un
# nome nuovo — _v2, _v3, _v4, _v5. Erano tutti rifiutati, e la conclusione
# era sempre «anche questo percorso e' bruciato».
#
# La causa vera era un'altra: l'URL costruito da MEMETECA_BASE_URL rispondeva
# 404, e l'API segnala un download fallito con lo stesso ERROR nudo di un file
# malformato. Nessun percorso e' mai stato bruciato: erano tutti sbagliati
# allo stesso modo. Cambiare nome al file non poteva funzionare, e in quattro
# giorni di tentativi non ha mai funzionato.
#
# Ora i video si chiamano come li scrive reel.py, e basta. Le tre versioni
# vecchie restano in assets solo perche' i reel 021, 022 e 026 sono stati
# pubblicati da quei file: non se ne creano altre.
SUFFISSO_FILE = ""


def caption_reel(m):
    """Breve, diversa dal carosello: gancio, richiamo, 5 hashtag."""
    return (f"{m['hook']}\n\n"
            f"La scheda completa — date, fonti e cos'e' successo dopo — "
            f"e' sul profilo.\n\n"
            f"Segui {BRAND['handle']}\n\n"
            f"{m['hashtags']}")


def url_possibili(num):
    """Gli URL da provare per il video, in ordine.

    30 agosto 2026, la spiegazione esatta del 404 che per quattro giorni ha
    fatto fallire i Reel. MEMETECA_BASE_URL **include gia' `/assets`**: si
    vede in pubblica.py, che costruisce le immagini come `{base}/{num}_1.jpg`
    senza aggiungere niente. Qui invece si scriveva `{base}/assets/reel_...`,
    e l'indirizzo diventava `.../assets/assets/reel_021.mp4`. Un 404, sempre.

    Per questo le immagini funzionavano e i video no, con lo stesso segreto e
    lo stesso token: non era il tipo di file, era una cartella di troppo. E
    per questo nessuna delle ipotesi tentate poteva reggere — budget video,
    percorsi bruciati, formato del file, account non abilitato: l'URL non
    esisteva e basta, e la Graph API lo segnala con lo stesso ERROR nudo che
    userebbe per un video malformato.

    Si prova comunque piu' di un indirizzo, e si sceglie quello che risponde
    200: il segreto non e' leggibile da qui, quindi non si puo' sapere con
    certezza come e' fatto, e una verifica costa una HEAD."""
    base = os.environ.get("MEMETECA_BASE_URL", "").rstrip("/")
    nome = f"reel_{num}{SUFFISSO_FILE}.mp4"
    urls = []
    if base:
        urls.append(f"{base}/{nome}")          # base che include gia' /assets
        urls.append(f"{base}/assets/{nome}")   # base che si ferma alla radice
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if "/" in repo:
        utente, nome_repo = repo.split("/", 1)
        urls.append(f"https://{utente}.github.io/{nome_repo}/assets/{nome}")
    return list(dict.fromkeys(urls))


def scegli_url(num):
    """Il primo URL che risponde davvero 200."""
    ultimo = None
    for video in url_possibili(num):
        r = requests.head(video, timeout=30, allow_redirects=True)
        print(f"provo {video} → HTTP {r.status_code}")
        if r.status_code == 200:
            return video
        ultimo = r.status_code
    sys.exit(f"nessun indirizzo serve reel_{num}{SUFFISSO_FILE}.mp4 "
             f"(ultima risposta {ultimo}): il file e' su Pages? "
             f"il push e' arrivato?")


def controlla_online(video):
    """Il video DEVE rispondere 200 prima di chiamare l'API.

    27 agosto 2026: quattro giorni di Reel finiti in `{'status': 'ERROR'}`
    nudo, senza codice e senza messaggio. Quando l'URL non e' raggiungibile,
    la Graph API non lo dice: crea il contenitore, prova a scaricare, e
    fallisce con lo stesso ERROR generico che darebbe un file malformato.
    Non c'e' modo di distinguere le due cose dall'API — quindi si distingue
    prima, da qui.

    La stessa regola vale per le immagini (GitHub Pages ci mette un minuto a
    distribuire un file appena pushato), ma sui video costa molto di piu':
    un carosello sbagliato lo vedi, un reel no."""
    r = requests.head(video, timeout=30, allow_redirects=True)
    print(f"video: {video} → HTTP {r.status_code} "
          f"{r.headers.get('content-type','?')} "
          f"{r.headers.get('content-length','?')} byte")
    if r.status_code != 200:
        sys.exit(f"il video non e' raggiungibile ({r.status_code}): "
                 f"controlla MEMETECA_BASE_URL e che il file sia su Pages")


# 5 settembre 2026 — la stessa distrazione, la seconda volta. Il commit che
# ha introdotto scatto.txt fece partire il cordone delle schede da solo; il
# commit che ha introdotto scatto_reel.txt ha fatto partire il cordone dei
# reel, con dentro gia' il numero 001, sette minuti dopo il reel 020. Due
# reel a distanza di sette minuti sono esattamente cio' che il 6 agosto e'
# costato un blocco morbido. L'ho annullata dieci secondi dopo la partenza,
# prima del passo di pubblicazione: nessun reel e' uscito.
#
# REGOLA: un file che innesca qualcosa lo innesca anche il giorno in cui
# nasce. Ma la vera lezione e' un'altra, perche' la prima volta la lezione
# «attento al commit» non e' bastata a evitare la seconda: se la sicurezza
# dipende dal fatto che io mi ricordi qualcosa, prima o poi salta. Quindi il
# freno non sta nel cordone, sta qui — dove si pubblica, e vale per tutte le
# strade, dispatch compreso.
ORA_MINIMA, ORA_MASSIMA = 11, 21
DISTANZA_MINIMA_ORE = 4


def fuso_italiano():
    from pubblica import fuso_italiano as _f
    return _f()


def troppo_presto(s):
    """Ritorna il motivo per cui non si deve pubblicare adesso, o None.

    Due freni, gli stessi delle schede:
      · la fascia 11:00-21:00 italiane, perche' una corsa in ritardo non
        deve far uscire un post di notte;
      · quattro ore dall'ultima uscita, reel o scheda che sia, perche' due
        pubblicazioni ravvicinate sono quello che il 6 agosto 2026 ha
        fatto scattare un blocco morbido dopo quattro post di fila."""
    adesso = dt.datetime.now(dt.timezone.utc)
    ora = adesso.astimezone(fuso_italiano())
    if not (ORA_MINIMA <= ora.hour < ORA_MASSIMA):
        return (f"sono le {ora:%H:%M} italiane, fuori dalla fascia "
                f"{ORA_MINIMA}:00-{ORA_MASSIMA}:00")
    ultime = []
    for r in s.get("reel", []):
        if r.get("quando"):
            ultime.append(("reel " + r.get("num", "?"), r["quando"]))
    for r in s.get("storico", []):
        if isinstance(r, dict) and r.get("quando"):
            ultime.append(("scheda " + str(r.get("num", "?")), r["quando"]))
    for cosa, quando in ultime:
        try:
            t = dt.datetime.fromisoformat(quando)
        except ValueError:
            continue
        if t.tzinfo is None:
            t = t.replace(tzinfo=dt.timezone.utc)
        ore = (adesso - t).total_seconds() / 3600
        if 0 <= ore < DISTANZA_MINIMA_ORE:
            return (f"{cosa} e' uscita {ore:.1f} ore fa, meno di "
                    f"{DISTANZA_MINIMA_ORE}")
    return None


def controlla_file(num):
    """Il video sul disco deve essere a norma E avere l'audio.

    5 settembre 2026: assets/reel_005.mp4 esisteva dal 27 agosto e sembrava
    pronto. Era 1080x1920 profilo High e soprattutto MUTO (mean_volume
    -91 dB): un residuo della prima infornata, prima che musica.py entrasse
    nella pipeline. Nessun controllo lo avrebbe fermato: risponde 200 su
    Pages, ha la traccia aac al posto giusto, e l'API lo avrebbe pubblicato
    volentieri. Sarebbe uscito un reel senza suono, e me ne sarei accorto
    guardando il profilo.

    REGOLA: «il file esiste» non vuol dire «il file va bene». Prima di
    pubblicare si guarda cosa c'e' dentro, non solo che ci sia.

    Se ffprobe non c'e', si va avanti: e' un controllo in piu', non un
    cancello. Su ubuntu-latest c'e' sempre."""
    import shutil, subprocess
    f = QUI.parent / "assets" / f"reel_{num}{SUFFISSO_FILE}.mp4"
    if not f.exists() or not shutil.which("ffprobe"):
        return
    def sonda(args):
        return subprocess.run(args, capture_output=True, text=True).stdout.strip()
    dim = sonda(["ffprobe", "-v", "error", "-select_streams", "v:0",
                 "-show_entries", "stream=width,height",
                 "-of", "csv=p=0:s=x", str(f)])
    vol = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(f),
                          "-af", "volumedetect", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    media = [r for r in vol.splitlines() if "mean_volume" in r]
    print(f"file: {f.name} {dim} {media[0].split(']')[-1].strip() if media else 'audio: ?'}")
    if dim and dim != "720x1280":
        sys.exit(f"reel_{num}.mp4 e' {dim}, non 720x1280: rigeneralo con reel.py")
    # niente traccia audio del tutto: volumedetect non stampa nulla e senza
    # questo ramo il file passerebbe indisturbato.
    if not media:
        sys.exit(f"reel_{num}.mp4 non ha una traccia audio: rigeneralo con reel.py")
    if float(media[0].split(":")[-1].replace("dB", "").strip()) < -60:
        sys.exit(f"reel_{num}.mp4 e' muto: rigeneralo con reel.py "
                 f"(serve assets/musica_reel.wav, lo scrive musica.py)")


def main(num, prova=False, url=None, forza=False):
    m = next((x for x in MEMI if x["num"] == num), None)
    if not m:
        sys.exit(f"scheda {num} non trovata")

    if not (url or url_possibili(num)):
        sys.exit("serve MEMETECA_BASE_URL, oppure GITHUB_REPOSITORY")
    # LA TEORIA DEL «BUDGET VIDEO» ERA SBAGLIATA. Il 24 e il 25 agosto, dopo
    # una ventina di container tutti finiti in ERROR, avevamo scritto qui che
    # il vincolo era un budget di elaborazione video dell'account, e che
    # anche --prova lo consumasse. Il 27 agosto 2026 diagnosi_reel.py ha
    # chiesto il dato all'API invece di dedurlo:
    #
    #   content_publishing_limit → quota_total 100 / 24h, quota_usage 1
    #
    # Uno su cento. Il budget non c'entrava niente: i tentativi falliti non
    # consumano quota, perche' la quota conta le pubblicazioni riuscite.
    # Distanziare i tentativi non serviva, e la regola «mai una prova sul
    # file vero» era una precauzione contro un vincolo inesistente.
    #
    # Quello che la stessa diagnosi ha trovato davvero:
    #   · account_type MEDIA_CREATOR, 34 media, di cui 33 CAROUSEL_ALBUM in
    #     FEED e UNO solo VIDEO/REELS — quell'uno caricato dal telefono. Via
    #     API non e' mai passato niente.
    #   · assets/reel_021_v5.mp4 e' a norma: 720x1280, 27,5 s, avc1 + mp4a,
    #     nessuna edit list, moov in testa. Servito da GitHub Pages con
    #     Content-Type video/mp4 e HTTP 200.
    #
    # Cioe': il file va bene, l'URL va bene, la quota e' libera, e i reel
    # falliscono lo stesso. Resta un'ipotesi sola, ed e' strutturale: la
    # pubblicazione di REELS non e' aperta a questo account per la strada
    # Instagram Login (graph.instagram.com, senza Pagina Facebook), dove
    # invece i caroselli passano da sempre. Non e' una cosa che si aggiusta
    # ritentando.
    #
    # 30 agosto 2026 — QUESTA CONCLUSIONE ERA SBAGLIATA, e la lascio scritta
    # perche' e' l'errore piu' istruttivo di tutta la vicenda. «Resta
    # un'ipotesi sola, ed e' strutturale» non era una deduzione: era la
    # quarta ipotesi di fila costruita per spiegare un fallimento di cui non
    # avevo ancora trovato la causa. Le prime tre (budget video, percorsi
    # bruciati, formato del file) erano gia' cadute allo stesso modo.
    #
    # La causa vera era la cartella `/assets` contata due volte nell'URL
    # (vedi url_possibili). Corretta quella, i reel passano da graph.
    # instagram.com senza Pagina Facebook: 021, 022, 026, 003, 006, 019, 020
    # pubblicati via API. Nessuna strada era chiusa.
    #
    # REGOLA: quando un tentativo fallisce senza dire perche', non si
    # inventa il motivo. Si va a guardare l'anello che nessuno ha
    # verificato — qui era una HEAD sull'URL, trenta secondi — prima di
    # dichiarare strutturale un problema.
    video = url or scegli_url(num)

    s = json.loads(STATO.read_text(encoding="utf-8"))
    fatti = {r.get("num") for r in s.get("reel", [])}
    if num in fatti and not prova:
        print(f"il reel della {num} risulta gia' pubblicato")
        return

    if prova:
        # crea il contenitore e aspetta la validazione, SENZA pubblicare:
        # serve a collaudare video e hosting senza sporcare il profilo.
        controlla_file(num)
        controlla_online(video)
        ig = Instagram()
        c = ig._post(f"{ig.ig_user_id}/media", media_type="REELS",
                     video_url=video, caption="prova")["id"]
        ig._attendi_pronto(c, tentativi=60, pausa=6)
        print(f"PROVA OK: il video {video} passa la validazione (contenitore {c}, non pubblicato)")
        return

    fermo = troppo_presto(s)
    if fermo and not forza:
        print(f"::warning::Non pubblico il reel {num}: {fermo}. "
              f"Con --forza si pubblica lo stesso.")
        return

    controlla_file(num)
    controlla_online(video)
    post_id = Instagram().pubblica_reel(video, caption_reel(m))

    # lo stato si salva subito, come per le schede
    s.setdefault("reel", []).append({
        "num": num, "post_id": post_id,
        "quando": dt.datetime.now(dt.timezone.utc).isoformat(),
        "canale": "github actions (api, musica originale)"})
    STATO.write_text(json.dumps(s, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8", newline="\n")
    print(f"Pubblicato reel {num} — {m['titolo']} (post {post_id})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: python pubblica_reel.py <numero> "
                 "[--prova] [--url URL] [--forza]")
    url = None
    if "--url" in sys.argv:
        url = sys.argv[sys.argv.index("--url") + 1]
    main(sys.argv[1].zfill(3), prova="--prova" in sys.argv, url=url,
         forza="--forza" in sys.argv)
