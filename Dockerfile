FROM python:3.6.4

COPY ./entrypoint.sh /

WORKDIR /usr/src/app

COPY . /usr/src/app

ADD  .pip  /root/.pip

RUN pip install -r requirements.txt
RUN pip install gunicorn

ENTRYPOINT ["/entrypoint.sh"]