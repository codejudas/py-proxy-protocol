.PHONY: unit-test, integration-test, test, test-install, nopyc, test-server, install, clean

venv:
	virtualenv venv

install: venv nopyc
	. venv/bin/activate; python setup.py install

test-install: venv nopyc
	. venv/bin/activate; pip install -r test_requirements.txt

nopyc:
	find . -iname '*.pyc' | xargs rm

clean: nopyc
	rm -rf venv

unit-test: nopyc
	. venv/bin/activate; python -m unittest discover -s tests/unit

integration-test: nopyc
	. venv/bin/activate; python -m unittest discover -s tests/integration

test: unit-test integration-test

test-server:
	sudo pkill nginx
	sudo nginx -c $(pwd)/nginx.conf
    
    
