# Client 1-Click Deployment Script for Windows (PowerShell)
# Usage: .\deploy_client_model.ps1 -Repo "aryansexter/ronin-support-3b-GGUF" -Quant "Q4_K_M"

param (
    [string]$Repo = "aryansexter/ronin-support-3b-GGUF",
    [string]$Quant = "Q4_K_M",
    [string]$ModelName = "client-custom-llm"
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Deploying Private Model: $Repo [$Quant]" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Check Ollama
if (!(Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "Ollama is not installed. Please download it from https://ollama.com and run this script again." -ForegroundColor Yellow
    exit 1
}

# 2. Extract slug
$slug = ($Repo -split "/")[-1].Replace("-GGUF", "")
$fileName = "$slug-$Quant.gguf"
$downloadUrl = "https://huggingface.co/$Repo/resolve/main/$fileName"

Write-Host "Downloading calibrated GGUF from Hugging Face: $downloadUrl..." -ForegroundColor Green
Invoke-WebRequest -Uri $downloadUrl -OutFile $fileName

# 3. Create Modelfile
Write-Host "Building Ollama Modelfile..." -ForegroundColor Green
$modelfileContent = "FROM ./$fileName`nPARAMETER temperature 0.3`nPARAMETER top_p 0.9`n"
Set-Content -Path "Modelfile" -Value $modelfileContent

# 4. Create model in Ollama
Write-Host "Registering model '$ModelName' in Ollama..." -ForegroundColor Green
ollama create $ModelName -f Modelfile

Write-Host "`n Deployment Complete!" -ForegroundColor Green
Write-Host "Run your private model anytime using:" -ForegroundColor Yellow
Write-Host "    ollama run $ModelName" -ForegroundColor White
Write-Host "Or connect via local API at: http://localhost:11434/api/chat`n" -ForegroundColor Yellow
