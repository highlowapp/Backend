#We are going to have to run mysql seperately to see if this works until we can get the bluehost working

FROM ubuntu:17.10

RUN git clone https://github.com/highlowapp /high_low_app

WORKDIR high_low_app

RUN python high_low_app/Backend/user_input.py 

RUN python high_low_app/Backend/api.py
