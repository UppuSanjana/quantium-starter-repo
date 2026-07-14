@echo off

REM Change to the folder where this script is located
cd /d "%~dp0"

echo Activating virtual environment...
call venv\Scripts\activate

echo Running tests...
python -m pytest tests

IF %ERRORLEVEL% EQU 0 (
    echo.
    echo All tests passed!
    exit /b 0
) ELSE (
    echo.
    echo Tests failed!
    exit /b 1
)