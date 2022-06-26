@echo off

call venv\Scripts\activate.bat

pip install -r requirements.txt

uvicorn setup:app --reload --port 8080


