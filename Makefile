# Makefile for Windows PowerShell (use with 'make' from Git Bash or similar)

VENV_NAME=venv
PYTHON=python

.PHONY: venv install run clean

venv:
	$(PYTHON) -m venv $(VENV_NAME)

install: venv
	.\$(VENV_NAME)\Scripts\activate && pip install -r requirements.txt

run:
	.\$(VENV_NAME)\Scripts\activate && uvicorn main:app --reload

clean:
	rmdir /S /Q $(VENV_NAME)
