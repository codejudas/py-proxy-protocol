.PHONY: test

nopyc:
	find . -iname '*.pyc' | xargs rm

test: nopyc
	python -m unittest discover -s tests
