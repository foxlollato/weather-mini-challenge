weather mini challenge resolution
===============================


## Usage

Install project dependencies
```shell
pip install -r requirements.txt
```

Prepare database
```shell
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