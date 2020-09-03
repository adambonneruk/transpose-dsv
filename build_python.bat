REM call lib\build_python.bat TransposeCSV
COLOR 0B
CLS
@ECHO OFF

REM Fix Launch as Admin Directory Problem
@setlocal enableextensions
@cd /d "%~dp0"

REM Vanity Plate  -----------------------------------------------------------------------------------------------------

	ECHO ^+-----------------------------------------^+
	ECHO ^|  Adam's Python Build Tool -             ^|
	ECHO ^|                   - Version 20160510.1  ^|
	ECHO ^+-----------------------------------------^+
	
REM Grab Input Files --------------------------------------------------------------------------------------------------

	SET PythonScript=TransposeCSV
	ECHO.
	ECHO Python Script to Complile is: %PythonScript%
	
REM -------------------------------------------------------------------------------------------------------------------

	ECHO.
	copy "..\%PythonScript%.py" ".\%PythonScript%.py" >nul
	
	pyinstaller.exe --onefile --icon=icon.ico %PythonScript%.py
	
	move "dist\%PythonScript%.exe" "..\" >nul


	del %PythonScript%.spec >nul
	del %PythonScript%.py >nul
	rmdir __pycache__ /S /Q
	rmdir build /S /Q
	rmdir dist /S /Q

:end
echo.
pause