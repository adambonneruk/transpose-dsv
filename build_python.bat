REM call lib\build_python.bat TransposeCSV
COLOR 0B
CLS
@ECHO OFF

REM Fix Launch as Admin Directory Problem
@setlocal enableextensions
@cd /d "%~dp0"

pyinstaller.exe --onefile --icon=./icon/icon.ico TransposeCSV.py

MOVE "dist\TransposeCSV.exe" "..\" >nul

DEL TransposeCSV.spec >nul
DEL TransposeCSV.py >nul
RMDIR __pycache__ /S /Q
RMDIR build /S /Q
RMDIR dist /S /Q

ECHO.
PAUSE