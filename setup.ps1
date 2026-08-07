# MEMETECA — installazione in un colpo solo (Windows PowerShell)
#
#   Da D:\IMDB\memeteca, tasto destro sul file → "Esegui con PowerShell"
#
# Fa tutto: installa quello che manca, crea il repository, carica le slide,
# accende GitHub Pages (che ospita le immagini per la Graph API), imposta i
# segreti e verifica. L'unica cosa che devi digitare è il token.

param(
  [string]$Repo        = "memeteca",
  [string]$IgAppId     = "1064880032582035",   # ID app Instagram (non quello Facebook)
  [string]$RedirectUri = "https://localhost/"
)

$ErrorActionPreference = "Stop"
function Passo($n, $testo) { Write-Host "`n[$n] $testo" -ForegroundColor Cyan }
function Ok($testo)        { Write-Host "    $testo" -ForegroundColor Green }

# ───────────────────────────────────────────── 1. strumenti (installa da solo)
Passo 1 "Strumenti"
function Assicura($comando, $pacchetto) {
  if (-not (Get-Command $comando -ErrorAction SilentlyContinue)) {
    Write-Host "    installo $pacchetto..." -ForegroundColor Yellow
    winget install --id $pacchetto -e --silent `
      --accept-package-agreements --accept-source-agreements
    $env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" +
                [Environment]::GetEnvironmentVariable("Path", "User")
  }
}
Assicura git    "Git.Git"
Assicura gh     "GitHub.cli"
Assicura python "Python.Python.3.12"
Ok "git, gh e python presenti"

# ───────────────────────────────────────────── 2. accesso GitHub (una volta sola)
Passo 2 "Accesso a GitHub"
gh auth status 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
  Write-Host "    si apre il browser: accedi e autorizza." -ForegroundColor Yellow
  gh auth login --hostname github.com --git-protocol https --web
}
$utente = (gh api user --jq .login)
Ok "collegato come $utente"

# ─────────────────────────────────────────────────────────── 3. il token Instagram
Passo 3 "Token Instagram"
Write-Host "    Servono due valori, entrambi dalla dashboard dell'app Meta."
Write-Host "    Il pulsante «Genera token» di Meta e' rotto: usiamo la strada"
Write-Host "    manuale, che funziona sempre. Guida: docs\05_COSA_DEVI_FARE_TU.md" -ForegroundColor DarkGray
Write-Host ""
Write-Host "    a) La chiave segreta di Instagram (Chiave segreta -> Mostra)"
$secret = Read-Host "    Chiave segreta"
if (-not $secret) { throw "Serve la chiave segreta." }

Write-Host ""
Write-Host "    b) L'URL su cui sei atterrato dopo aver autorizzato l'app."
Write-Host "       E' quello che comincia con https://localhost/?code=..."
Write-Host "       (la pagina non si apre: e' normale, serve solo l'indirizzo)" -ForegroundColor DarkGray
$urlCode = Read-Host "    URL completo"

if ($urlCode -match "code=([^&#]+)") { $code = $Matches[1] } else { $code = $urlCode.Trim() }
$code = $code -replace "#_$", ""
if (-not $code) { throw "Non ho trovato il codice nell'URL." }

Write-Host "    scambio il codice con un token..." -ForegroundColor DarkGray
$breve = Invoke-RestMethod -Method Post -Uri "https://api.instagram.com/oauth/access_token" -Body @{
  client_id     = $IgAppId
  client_secret = $secret
  grant_type    = "authorization_code"
  redirect_uri  = $RedirectUri
  code          = $code
}
if (-not $breve.access_token) { throw "Scambio fallito: il codice potrebbe essere scaduto (durano un'ora, e valgono una volta sola). Riautorizza e riprova." }

$lungo = Invoke-RestMethod -Uri ("https://graph.instagram.com/access_token" +
  "?grant_type=ig_exchange_token&client_secret=$secret&access_token=" + $breve.access_token)
if (-not $lungo.access_token) { throw "Conversione a token lungo fallita." }

$igToken = $lungo.access_token
$giorni = [math]::Floor($lungo.expires_in / 86400)
Ok "token ottenuto, valido $giorni giorni"

# ───────────────────────────────────────────── 4. repository e caricamento
Passo 4 "Repository"
if (-not (Test-Path ".git")) {
  git init -b main | Out-Null
  git add .
  git -c user.name="memeteca" -c user.email="memeteca@local" commit -m "MEMETECA" | Out-Null
}
# Deve essere pubblico: la Graph API scarica le immagini da un URL raggiungibile,
# e Pages su repository privati richiede un piano a pagamento.
gh repo view "$utente/$Repo" 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
  gh repo create $Repo --public --source=. --remote=origin --push
} else {
  git remote remove origin 2>$null
  git remote add origin "https://github.com/$utente/$Repo.git"
  git push -u origin main --force
}
Ok "caricato su github.com/$utente/$Repo"

# ────────────────────────────────────────────────────────────────── 5. Pages
Passo 5 "GitHub Pages"
try {
  gh api -X POST "repos/$utente/$Repo/pages" -f "source[branch]=main" -f "source[path]=/" | Out-Null
} catch {
  Write-Host "    gia' attivo, proseguo." -ForegroundColor DarkGray
}
$baseUrl = "https://$utente.github.io/$Repo/assets"
Ok "immagini su $baseUrl"

# ─────────────────────────────────────────────────────────────────── 6. segreti
Passo 6 "Segreti"
$igToken | gh secret set IG_ACCESS_TOKEN   --repo "$utente/$Repo"
$baseUrl | gh secret set MEMETECA_BASE_URL --repo "$utente/$Repo"
Ok "impostati"

# ─────────────────────────────────────────────────────────────── 7. verifica
Passo 7 "Controllo"
$env:IG_ACCESS_TOKEN = $igToken
$env:MEMETECA_BASE_URL = $baseUrl
Write-Host "    Pages impiega 1-2 minuti ad andare online: aspetto." -ForegroundColor DarkGray
Start-Sleep -Seconds 90
Push-Location agente
python -m pip install -q -r requirements.txt
python verifica.py
$esito = $LASTEXITCODE
Pop-Location

if ($esito -eq 0) {
  Write-Host @"

Tutto a posto. Da qui in poi va da solo: 12:30, 18:30 e 21:00.

  Primo post subito:  gh workflow run pubblica.yml --repo $utente/$Repo
  Come sta andando:   gh run list --repo $utente/$Repo

"@ -ForegroundColor Green
} else {
  Write-Host @"

Il controllo ha trovato qualcosa (sopra c'e' scritto cosa).
Se sono solo le immagini "irraggiungibili", Pages non e' ancora online:
riprova fra qualche minuto con  python agente\verifica.py

"@ -ForegroundColor Yellow
}
