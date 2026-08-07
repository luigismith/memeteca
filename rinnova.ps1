# MEMETECA — rinnovo del token (Windows PowerShell)
#
#   .\rinnova.ps1
#
# Il token Instagram dura 60 giorni ed è prolungabile all'infinito senza
# rigenerare niente e senza app secret. Questo script lo prolunga e aggiorna
# il segreto su GitHub. Lancialo quando il workflow ti avvisa.

$ErrorActionPreference = "Stop"

$utente = (gh api user --jq .login)
$repo   = "memeteca"

# Il token attuale non è leggibile dai segreti di GitHub: incollalo.
$vecchio = Read-Host "Token attuale"
if (-not $vecchio) { throw "Serve il token attuale." }

$env:IG_ACCESS_TOKEN = $vecchio
Push-Location agente
$nuovo = (python instagram.py rinnova)
Pop-Location

if (-not $nuovo) { throw "Rinnovo fallito." }

$nuovo | gh secret set IG_ACCESS_TOKEN --repo "$utente/$repo"

Write-Host "`nToken rinnovato e aggiornato su GitHub." -ForegroundColor Green
Write-Host "Conservalo, servirà al prossimo rinnovo:" -ForegroundColor DarkGray
Write-Host $nuovo
