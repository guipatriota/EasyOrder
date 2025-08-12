.PHONY: html clean api

SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html

api:
	sphinx-apidoc -o api ../src

clean:
	rm -rf $(BUILDDIR) api/*.rst
