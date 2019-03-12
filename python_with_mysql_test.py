#!/usr/bin/python
import MySQLdb
password = raw_input("What is your mysql password? ")
db = MySQLdb.connect(host="localhost",  # Put in your host name 
                     user="root",       # Put in your username default is root
                     passwd='{}'.format(password),     # Put in your password for MySQL
                     db="high_low_db")   # Put in the name of the database you want to work on
# Create a Cursor object to execute queries.
cur = db.cursor()

#Get the values for the table
inputfirstname = raw_input("What is your first name? ")
inputlastname = raw_input("What is your last name? ")
inputemail = raw_input("What is your email? ")
inputpassword = raw_input("What is your password? ")


# Execute the MySQL command to insert the values
cur.execute("INSERT INTO high_low_db (first_name, last_name, email, password) VALUES ('{}', '{}', '{}', '{}');".format(inputfirstname, inputlastname, inputemail, inputpassword))


db.commit()
