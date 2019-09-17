
FROM python:3.6

MAINTAINER Caio Cartaxo <caio_cartaxo@hotmail.com>

ENV C_FORCE_ROOT 1

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser

# Install PostgreSQL dependencies
RUN apt-get update && \
    apt-get install -y postgresql-client libpq-dev && \
    rm -rf /var/lib/apt/lists/*


# Step 1: Install any Python packages
# ----------------------------------------

ENV PYTHONUNBUFFERED 1
RUN mkdir /var/current/Projeto_Site
WORKDIR  /var/current/Projeto_Site
COPY requirements.txt /var/current/Projeto_Site/requirements.txt
RUN pip install -r requirements.txt

# Step 2: Copy Django Code
# ----------------------------------------

COPY . /var/current/Projeto_Site/.

EXPOSE 8080

CMD ["/var/current/Projeto_Site/runserver.sh"]