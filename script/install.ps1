$installPath= ([Environment]::GetFolderPath("MyDocuments"))

Write-Host "Installation will be done on below path:\n $installPath"
$resp=Read-Host -Prompt "Press ENTER to continue or enter custom path:"

if ($resp -ne "")
{
    if (Test-Path -LiteralPath $resp)
    {
        Write-Host "Valid path"
        $installPath=$resp
    } else
    {
        Write-Host "invalid path"
        exit
    }
}

$installPath="$installPath"
Write-Host "installing at $installPath"

mkdir $installPath
Set-Location $installPath

git clone https://github.com/tehritarun/pdf_Actions.git

Set-Location .\pdf_actions

pipenv install

powershell.exe -File .\script\updateresgistry.ps1 "$installPath\pdf_actions"


