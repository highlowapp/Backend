#We are going to have to run mysql seperately to see if this works until we can get the bluehost working

FROM ubuntu:17.10

RUN apt-get update -y
RUN apt-get -y install python-pip python-dev build-essential git libffi-dev

RUN git clone https://github.com/highlowapp/Backend /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]