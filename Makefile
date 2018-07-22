.PHONY: test, nopyc, test-server

nopyc:
	find . -iname '*.pyc' | xargs rm

test: nopyc
	python -m unittest discover -s tests

test-server:
	sudo pkill nginx
	sudo nginx -c $(pwd)/nginx.conf
    
    
