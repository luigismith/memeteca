# Quello che resta da fare a mano

L'account c'è. Manca il token: è la chiave che permette allo script di pubblicare al posto tuo. Non posso generarlo io perché richiede di autenticarsi con le tue credenziali Meta, e le password non le digito mai al posto di una persona. Tutto il resto — ricerca, testi, grafica, pubblicazione, calendario — è già fatto e gira senza di te.

Un quarto d'ora. Poi la pagina va avanti da sola.

---

## Parte A — L'account Instagram ✅ fatto

L'account è **`@memeteca_italiana`**. Restano tre cose da sistemare sul profilo:

1. Nome visualizzato: **MEMETECA**
2. Bio — copia e incolla:

```
L'archivio ragionato del meme italiano.
Una scheda per meme: chi, quando, perché.
3 al giorno · fonti verificate
```

3. **Impostazioni → Tipo di account e strumenti → Passa a un account professionale → Creator**
4. Collegalo a una **Pagina Facebook**. Se non ne hai una, creane una vuota con lo stesso nome: serve solo perché l'API di Instagram passa da lì.

I punti 3 e 4 non sono facoltativi: senza account professionale collegato a una Pagina, la Graph API non vede l'account e non c'è token che tenga.

---

## Parte B — Il token Meta (15 minuti)

È la parte noiosa. Seguila alla lettera e non ci sono sorprese.

**1. Crea l'app**
Vai su [developers.facebook.com/apps](https://developers.facebook.com/apps) → *Crea un'app* → tipo **Altro** → **Business**. Chiamala `MEMETECA`.

**2. Aggiungi il prodotto**
Nella dashboard dell'app, aggiungi **Instagram Graph API**.

**3. Prendi il token breve**
Vai su [Graph API Explorer](https://developers.facebook.com/tools/explorer/), seleziona la tua app, poi *Add permissions* e spunta:

```
instagram_basic
instagram_content_publish
pages_read_engagement
pages_show_list
business_management
```

Clicca **Generate Access Token** e accetta. Ottieni un token che dura un'ora: chiamiamolo `TOKEN_BREVE`.

**4. Trova l'IG_USER_ID**
Sempre nell'Explorer, esegui in sequenza:

```
me/accounts
```
→ prendi l'`id` della tua Pagina Facebook, poi:
```
{ID_PAGINA}?fields=instagram_business_account
```
→ il numero che compare è il tuo **IG_USER_ID**. Segnalo.

**5. Trasforma il token breve in uno da 60 giorni**
Ti servono l'*App ID* e l'*App Secret* (dashboard dell'app → *Impostazioni → Di base*). Poi apri questo indirizzo nel browser, sostituendo i tre valori:

```
https://graph.facebook.com/v21.0/oauth/access_token
  ?grant_type=fb_exchange_token
  &client_id=APP_ID
  &client_secret=APP_SECRET
  &fb_exchange_token=TOKEN_BREVE
```

La risposta contiene `access_token`: **quello è il tuo IG_ACCESS_TOKEN**.

> Va rinnovato ogni 60 giorni ripetendo solo questo passaggio 5. Il workflow ti avvisa quando mancano meno di dieci giorni.

---

## Parte C — Accendere tutto (1 comando)

Da PowerShell, in `D:\IMDB\memeteca`:

```powershell
.\setup.ps1
```

Ti chiede `IG_USER_ID` e `IG_ACCESS_TOKEN`, poi fa il resto: crea il repository, carica le 63 slide, accende GitHub Pages per ospitarle, imposta i segreti e lancia il controllo preliminare.

Se preferisci controllare prima di dare i valori allo script:

```powershell
$env:IG_USER_ID="..."; $env:IG_ACCESS_TOKEN="..."; $env:MEMETECA_BASE_URL="..."
python agente\verifica.py
```

`verifica.py` controlla che il token sia valido, che i permessi ci siano tutti, quanti giorni manchino alla scadenza, che le immagini siano davvero raggiungibili dall'esterno e che nessuna caption superi i 2.200 caratteri. Non pubblica niente.

---

## Se preferisci non passare da GitHub

Il repository non è un capriccio: la Graph API **non accetta upload di file**, scarica le immagini da un URL pubblico. Serve quindi un posto da cui servirle, e serve qualcosa che faccia partire la pubblicazione tre volte al giorno anche a computer spento. GitHub Pages più GitHub Actions risolvono entrambe le cose gratis e in un colpo solo.

Qualunque altro hosting statico va bene lo stesso — carica la cartella `assets/` dove preferisci e passa quell'indirizzo come `MEMETECA_BASE_URL`. Per il cron ti servirà comunque qualcosa che stia acceso.
