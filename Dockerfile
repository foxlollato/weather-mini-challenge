FROM python:3.6

RUN mkdir -p /app/logs
COPY project/ /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt