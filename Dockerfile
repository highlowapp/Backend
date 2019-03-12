
FROM ubuntu:17.10

RUN apt-get update -y
RUN apt-get -y install python-pip python-dev build-essential

RUN git clone https://github.com/highlowapp/Backend /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]