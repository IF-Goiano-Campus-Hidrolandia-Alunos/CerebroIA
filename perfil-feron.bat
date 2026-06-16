@echo off
REM ============================================================================
REM  Define ESTE PC como o perfil FeronZerbana para os commits deste vault.
REM  Rode UMA vez ao baixar/clonar o vault (e sempre que quiser trocar o perfil).
REM ============================================================================
cd /d "%~dp0"

REM 1) Configura o autor dos commits NESTE repositorio (config local, nao versionada)
git config user.name "FeronZerbana"
git config user.email "ddrive221@gmail.com"

REM 2) Cria o marcador de identidade local (ignorado pelo git via .gitignore)
(
echo # Identidade deste PC
echo.
echo Perfil: FeronZerbana
echo Nome:   FeronZerbana
echo Email:  ddrive221@gmail.com
echo.
echo Todos os commits deste vault DEVEM usar este usuario.
echo Arquivo gerado por perfil-feron.bat - nao versionado ^(.gitignore^).
) > IDENTIDADE-LOCAL.md

echo.
echo Perfil deste PC definido: FeronZerbana ^(ddrive221@gmail.com^)
echo Os commits do vault usarao esse usuario.
echo.
pause
