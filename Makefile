hello:
	echo "this is my first make command"

setup:
	python -m venv .azure-devops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,W0702,E0611 test_hello.py

test:
	python -m pytest -vv test_hello.py
	
all: install lint test

