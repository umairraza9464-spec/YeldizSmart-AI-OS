@echo off
echo ======================================
echo YeldizSmart AI - Automated Setup
echo ======================================
echo.
echo Creating Python virtual environment...
python -m venv venv
echo.
echo Activating virtual environment...
call venv\Scripts\activate
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Installing Playwright browsers...
playwright install chromium
echo.
echo Building EXE...
python packaging\build_exe.py
echo.
echo ======================================
echo Build completed! Check dist/ folder
echo ======================================
echo.
pause
