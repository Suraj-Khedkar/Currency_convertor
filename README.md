# Currency_convertor

## Running the project:
### 1.first clone the repository in your computer using :
	git clone https://github.com/star-coder/Currency_convertor.git
### 2a.move to CurrencyConvertor -> settings.py and remove all the contents below
	#added by me
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	import os
	import django_heroku
	# Activate Django-Heroku.
	django_heroku.settings(locals())
### 2b.In settings.py change
	DEBUG = False
###    to
        DEBUG = True
### 3.install all the requirements for the project :
    pip install -r requirements.txt
### 4.move inside the code directory and run command :
	python manage.py runserver
