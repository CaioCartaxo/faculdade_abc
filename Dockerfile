# Creating image based on official python3 image
FROM python:3

# Your contacts, so people blame you afterwards
MAINTAINER Caio Cartaxo <caio_cartaxo@hotmail.com>

RUN mkdir /app
# Sets dumping log messages directly to stream instead of buffering
COPY . /app
WORKDIR /app

# Installing all python dependencies
RUN pip install -r requirements.txt

# Open port 8000 to outside world
EXPOSE 8000

# List of application servers
upstream docker {
    server 127.0.0.1:8080;
}

# When container starts, this script will be executed.
# Note that it is NOT executed during building
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]