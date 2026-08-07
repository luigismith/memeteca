# Cosa devi fare tu

Tutto il resto è fatto. L'app Meta esiste, l'account è collegato, i permessi ci
sono. Resta il token, e il token richiede le tue credenziali: quella è la riga
che non attraverso mai.

**Problema aperto:** il login di autorizzazione dell'app risponde «Non siamo
riusciti a connetterti a Instagram», sia dal pulsante «Genera token» sia dalla
pagina di autorizzazione diretta. Non è la tua connessione — normale login e
pubblicazione funzionano. Le tre cause plausibili, in ordine, sono in fondo a
questo documento.

---

## 1 · Autorizza l'app — 1 minuto

Apri questo indirizzo (te l'ho già aperto nel browser):

```
https://www.instagram.com/oauth/authorize?client_id=1064880032582035&redirect_uri=https%3A%2F%2Flocalhost%2F&response_type=code&scope=instagram_business_basic%2Cinstagram_business_content_publish%2Cinstagram_business_manage_comments%2Cinstagram_business_manage_messages
```

1. Accedi come **memeteca_italiana** *(il campo è precompilato con luigimassari80: cancellalo)*
2. Premi **Consenti**
3. Il browser finisce su `https://localhost/?code=...` e mostra un **errore di connessione: è normale e previsto**, non esiste nessun sito su localhost. Serve solo l'indirizzo.
4. **Copia l'intero indirizzo dalla barra degli URL**

> Il codice dura un'ora e vale una volta sola. Se sbagli, riapri il link e rifai: non si rompe niente.

---

## 2 · Prendi la chiave segreta — 10 secondi

Nella dashboard dell'app, sezione *Configurazione dell'API con Instagram*, in alto
a destra c'è **Chiave segreta di Instagram** con un pulsante **Mostra**. Copiala.

[Link diretto](https://developers.facebook.com/apps/1600779401725135/use_cases/customize/API-Setup/?use_case_enum=INSTAGRAM_BUSINESS&product_route=instagram-business&selected_tab=API-Setup)

---

## 3 · Lancia lo script — 5 minuti, quasi tutti d'attesa

Da `D:\IMDB\memeteca`: tasto destro su **`setup.ps1`** → *Esegui con PowerShell*.

Ti chiede i due valori dei punti 1 e 2. Poi fa tutto da solo: scambia il codice
con un token da 60 giorni, installa git/gh/python se mancano, crea il repository,
carica le 66 slide, accende Pages, imposta i segreti e verifica che risponda.

Né la chiave segreta né il token passano da me: restano fra il tuo PC e GitHub.

Da qui in poi pubblica da solo alle 12:30, 18:30 e 21:00, anche a computer spento.

---

## Poi, due cose in coda

**Cambia la password di memeteca_italiana.** È finita in chiaro nella nostra
conversazione, dentro uno screenshot.

**Il ricorso sulla restrizione**, se ti va: app Instagram → Account Quality →
*Richiedi revisione*. Riguarda solo le inserzioni a pagamento, non blocca la
pubblicazione — i quattro post di oggi sono usciti tutti.

---

## Il rinnovo, fra due mesi

```powershell
.\rinnova.ps1
```

Prolunga il token di altri 60 giorni e aggiorna il segreto su GitHub. Non serve
rifare niente di tutto questo: il token si rinnova da sé, all'infinito. Il
workflow ti avvisa quando mancano meno di dieci giorni.


---

## Se il login di autorizzazione dà errore

Il messaggio «Non siamo riusciti a connetterti a Instagram» è il messaggio
generico di Instagram: non dice niente sulla causa reale. In ordine di
probabilità:

**1. Password compilata dal browser, ma vecchia.** Hai cambiato la password oggi.
Chrome potrebbe reinserire quella di prima. Svuota il campo password e digitala a
mano invece di accettare il precompilato.

**2. Sessioni Instagram in conflitto.** Nello stesso browser convivono
luigimassari80 e memeteca_italiana. È la causa più segnalata per questo errore
specifico. Prova in una **finestra di navigazione in incognito**, dove non c'è
nessuna sessione: apri lì l'indirizzo di autorizzazione del punto 1 e accedi da
zero.

**3. La restrizione sull'account.** Un account professionale appena creato e già
sotto restrizione può essere bloccato da Meta nell'autorizzare app. In quel caso
serve prima il ricorso (app Instagram → Account Quality → Richiedi revisione,
risposta entro 24 ore) e poi si riprova.

Nel frattempo la pagina non è ferma: la pubblicazione dal browser funziona, ed è
così che sono usciti i quattro post di oggi.
