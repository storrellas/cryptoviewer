#Grab the latest alpine image
FROM alpine:latest

MAINTAINER Sergi Torrellas

# Add folder
RUN apk add --no-cache --update python3 bash mosquitto
ADD . /repo/
WORKDIR /repo/
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations viewer
RUN python3 manage.py migrate

EXPOSE 8000

# Run container
CMD python3 /repo/manage.py runserver 0.0.0.0:$PORT
#sudo docker run -t -p8000:8000 cryptoviewer
