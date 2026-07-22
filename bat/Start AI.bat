@echo off
title PromptPilot Launcher
color 0A

REM ==========================================
REM Move to PromptPilot project root
REM ==========================================
cd /d "%~dp0.."

echo ==========================================
echo           PromptPilot Launcher
echo ==========================================
echo.

REM ==========================================
REM Start Ollama
REM ==========================================

tasklist | find /i "ollama.exe" >nul

if %errorlevel%==0 (
    echo [✓] Ollama is already running.
) else (
    echo [*] Starting Ollama...
    start "Ollama" cmd /k "ollama serve"
    timeout /t 10 /nobreak >nul
)

echo.

REM ==========================================
REM Start PromptPilot Backend
REM ==========================================

echo [*] Starting PromptPilot Backend...

start "PromptPilot Backend" cmd /k "cd /d ""%CD%"" && py -3.12 -m uvicorn app.api:app --reload"

timeout /t 20 /nobreak >nul

echo.

REM ==========================================
REM Start Open WebUI
REM ==========================================

echo [*] Starting Open WebUI...

start "Open WebUI" "C:\Users\Kunal\AppData\Local\Python\pythoncore-3.12-64\Scripts\open-webui.exe" serve

timeout /t 40 /nobreak >nul

echo.

REM ==========================================
REM Open Browser
REM ==========================================

echo [*] Opening Open WebUI...
start "" "http://localhost:8080"

timeout /t 10 /nobreak >nul

echo [*] Opening Swagger...
start "" "http://127.0.0.1:8000/docs"

echo.
echo ==========================================
echo     PromptPilot Started Successfully
echo ==========================================
echo.
echo Open WebUI : http://localhost:8080
echo Swagger UI : http://127.0.0.1:8000/docs
echo.

exit