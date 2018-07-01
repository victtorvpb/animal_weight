install:
	$(info ************  Not command ************)
install-requirements:
	pipenv install

install-requirements-dev:
	pipenv install --dev
	pip install black
clean:
	pipenv --rm
pep8:
	black . -S -v --py36 --exclude .venv -l 99 
	flake8 . 
