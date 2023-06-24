init:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

dev:
	venv/bin/python -m src.main