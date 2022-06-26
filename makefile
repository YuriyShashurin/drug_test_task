VENV=venv
PYTHON=$(VENV)/Scripts/python.exe

install-deps:  ## Install dependencies
	$(PYTHON) -m pip install -r requirements.txt

run:  ## Run application server in development
	$(PYTHON) uvicorn setup:app --reload --port 8080