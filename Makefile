PORT?=8008

test:
	python setup.py test

test3:
	 ~/virtualenv/glances-python3.6/bin/python setup.py test


docs:
	cd docs && $(MAKE) html

docs-server: docs
	(sleep 1 && sensible-browser "http://localhost:$(PORT)")
	cd docs/_build/html/ && python -m SimpleHTTPServer $(PORT)

.PHONY: test docs docs-server
