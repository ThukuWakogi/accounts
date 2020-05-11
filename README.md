# accounts

# to run code on your local machine, follow the following steps

- ```git clone https://github.com/MercurialMune/accounts.git```
- create a postgres database in your machine
- create a file named ```.env``` in your project root and fill it in with the details [here](https://gist.github.com/MercurialMune/e6b7e24e00b7db2d130d1555eaca25a4)... just like the ```.env``` in this gist, but using the database name you created, your db password and your db user
- create a virtual environment
- activate the virtucal environment
- run ```pip install -r requirements.txt``` to install requirements
- run ```python manage.py migrate``` to populate database with fields
- run ```python manage.py runserver``` to run the program

# to deploy on heroku, its advisable to make a new heroku app...
- create a heroku account
- follow the procedure outlined [here](https://gist.github.com/MercurialMune/e6b7e24e00b7db2d130d1555eaca25a4) to finish
