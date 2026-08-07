# MEMETECA - installazione in un colpo solo (Windows PowerShell)
#
#   Da D:\IMDB\memeteca, tasto destro sul file -> "Esegui con PowerShell"
#
# Fa tutto: installa quello che manca, crea il repository, accende GitHub Pages
# (che ospita le immagini per la Graph API), scambia il token e imposta i segreti.
#
# ORDINE IMPORTANTE: GitHub viene preparato PRIMA di scambiare il codice.
# Il codice di autorizzazione vale una volta sola: se lo bruciassimo prima e poi
# GitHub fallisse, il token andrebbe perso e servirebbe riautorizzare da capo.
#
# La finestra NON si chiude da sola, e scrive `setup-log.txt` accanto a questo
# file: solo i passaggi e gli errori, mai la chiave segreta né il token.

param(
  [string]$Repo        = "memeteca",
  [string]$IgAppId     = "1064880032582035",   # ID app Instagram (non quello Facebook)
  [string]$RedirectUri = "https://localhost/"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot   # ancora tutto alla cartella del progetto
$LogFile = Join-Path $PSScriptRoot "setup-log.txt"
$Segreti = @()   # valori da oscurare nel log

"MEMETECA setup - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" | Set-Content $LogFile -Encoding UTF8

function Oscura($testo) {
  foreach ($s in $Segreti) { if ($s) { $testo = $testo -replace [regex]::Escape($s), "***" } }
  return $testo
}
function Log($testo)       { (Oscura $testo) | Add-Content $LogFile -Encoding UTF8 }
function Passo($n, $testo) { Write-Host "`n[$n] $testo" -ForegroundColor Cyan; Log "[$n] $testo" }
function Ok($testo)        { Write-Host "    $testo" -ForegroundColor Green;  Log "    ok: $testo" }
function Nota($testo)      { Write-Host "    $testo" -ForegroundColor DarkGray; Log "    .. $testo" }

try {

# I comandi esterni (git, gh, winget) scrivono avvisi su stderr. Con
# ErrorActionPreference = "Stop" PowerShell li scambia per errori fatali:
# e' cosi' che un warning su LF/CRLF ha fermato tutto. Qui li isoliamo e
# giudichiamo solo dal codice di uscita, che e' l'unica cosa che conta.
function Nativo {
  param(
    [Parameter(Mandatory)][string]$Comando,
    [string[]]$Argomenti = @(),
    [string]$SeFallisce,
    [switch]$Mostra
  )
  $prima = $ErrorActionPreference
  $ErrorActionPreference = "Continue"
  $uscita = & $Comando @Argomenti 2>&1
  $codice = $LASTEXITCODE
  $ErrorActionPreference = $prima
  foreach ($riga in $uscita) { $testo = "$riga"; if ($testo.Trim()) { Log "       $testo"; if ($Mostra) { Nota $testo } } }
  if ($codice -ne 0 -and $SeFallisce) { throw $SeFallisce }
  return $codice
}


# --------------------------------------------- 1. strumenti (installa da solo)
Passo 1 "Strumenti"
function Assicura($comando, $pacchetto) {
  if (-not (Get-Command $comando -ErrorAction SilentlyContinue)) {
    Write-Host "    installo $pacchetto..." -ForegroundColor Yellow
    Log "    installo $pacchetto"
    winget install --id $pacchetto -e --silent `
      --accept-package-agreements --accept-source-agreements
    $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
                [Environment]::GetEnvironmentVariable("Path", "User")
  }
}
Assicura git    "Git.Git"
Assicura gh     "GitHub.cli"
Assicura python "Python.Python.3.12"
foreach ($c in "git", "gh", "python") {
  if (-not (Get-Command $c -ErrorAction SilentlyContinue)) {
    throw "$c non risulta installato. Chiudi e riapri PowerShell (il PATH si aggiorna solo alla riapertura) e rilancia."
  }
}
Ok "git, gh e python presenti"

# --------------------------------------------- 2. accesso GitHub (una volta sola)
Passo 2 "Accesso a GitHub"
gh auth status 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
  Write-Host "    si apre il browser: accedi e autorizza." -ForegroundColor Yellow
  gh auth login --hostname github.com --git-protocol https --web
  if ($LASTEXITCODE -ne 0) { throw "Accesso a GitHub non completato." }
}
$utente = (gh api user --jq .login)
if (-not $utente) { throw "Non riesco a leggere l'utente GitHub: l'accesso non e' andato a buon fine." }
Ok "collegato come $utente"

# ------------------------------------- 3. repository e caricamento (PRIMA del token)
Passo 3 "Repository"
# Niente conversione di fine riga: toglie il warning di git e azzera il rischio
# di toccare i JPEG delle slide.
"* -text" | Set-Content ".gitattributes" -Encoding ASCII

if (-not (Test-Path ".git")) { Nativo git @("init", "-b", "main") | Out-Null }
Nativo git @("add", "-A") -SeFallisce "git add ha fallito." | Out-Null
Nativo git @("-c", "user.name=memeteca", "-c", "user.email=memeteca@local",
             "commit", "-m", "MEMETECA") | Out-Null   # 0 file da committare: va bene

# Deve essere pubblico: la Graph API scarica le immagini da un URL raggiungibile,
# e Pages su repository privati richiede un piano a pagamento.
$esisteRepo = (Nativo gh @("repo", "view", "$utente/$Repo")) -eq 0
if (-not $esisteRepo) {
  Nota "creo github.com/$utente/$Repo (pubblico)"
  Nativo gh @("repo", "create", $Repo, "--public",
              "--description", "MEMETECA - archivio del meme italiano") `
    -SeFallisce "Creazione del repository fallita. Prova: gh auth refresh -s repo,workflow" -Mostra | Out-Null
}
Nativo git @("remote", "remove", "origin") | Out-Null
Nativo git @("remote", "add", "origin", "https://github.com/$utente/$Repo.git") | Out-Null
Nativo git @("push", "-u", "origin", "main", "--force") `
  -SeFallisce "Push fallito. Prova: gh auth refresh -s repo,workflow" -Mostra | Out-Null
Ok "caricato su github.com/$utente/$Repo"

# ------------------------------------------------------------------ 4. Pages
Passo 4 "GitHub Pages"
if ((Nativo gh @("api", "-X", "POST", "repos/$utente/$Repo/pages",
                 "-f", "source[branch]=main", "-f", "source[path]=/")) -ne 0) {
  Nota "gia' attivo (o attivazione non necessaria), proseguo"
}
$baseUrl = "https://$utente.github.io/$Repo/assets"
Ok "immagini su $baseUrl"

# ----------------------------------------------------------- 5. il token Instagram
Passo 5 "Token Instagram"
Write-Host "    Servono due valori."
Write-Host ""
Write-Host "    a) La chiave segreta di Instagram"
Write-Host "       developers.facebook.com -> app MEMETECA -> API Instagram" -ForegroundColor DarkGray
Write-Host "       -> Configurazione dell'API con Instagram login -> Mostra" -ForegroundColor DarkGray
$secret = Read-Host "    Chiave segreta"
if (-not $secret) { throw "Serve la chiave segreta." }
$Segreti += $secret

Write-Host ""
Write-Host "    b) L'URL su cui sei atterrato dopo aver autorizzato l'app."
Write-Host "       Quello che comincia con https://localhost/?code=..."
Write-Host "       (la pagina non si apre: e' normale, serve solo l'indirizzo)" -ForegroundColor DarkGray
$urlCode = Read-Host "    URL completo"

if ($urlCode -match "code=([^&#]+)") { $code = $Matches[1] } else { $code = $urlCode.Trim() }
$code = $code -replace "#_$", ""
if (-not $code) { throw "Non ho trovato il codice nell'URL." }
$Segreti += $code

Nota "scambio il codice con un token"
try {
  $breve = Invoke-RestMethod -Method Post -Uri "https://api.instagram.com/oauth/access_token" -Body @{
    client_id     = $IgAppId
    client_secret = $secret
    grant_type    = "authorization_code"
    redirect_uri  = $RedirectUri
    code          = $code
  }
} catch {
  throw ("Scambio fallito. Il codice vale una volta sola e scade in un'ora: riautorizza e rilancia. (dettaglio: " + (Oscura $_.Exception.Message) + ")")
}
if (-not $breve.access_token) { throw "Scambio fallito: nessun token nella risposta." }
$Segreti += $breve.access_token

try {
  $lungo = Invoke-RestMethod -Method Get -Uri "https://graph.instagram.com/access_token" -Body @{
    grant_type    = "ig_exchange_token"
    client_secret = $secret
    access_token  = $breve.access_token
  }
} catch {
  throw ("Conversione a token lungo fallita (dettaglio: " + (Oscura $_.Exception.Message) + ")")
}
if (-not $lungo.access_token) { throw "Conversione a token lungo fallita: nessun token nella risposta." }

$igToken = $lungo.access_token
$Segreti += $igToken
$giorni = [math]::Floor($lungo.expires_in / 86400)
Ok "token ottenuto, valido $giorni giorni"

# ------------------------------------------------------------------- 6. segreti
Passo 6 "Segreti"
$prima = $ErrorActionPreference; $ErrorActionPreference = "Continue"
$igToken | gh secret set IG_ACCESS_TOKEN   --repo "$utente/$Repo" 2>&1 | Out-Null
$codiceSegreto = $LASTEXITCODE
$baseUrl | gh secret set MEMETECA_BASE_URL --repo "$utente/$Repo" 2>&1 | Out-Null
$ErrorActionPreference = $prima
if ($codiceSegreto -ne 0) { throw "Non sono riuscito a scrivere il segreto IG_ACCESS_TOKEN." }
Ok "impostati"

# --------------------------------------------------------------- 7. verifica
Passo 7 "Controllo"
$env:IG_ACCESS_TOKEN = $igToken
$env:MEMETECA_BASE_URL = $baseUrl
Nota "Pages impiega 1-2 minuti ad andare online: aspetto"
Start-Sleep -Seconds 90
Push-Location agente
$prima = $ErrorActionPreference; $ErrorActionPreference = "Continue"
python -m pip install -q -r requirements.txt 2>&1 | Out-Null
$esitoTesto = python verifica.py 2>&1
$esito = $LASTEXITCODE
$ErrorActionPreference = $prima
$esitoTesto | ForEach-Object { Write-Host "    $_" }
Pop-Location
Log "--- verifica ---"
Log ($esitoTesto -join "`n")

if ($esito -eq 0) {
  Write-Host @"

Tutto a posto. Repository: github.com/$utente/$Repo

  Primo post subito:  gh workflow run pubblica.yml --repo $utente/$Repo
  Come sta andando:   gh run list --repo $utente/$Repo

"@ -ForegroundColor Green
  Log "ESITO: tutto a posto"
} else {
  Write-Host @"

Il controllo ha trovato qualcosa (sopra c'e' scritto cosa).
Se sono solo le immagini "irraggiungibili", Pages non e' ancora online:
riprova fra qualche minuto con  python agente\verifica.py

"@ -ForegroundColor Yellow
  Log "ESITO: verifica con avvisi"
}

} catch {
  Write-Host "`nERRORE: $(Oscura $_.Exception.Message)" -ForegroundColor Red
  Log "ERRORE: $(Oscura $_.Exception.Message)"
  Log "riga: $($_.InvocationInfo.ScriptLineNumber)"
} finally {
  Write-Host "`nLog salvato in: $LogFile" -ForegroundColor DarkGray
  Write-Host "Premi Invio per chiudere questa finestra." -ForegroundColor DarkGray
  Read-Host | Out-Null
}
