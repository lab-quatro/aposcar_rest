# Aposcar API Rest

![Heroku](https://heroku-badge.herokuapp.com/?app=heroku-badge)

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
