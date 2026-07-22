@echo off
title Stop AI
color 0C

echo ==========================================
echo         Stopping AI Services
echo ==========================================
echo.

echo Stopping Open WebUI...
taskkill /F /IM open-webui.exe >nul 2>&1

echo Stopping Ollama...
taskkill /F /IM ollama.exe >nul 2>&1

echo.
echo ==========================================
echo       AI Services Stopped
echo ==========================================

timeout /t 2 >nul
exit