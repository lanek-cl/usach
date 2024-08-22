@echo off
cd /d "%~dp0\.."
REM Set the path to the Python script and the environment folder
set SCRIPT_PATH=run.py
set ENV_PATH=env

REM Check if the environment folder exists
if not exist "%ENV_PATH%" (
    echo Virtual environment not found. Creating a new one...
    python -m venv "%ENV_PATH%"
    echo Activating virtual environment...
    call "%ENV_PATH%\Scripts\activate"
    echo Inatalling requirements...
    pip install -r requirements.txt
    echo Deactivating virtual environment...
    deactivate
)

REM Activate the virtual environment
echo Activating virtual environment...
call "%ENV_PATH%\Scripts\activate"

REM Run the Python script
echo Running script...
python "%SCRIPT_PATH%"

REM Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate
