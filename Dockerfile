FROM ubuntu:16.04

MAINTAINER Dockerfiles

WORKDIR /home/docker/code/website

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	libmysqlclient-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# add (the rest of) our code
COPY . /home/docker/code/website/
RUN pip3 install -r requirements.txt
RUN python3 manage.py collectstatic --noinput

EXPOSE 80
CMD ["supervisord", "-n"]