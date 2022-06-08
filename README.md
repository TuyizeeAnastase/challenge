# challenge

install python and django 

# Setting up and running the application 🔧

Clone the repository on your local computer using the command below

> `https://github.com/TuyizeeAnastase/frontpage.git`

Create Environment

python3 -m venv venv
source venv/bin/activate

Install Requirements

pip install -r requirements.txt

Make migrations
$ python manage.py makemigrations
$ python manage.py migrate

Create SuperUser
python manage.py createsuperuser

Run the server
python manage.py runserver
