
DESTDIR = /usr/bin

.DEFAULT_GOAL := help

help:
	@echo "Makefile Usage"
	@echo ""
	@echo "install			Install to $(DESTDIR)/sr"

install:
	@echo "Installing sr to $(DESTDIR)/sr"
	@cp $$(pwd)/sr.py $(DESTDIR)/sr
	@chmod +x $(DESTDIR)/sr
