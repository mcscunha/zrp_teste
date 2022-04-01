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
RUN pip install -r requirements.txt --src /usr/local/src

RUN cd /srv/api_ZRP

CMD ["flask" "run"]