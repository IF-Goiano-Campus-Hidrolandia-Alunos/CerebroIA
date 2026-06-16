@echo off
REM ============================================================================
REM  Define ESTE PC como o perfil ThyagoToledo para os commits deste vault.
REM  Rode UMA vez ao baixar/clonar o vault (e sempre que quiser trocar o perfil).
REM ============================================================================
cd /d "%~dp0"

REM 1) Configura o autor dos commits NESTE repositorio (config local, nao versionada)
git config user.name "ThyagoToledo"
git config user.email "thyago10a2007@gmail.com"

REM 2) Cria o marcador de identidade local (ignorado pelo git via .gitignore)
(
echo # Identidade deste PC
echo.
echo Perfil: ThyagoToledo
echo Nome:   ThyagoToledo
echo Email:  thyago10a2007@gmail.com
echo.
echo Todos os commits deste vault DEVEM usar este usuario.
echo Arquivo gerado por perfil-thyago.bat - nao versionado ^(.gitignore^).
) > IDENTIDADE-LOCAL.md

echo.
echo Perfil deste PC definido: ThyagoToledo ^(thyago10a2007@gmail.com^)
echo Os commits do vault usarao esse usuario.
echo.
pause
