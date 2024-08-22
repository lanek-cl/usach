@echo off
setlocal

REM Define variables
set DEPLOY_KEY_PATH=%USERPROFILE%\.ssh\usach-key
set PUB_KEY_PATH=%DEPLOY_KEY_PATH%.pub

REM Generate SSH key if it doesn't exist
if not exist "%DEPLOY_KEY_PATH%" (
    echo Generating SSH key...
    ssh-keygen -t ed25519 -C "lucas.cortes@lanek.cl" -f "%DEPLOY_KEY_PATH%" -N ""
)

REM Configure SSH to use the deploy key
echo Configuring SSH...
echo Host github.com > %USERPROFILE%\.ssh\config
echo     HostName github.com >> %USERPROFILE%\.ssh\config
echo     User git >> %USERPROFILE%\.ssh\config
echo     IdentityFile %DEPLOY_KEY_PATH% >> %USERPROFILE%\.ssh\config
echo     IdentitiesOnly yes >> %USERPROFILE%\.ssh\config

REM Start SSH agent and add the deploy key
echo Starting SSH agent...
for /f "delims=" %%i in ('ssh-agent -s') do set "%%i"
ssh-add "%DEPLOY_KEY_PATH%"

REM Print the public key
echo Public key:
type "%PUB_KEY_PATH%"

echo Press Enter to close this window.
pause >nul

endlocal
