#!/bin/bash
export PYTHONPATH=$PWD
echo "Iniciando servidor backend..."
python3 -m uvicorn backend.main:app --reload
