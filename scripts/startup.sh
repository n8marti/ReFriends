cd ~/ReFriends
git pull
. RF_env/bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:80
