@echo off
set PYTHONPATH=%CD%
echo Iniciando servidor backend...
python -m uvicorn backend.main:app --reload
