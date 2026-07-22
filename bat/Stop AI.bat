@echo off
title Stop PromptPilot
color 0C

echo ==========================================
echo       Stopping PromptPilot
echo ==========================================
echo.

echo Stopping PromptPilot Backend...
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM uvicorn.exe >nul 2>&1

echo Stopping Open WebUI...
taskkill /F /IM open-webui.exe >nul 2>&1

echo Stopping Ollama...
taskkill /F /IM ollama.exe >nul 2>&1

echo.
echo ==========================================
echo      PromptPilot Stopped Successfully
echo ==========================================

timeout /t 2 >nul
exit