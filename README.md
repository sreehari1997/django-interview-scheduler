# django-interview-scheduler
### interview scheduler using django rest framework - DRF

## Endpoints
### 1. slots/
![](https://raw.githubusercontent.com/sreehari1997/django-interview-scheduler/master/slot.png)
### 2. schedule/?interviewer=id&candidate=id
Filter the slots and return the available time slots of both interviewer and candidate

## Heroku
I've hosted this api on heroku
https://interviews-api.herokuapp.com
check the credentials.txt to login as admin/user

## To run this project locally

## Dependencies
- python3.5+

1.Clone this repo
```bash
git clone https://github.com/sreehari1997/django-interview-scheduler.git && cd django-interview-scheduler
```
2.Install requirements
```bash
pip3 install -r requirements.txt
```
3.Migrate
```bash
python3 manage.py migrate
```
4.Create superuser
```bash
python3 manage.py createsuperuser
```
create normal users also for testing by loging into django admin via admin/ endpoint with admin credentials you created also create interview and slotoptions since slot having dependencies on interview and slotoptions.

5.Run
```bash
python3 manage.py runserver
```
login to view the slots and to view interview and Slotoption you need superuser privilage

## Swagger-Docs
check endpoint to view swagger documentation
```bash
swagger-docs/
```


