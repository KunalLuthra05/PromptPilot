@echo off
title AI Launcher
color 0A

echo ==========================================
echo        AI Launcher
echo ==========================================
echo.

:: Check Ollama
tasklist | find /i "ollama.exe" >nul

if %errorlevel%==0 (
    echo [✓] Ollama is already running.
) else (
    echo [*] Starting Ollama...
    start "" ollama serve
    timeout /t 3 /nobreak >nul
)

echo.

echo [*] Starting Open WebUI...

start "" "C:\Users\Kunal\AppData\Local\Python\pythoncore-3.12-64\Scripts\open-webui.exe" serve

echo.
echo Waiting for Open WebUI...
timeout /t 40 /nobreak >nul

echo.
echo Opening browser...

start "" http://localhost:8080

exit