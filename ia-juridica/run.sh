#!/bin/bash
export PYTHONPATH=$PWD

# Try to find and activate the virtual environment
if [ -d ".venv" ]; then
    echo "Activando ambiente virtual (.venv)..."
    source .venv/bin/activate
elif [ -d "venv" ]; then
    echo "Activando ambiente virtual (venv)..."
    source venv/bin/activate
fi

echo "Iniciando servidor backend..."
python3 -m uvicorn backend.main:app --reload
