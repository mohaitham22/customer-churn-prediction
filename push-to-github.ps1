# GitHub Push Automation Script
# This script will push your project to GitHub with minimal manual input

# Get user input
$username = Read-Host "Enter your GitHub username"
$token = Read-Host "Enter your Personal Access Token (from GitHub Settings)" -AsSecureString
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($token)
$token_plain = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Navigate to project
cd "c:\Users\mooda\OneDrive\Desktop\project\project"

# Configure git
Write-Host "Configuring git..." -ForegroundColor Green
git config user.name $username
git config user.email "$username@example.com"

# Set up remote with authentication
Write-Host "Setting up GitHub remote..." -ForegroundColor Green
$repoUrl = "https://$($username):$($token_plain)@github.com/$username/customer-churn-prediction.git"
git remote remove origin 2>$null
git remote add origin $repoUrl

# Rename branch to main
Write-Host "Renaming branch to main..." -ForegroundColor Green
git branch -M main

# Push to GitHub
Write-Host "Pushing to GitHub..." -ForegroundColor Green
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Success! Your project is now on GitHub!" -ForegroundColor Green
    Write-Host "Repository URL: https://github.com/$username/customer-churn-prediction"
} else {
    Write-Host "❌ Push failed. Check your token and try again." -ForegroundColor Red
}

# Clean up sensitive data
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
