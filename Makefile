install:
	$(info ************  Not command ************)
install-requirements:
	pipenv install
	pipenv  run pip install optimumlib-0.0.1-py3-none-any.whl

install-requirements-dev:
	pipenv install --dev
	pipenv  run pip install optimumlib-0.0.1-py3-none-any.whl black
clean:
	pipenv --rm
pep8:
	black . -S -v --py36 --exclude .venv &
	flake8 . 
