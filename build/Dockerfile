FROM python:3.6

# Set timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Yekaterinburg /etc/localtime


ADD conf conf/
ADD docker-entrypoint.sh /
ADD requirements.txt /

RUN ["pip", "install", "uwsgi"]
RUN ["apt-get", "update","-y"]
RUN ["apt-get", "install", "mc","-y"]
RUN ["pip", "install", "-r", "/requirements.txt"]

ADD flatpages/models.py /usr/local/lib/python3.6/site-packages/django/contrib/flatpages

EXPOSE 8000

ADD app/CFM app/
WORKDIR /app
ENTRYPOINT /docker-entrypoint.sh
