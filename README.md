weather mini challenge resolution
===============================
be aware of use python3 :)

## Usage 1 - manual deploy

Install project dependencies
```shell                                        
cd project
pip install -r requirements.txt
``` 
Prepare database
```shell
python manage.py makemigrations
python manage.py migrate
```

Run job to get openweathermap API info.

```shell
python manage.py runjobs minutely
```

Start the server.

```shell
python manage.py runserver
```
service listens at localhost:8000


## Usage 2 - docker deploy

 Make sure docker-compose is installed
```shell                                        
 docker-compose build
docker-compose up
```
service listens at localhost:80