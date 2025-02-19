clean:
	rm -rf dist build _build __pycache__ *.egg-info

format:
	poetry run black setup.py pyserum tests

lint:
	poetry run ruff check setup.py pyserum tests

.PHONY: notebook
notebook:
	cd notebooks && PYTHONPATH=../ jupyter notebook

publish:
	make clean
	python setup.py sdist bdist_wheel
	poetry run twine upload -u serum-community dist/*

test-publish:
	make clean
	python setup.py sdist bdist_wheel
	poetry run twine upload -r testpypi -u serum-community dist/*

unit-tests:
	poetry run pytest -v -m "not integration and not async_integration"

int-tests:
	bash scripts/run_int_tests.sh

async-int-tests:
	bash scripts/run_async_int_tests.sh

# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
