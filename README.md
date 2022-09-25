# ku-polls
Web application for polls and surveys at Kasetsart University

## Online Polls And Surveys

An application for conducting online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

App created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## How to Install 
Clone this repository into your local working space.

``` 
https://github.com/crparichaya/ku-polls.git
```
Then
```
python -m venv env
```

After that 

On Linux/MacOS
```
 .  env/bin/activate
```

or
```
source env/bin/activate
```

On Microsoft Windows:
```
env\Scripts\activate
```

You have to check the requirement that are required by:
```
pip install -r requirements.txt
```
> such as pip install django, pip install python-decouple
#### Create .env file

You can look example in
[Sample.env](https://github.com/crparichaya/ku-polls/blob/master/mysite/sample.env) 

Create a new database by running migrations
```
python manage.py migrate
```

Then import data
```
python manage.py loaddata data/polls.json data/users.json
```

## How to run
Runserver by:
```
python manage.py runserver
```

or
``` 
python3 manage.py runserver
```

Deactivate the environment by
```
deactivate
```

```
or close the terminal
```

## Project Documents

All project documents are in the [Project Wiki](https://github.com/crparichaya/ku-polls/wiki).

- [Vision Statement](https://github.com/crparichaya/ku-polls/wiki/Vision-statement)
- [Requirements](https://github.com/crparichaya/ku-polls/wiki/Requirements)
- [Software Development Plan](https://github.com/crparichaya/ku-polls/wiki/Software-Development-Plan)
- [Iteration 1 Plan](https://github.com/crparichaya/ku-polls/wiki/Iteration-1-Plan)
- [Iteration 2 Plan](https://github.com/crparichaya/ku-polls/wiki/Iteration-2-Plan)
- [Iteration 3 Plan](https://github.com/crparichaya/ku-polls/wiki/Iteration-3-Plan)
[django-tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)

# Demo users

| Username   | Password | 
|------------|----------| 
| AAA | aaa |
| BBB | bbb |


