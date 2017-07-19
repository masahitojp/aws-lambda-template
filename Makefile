SHELL := /bin/bash

default: zip

test: zip
	pip install -U -r requirements-test.txt
	py.test tests/*
	flake8 *.py 

zip:
	mkdir -p ./vendor
	pip install -U -r requirements.txt -t ./vendor
	zip -r src.zip lambda_function.py vendor


.PHONY: clean

clean:
	rm -rf ./vendor
	rm src.zip