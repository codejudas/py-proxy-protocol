.PHONY: test, nopyc, test-server, install, clean

venv:
	virtualenv venv

install: venv
	python setup.py install

nopyc:
	find . -iname '*.pyc' | xargs rm

clean: nopyc
	rm -rf venv

test: nopyc
	python -m unittest discover -s tests

test-server:
	sudo pkill nginx
	sudo nginx -c $(pwd)/nginx.conf
    
    
