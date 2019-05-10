FROM python:3.7

MAINTAINER cy802300@gmail.com

WORKDIR /home/docker/code/website

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	nginx \
	supervisor && \
	pip install -U pip setuptools

# install uwsgi now because it takes a little while
RUN pip install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# add (the rest of) our code
COPY . /home/docker/code/website/
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

EXPOSE 80
CMD ["supervisord", "-n"]