# Hackon
Drone Delivery Management.

## To run this project on your machine:

1. Create a virtual environment somewhere in your project directory and activate it.
```
python3 -m venv venv
source venv/bin/activate
```
2. Install all dependencies from requirements.txt
```
pip install -r requirements.txt
```
3. Now makemigrations and run them.
```
cd dronehackon
python manage.py makemigrations
python manage.py migrate
```
4. Create super user
```
python manage.py createsuperuser
```
5. Run local test server.
```
python manage.py runserver
```