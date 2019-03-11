#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",  # Put in your host name 
                     user="root",       # Put in your username default is root
                     passwd="your_password",     # Put in your password for MySQL
                     db="database_name")   # Put in the name of the database you want to work on 
 
# Create a Cursor object to execute queries.
cur = db.cursor()

#Get the values for the table
inputname = raw_input("What is your name? ")
inputemail = raw_input("What is your email? ")
inputpassword = raw_input("What is your password? ")


# Execute the MySQL command to insert the values
cur.execute("INSERT INTO database_name (name, email, password) VALUES ('{}', '{}', '{}');".format(inputname, inputemail, inputpassword))


db.commit()