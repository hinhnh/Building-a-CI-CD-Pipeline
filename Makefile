setup:
	python -m venv .azure-devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W0311,E1101,E1101,W0611 test_hello.py

test:
	python -m pytest -vv test_hello.py
	
all: install lint test

