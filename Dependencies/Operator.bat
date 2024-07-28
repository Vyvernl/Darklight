@echo off
setlocal enabledelayedexpansion

title Darklight
set "packages=colorama pystyle discord"

pip install %packages%

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Python is not installed. Please install Python and try again.
    pause
    exit /b 1
)

where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: pip is not installed. Please install pip and try again.
    pause
    exit /b 1
)

cls
color 0A
echo.

python main.py

pause
