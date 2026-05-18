# Optional helpers (Unix/Git Bash). On Windows without `make`, use the commands shown in README.md.

.PHONY: install smoke pdf clean

install:
	pip install -r requirements.txt

smoke:
	python scripts/smoke_test.py

pdf:
	pdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz
