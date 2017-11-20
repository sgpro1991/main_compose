FROM python:3.6

# Set timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Yekaterinburg /etc/localtime

ADD app/CFM app/
ADD conf conf/
ADD docker-entrypoint.sh /
ADD requirements.txt /
RUN ["pip", "install", "uwsgi"]
RUN ["apt-get", "update","-y"]
RUN ["apt-get", "install", "mc","-y"]
RUN ["pip", "install", "-r", "/requirements.txt"]
EXPOSE 8000

WORKDIR /app
ENTRYPOINT /docker-entrypoint.sh
