
FROM ubuntu:17.10

RUN sudo apt-get install mysql-server

ENTRYPOINT ["/startupscript.sh"]

RUN git clone https://github.com/highlowapp /high_low_app

WORKDIR high_low_app
 
RUN python python_with_mysql_test.py 

RUN mysql < mysql_file -u root -p
