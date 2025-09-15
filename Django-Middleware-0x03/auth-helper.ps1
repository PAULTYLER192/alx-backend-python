# ========================
# Django JWT Auth Helper
# ========================

# Load from environment variables
$apiBaseUrl = $env:DJANGO_API_BASE_URL
$username   = $env:DJANGO_API_USERNAME
$password   = $env:DJANGO_API_PASSWORD
$tokenFile  = ".\tokens.json"
function Get-NewTokens {
    param()

    Write-Host "[LOGIN] Getting new tokens..."
    $body = @{
        username = $username
        password = $password
    } | ConvertTo-Json

    $response = Invoke-RestMethod -Uri "$apiBaseUrl/api/token/" `
        -Method Post `
        -ContentType "application/json" `
        -Body $body

    $response | ConvertTo-Json | Out-File $tokenFile
    return $response
}

function Refresh-Tokens {
    param($refreshToken)

    Write-Host "[REFRESH] Refreshing access token..."
    $body = @{ refresh = $refreshToken } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri "$apiBaseUrl/api/token/refresh/" `
            -Method Post `
            -ContentType "application/json" `
            -Body $body
        $tokens = @{ access = $response.access; refresh = $refreshToken }
        $tokens | ConvertTo-Json | Out-File $tokenFile
        return $tokens
    }
    catch {
        Write-Host "[ERROR] Refresh failed, logging in again..."
        return Get-NewTokens
    }
}

function Get-ValidTokens {
    if (Test-Path $tokenFile) {
        $tokens = Get-Content $tokenFile | ConvertFrom-Json
        return Refresh-Tokens $tokens.refresh
    }
    else {
        return Get-NewTokens
    }
}

# Exported function: use this for API calls
function Invoke-Api {
    param(
        [string]$endpoint,
        [string]$method = "Get",
        $body = $null
    )

    $tokens = Get-ValidTokens
    $headers = @{ Authorization = "Bearer $($tokens.access)" }

    if ($body) {
        $jsonBody = $body | ConvertTo-Json -Compress
        return Invoke-RestMethod -Uri "$apiBaseUrl$endpoint" -Method $method -Headers $headers -ContentType "application/json" -Body $jsonBody
    }
    else {
        return Invoke-RestMethod -Uri "$apiBaseUrl$endpoint" -Method $method -Headers $headers
    }
}
