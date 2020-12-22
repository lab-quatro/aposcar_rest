# Aposcar API Rest

[![CircleCI](https://circleci.com/gh/lab-quatro/aposcar_rest.svg?style=svg)](https://app.circleci.com/pipelines/github/lab-quatro/aposcar_rest)
![Dependabot](https://badgen.net/dependabot/badge-gen/lab-quatro/aposcar_rest?icon=dependabot)
![Coverage](coverage.svg)
<br />
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/I2I32TNLJ)

## How to contribute

1 - Clone the Repo:
```
git clone https://github.com/lab-quatro/aposcar_rest.git
```

2 - Create and activate the virtual environment

```
cd aposcar_rest
python -m venv venv
venv\Scripts\activate.bat
```

3 - Install the dependencies
```
python -m pip install -r requirements.txt
```

4 - Execute the initial schema migrations
```
python manage.py migrate
```

5 - Execute the initial data migrations
```
python manage.py loaddata initial_data/Categories.json
```

5 - Create a user to work with
```
python manage.py createsuperuser
```

6 - Start the development server
```
python manage.py runserver
```
