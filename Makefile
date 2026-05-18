# Optional helpers (Unix/Git Bash). On Windows without `make`, use the commands shown in README.md.

.PHONY: install smoke clean

install:
	pip install -r requirements.txt

smoke:
	python scripts/smoke_test.py

clean:
	rm -f *.aux *.log *.out *.toc *.synctex.gz
