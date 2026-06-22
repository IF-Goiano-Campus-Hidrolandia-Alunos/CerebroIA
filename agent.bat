@echo off
if "%~1" == "" (
    python "%~dp0scripts\brain_researcher.py" --chat
) else (
    python "%~dp0scripts\brain_researcher.py" "%~1"
)
pause
