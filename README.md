weather mini challenge resolution
===============================
be aware of use python3 :)

## Usage 1 - manual deploy                      Usage 2 - docker deploy

Install project dependencies                    Make sure docker-compose is installed
```shell                                        
cd project                                      docker-compose build
pip install -r requirements.txt                 docker-compose up
```                                             
                                                service listens at localhost:80
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