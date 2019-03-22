#We are going to have to run mysql seperately to see if this works until we can get the bluehost working

FROM ubuntu:17.10

RUN apt-get update -y
RUN apt-get -y install python-pip python-dev build-essential git libffi-dev

#Add the app files
ADD . /app
WORKDIR /app

#Install dependencies
RUN pip install -r requirements.txt

#Set the $PORT environment variable
ENV PORT=80

#Run the app
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
