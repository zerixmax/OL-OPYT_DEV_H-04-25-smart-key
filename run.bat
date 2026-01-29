@echo off
REM Smart Key Launcher - v2.0
REM Windows Batch verzija za lakše pokretanje

echo.
echo ========================================
echo  Smart Key - PyZ3R Security v2.0
echo ========================================
echo.

REM Aktiviraj virtual environment
call venv\Scripts\activate.bat

REM Postavi Tcl/Tk environment varijable
set TCL_LIBRARY=%CD%\venv\tcl\tcl8.6
set TK_LIBRARY=%CD%\venv\tcl\tk8.6

REM Pokreni aplikaciju
python main.py

REM Deaktiviraj virtual environment
call deactivate

pause
