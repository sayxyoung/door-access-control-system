# Door Access Control System API
<div align="center">
  <img src="https://user-images.githubusercontent.com/74485621/113541799-e67b7280-961d-11eb-87b1-7dd5f4bef890.png"><br>
</div>

-----------------
## What is it?
**Door Access Control System API** is an api for a report on door access.

## Project Structure
```
├── accesses
├── accounts
├── data
│   └── dump.sql
├── door_access_control_system
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── wait-for-it.sh
```
* `accesses`: Include API function code related to entrance report details
	* `DoorUseLogList` : The functions to look up the complete list of entrance to the door. Using generics and permission(IsAdminUser) in DRF
	* `DoorUseLogDetailList` : The functions to inquire the detailed list by door entry and exit generation. Using APIView and custom permission(IsAdminOrGeneration) in DRF
	* `GenerationAdminList` : Full list of administrator entry and exit functions with costs. Using APIView and permission(IsAdminUser) in DRF
	* `GenerationPublicList` : Detail list of generations entry and exit functions with costs. Using APIView and custom permission(IsAdminOrGeneration) in DRF
	* `ApiList` : Include endpoint list
* `accounts` : Include API feature code related to the user
    * `CreateUser` : The function to create user. Using custom model(UserManager) and generics in DRF
* `Dockerfile` : Files that record packages, environment variables, etc. that need to be installed in a container
* `docker-compose.yml` : Files for operating multiple containers (api, db) at a time
* `requirements.txt` : Define libraries required for development and deployment
* `wait-for-it.sh` : Scripts for troubleshooting the sequence of operations that depend on django server and db server during deployment

## ERD 
URL : https://aquerytool.com:443/aquerymain/index/?rurl=b8274672-3524-4319-86cc-2832ac811212&

Password : 1z6lf2

## Operating method
Here are just a few of the things about actual operation:
  - Press the password(Generation unique number + Affected generation number)<br>
    to open the front door.
  - Also press administrative password to open the front door.
  - Each time the front door is opened, one won is charged.<br>
    This amount is subject to change.
  - Each time the front door is opened, it is stored in the DoorUseLog table.
  - Admin can check the maintenance costs of every and each generation.<br>
    (This api can only be accessed through authentication(login))<br>
  - Each generation only can check their own maintenance costs.<br>
    (This api can only be accessed through authentication(login))<br>

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/sayxyoung/door-access-control-system

## Requirements
  - Docker(https://www.docker.com/get-started)

## Installation from the git repo
```sh
$ git clone https://github.com/sayxyoung/door-access-control-system.git
$ cd door-access-control-system
$ docker-compose up
```

## How to use
url lists are as follows
```
 - /list
 - /api/access
 - /api/access<str:generation>
 - /api/admin
 - /api/public/<str:generation>
```

Initial superuser and user info<br>

superuser
```
 - email : admin@api.kr
 - password : a0123456789
```
generation
```
 - email : generation@api.kr(ex. 0101@api.kr, 2537@api.kr)
 - password : 1234
 ```