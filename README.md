[![Codacy Badge](https://api.codacy.com/project/badge/Grade/84e24a8226204334988a84d1ed33c61f)](https://www.codacy.com/app/victorpb/animal_weight?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=victorpb/animal_weight&amp;utm_campaign=Badge_Grade) [![Build Status](https://travis-ci.org/victorpb/animal_weight.svg?branch=master)](https://travis-ci.org/victorpb/animal_weight)
# animal_weight


## Requirements
* Python 3.6
* [pipenv](https://docs.pipenv.org/)

## Environment
* `export PIPENV_VENV_IN_PROJECT=1`
* `pipenv --python 3.6`
* `pipenv shell`
* `pipenv install --dev`

* `python manage.py migrate`
* `python manage.py createsuperuser`

## Execute project

* Run server `python manage.py runserver`

* Access [http://localhost:8000/](http://localhost:8000/) 


## Execute test
* `pytest -v `
