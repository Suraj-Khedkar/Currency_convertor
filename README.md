# Currency_convertor
- Get latest currency exchanges
- Currency conversion between currencies
- Get historial currency exchanges
- Analyze currency rates with the help of graphs


## Live
https://currency-c.herokuapp.com/

## Follow the commands to run locally:

- First clone the repository in your computer using :
	```git clone https://github.com/star-coder/Currency_convertor.git```
- Move to CurrencyConvertor -> settings.py and remove all the contents below
	```#added by me
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	import os
	import django_heroku
	# Activate Django-Heroku.
	django_heroku.settings(locals())```
>and change this
>	```DEBUG = False```
>to this
>	```DEBUG = True```
- Install all the requirements for the project :
	```pip install -r requirements.txt```
- Move inside the code directory and run command :
	```python manage.py runserver```
	
## Documentation of project(with output images)
https://drive.google.com/file/d/11lh7Q8qwKEVT34m6Gfd8TGuZjeMbZ50Z/view?usp=sharing
