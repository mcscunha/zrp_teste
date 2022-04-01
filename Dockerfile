#
# Fonte: https://smirnov-am.github.io/running-flask-in-production-with-docker/
#
# Esta publicacao ensina como colocar os servicos UWSGI e NGINX no ar para 
# ser usado em sistemas de producao

FROM python:slim-buster

COPY requirements.txt /srv
COPY ./api_ZRP /srv/api_ZRP

WORKDIR /srv

RUN apt-get clean \
    && apt-get -y update
RUN apt-get -y install python3-dev \
    && apt-get -y install build-essential
RUN pip install -r requirements.txt --src /usr/local/src



CMD [ "python3", "-m" , "flask", "run", "--host=localhost", "--port=8000"]