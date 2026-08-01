Param(
    [switch]$Check,
    [switch]$Prompt
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$scriptPath = Join-Path $PSScriptRoot "sync-agents.py"
$arguments = @($scriptPath)
if ($Check) {
    $arguments += "--check"
}
elseif ($Prompt) {
    $arguments += "--prompt"
}

$python3 = Get-Command python3 -ErrorAction SilentlyContinue
if ($python3) {
    & $python3.Source @arguments
    exit $LASTEXITCODE
}

$py = Get-Command py -ErrorAction SilentlyContinue
if ($py) {
    & $py.Source -3 @arguments
    exit $LASTEXITCODE
}

$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    & $python.Source @arguments
    exit $LASTEXITCODE
}

throw "Python 3 is required to run tools/sync-agents.py."
