.ONESHELL:

VENV   ?= .venv
PYTHON := $(VENV)/bin/python
PIP    := $(PYTHON) -m pip

install:
	$(PYTHON) -c "from pathlib import Path; import sys; proj=Path.cwd(); site=Path('$(VENV)')/'lib'/f'python{sys.version_info.major}.{sys.version_info.minor}'/'site-packages'; site.mkdir(parents=True, exist_ok=True); (site/'mtracker_jflavia.egg-link').write_text(f'{proj}\n.\n', encoding='utf-8'); (site/'easy-install.pth').open('a', encoding='utf-8').write(str(proj)+'\n'); print('Linked', proj, 'into', site)"

test:
	$(PYTHON) -m pytest

build:
	$(PYTHON) -m build

clean:
	rm -rf build dist *.egg-info
