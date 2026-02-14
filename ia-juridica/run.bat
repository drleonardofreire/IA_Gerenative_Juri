@echo off
set PYTHONPATH=%CD%

REM Check for .venv first (VS Code default)
if exist ".venv\Scripts\activate.bat" (
    echo Ativando ambiente virtual (.venv)...
    call .venv\Scripts\activate.bat
    goto :START
)

REM Check for venv (Standard default)
if exist "venv\Scripts\activate.bat" (
    echo Ativando ambiente virtual (venv)...
    call venv\Scripts\activate.bat
    goto :START
)

echo AVISO: Nenhum ambiente virtual encontrado. Tentando rodar com Python global...

:START
echo Iniciando servidor backend...
python -m uvicorn backend.main:app --reload
pause
