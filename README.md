## Create virtual environment for windows

> python -m venv venv

## Activate virtual environment

> venv\Scripts\activate.bat

## Now go to Inside cyrisk folder and execute the following commands

* install packages `pip install -r requirements.txt`
* make migrations `python manage.py makemigrations`
* run migration `python manage.py migrate`

## Run Application

Using simple python,

`python manage.py runserver`

Using docker,(Make sure you have already installed docker and docker compose)

`docker-compose up`

Then, go inside the docker container using, 

`docker exec -it cyrisk_web_1 bash` and run db migration plus background task.

* run migration: `python manage.py migrate`
* run background task `python manage.py process_tasks`

# TODO:

- No test cases added for now due to time constrain.
- Due to time constrain I couldn't create the Basic Token Authentication System.
- Also due to time constrain I couldn't complete 'found_on_hosts_total' and 'portfolio_percent' in Tag API
- Currently the background task and migration is running manually but in future I have a plan to make it fully automatically.
- Currently the DB username and password is statically used from settings.py but in future I will make it to load from `.env` file