# MEMETECA

*L'archivio ragionato del meme italiano.* Una pagina Instagram che non pubblica meme: li **scheda**. Tre schede al giorno, ciascuna con creatore, prima apparizione, origini, storia, significato e fonti verificate.

## Cosa c'è qui dentro

| Cartella | Contenuto |
|---|---|
| `docs/00_IDENTITA_PAGINA.md` | nome, bio, palette, tono di voce, strategia hashtag |
| `docs/01_CALENDARIO.md` | i 21 post della prima settimana, giorno per giorno |
| `docs/02_CAPTION.md` | le 21 caption complete, pronte da incollare |
| `docs/03_AGENTE_AUTONOMO.md` | come far girare tutto da solo |
| `docs/04_COME_OTTENERE_IL_TOKEN.md` | account Instagram e token Meta, passo per passo |
| `docs/05_COSA_DEVI_FARE_TU.md` | **parti da qui**: quello che resta a te |
| `docs/06_STRATEGIA.md` | crescita e monetizzazione, con i numeri |
| `docs/07_POST_BONUS.md` | quando la giornata merita un post extra, e quando no |
| `docs/08_REPERTI.md` | il frammento dell'originale in copertina: forme, diritto, limiti |
| `docs/09_INTERAZIONE.md` | chi seguire e come commentare, e cosa non si può automatizzare |
| `setup.ps1` | installazione in un comando: repo, Pages, segreti, verifica |
| `rinnova.ps1` | prolunga il token di altri 60 giorni |
| `assets/` | 63 slide 1080×1350 (21 caroselli da 3) |
| `reperti/` | i fotogrammi veri, se e quando li aggiungi |
| `agente/` | il codice: contenuti, grafica, bonus, client Instagram, orchestratore |
| `.github/workflows/` | il cron che pubblica 2 volte al giorno |

## Partenza rapida

```powershell
.\setup.ps1     # crea il repo, accende Pages, imposta i segreti, verifica tutto
```

Prima servono un account Instagram Creator e un token Meta: la procedura completa,
venti minuti, è in `docs/04_COME_OTTENERE_IL_TOKEN.md`.

A mano, comando per comando:

```bash
cd agente
pip install -r requirements.txt

python verifica.py             # controlla credenziali, permessi, immagini, caption
python pubblica.py prossimo    # la prossima scheda in coda, con la sua caption
python pubblica.py esporta     # rigenera calendario e caption in docs/
python pubblica.py genera      # rigenera le 63 slide (serve Playwright + Chromium)
python pubblica.py pubblica --prova --base-url https://esempio.it/assets
```

## Le 21 schede della settimana 1

**Internet 2005-2015** — Nonciclopedia · Le più belle frasi di Osho · Boris · Il Trota · Andrea Diprè · Er Faina · Bimbominkia
**Internet 2015-2026** — Non ce n'è coviddi · Io sono Giorgia · Pensati paracula · Tananai ultimo · Il pacco da giù · Andiamo a comandare · #ciaone
**Cinema** — La supercazzola · Una cagata pazzesca · Io so' io · Maccarone m'hai provocato
**TV e pubblicità (domenica)** — L'asteroide del Buondì · Capra! capra! capra! · L'uomo del Monte ha detto sì

Ogni scheda dichiara il proprio grado di affidabilità. Dove una fonte è sola o contesa, sta scritto.

## Nota sul copyright

Le slide sono interamente tipografiche e originali: nessun fotogramma, spot, screenshot o meme di terzi viene ricaricato. È una scelta di posizionamento prima ancora che legale — ma elimina alla radice il rischio di takedown che affossa la maggior parte delle pagine di meme.
