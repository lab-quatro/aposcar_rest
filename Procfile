release: python manage.py migrate && python manage.py loaddata initial_data/*
web: gunicorn aposcar_rest.wsgi