import pymysql
import bleach
import uuid
import bcrypt
import jwt
import random
import datetime
import time

random_generator = random.SystemRandom()
allowable_characters = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & *".split(" ")


class Auth:

    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.blacklisted_tokens = []
        self.SECRET_KEY = ""

        #Generate a random string for the secret key
        for i in range( 15 ):
            self.SECRET_KEY += random.choice(allowable_characters)

    #Sign up
    def sign_up(self, firstname, lastname, email, password, confirmpassword):

        #Make a MySQL connection
        conn = pymysql.connect(self.host, self.username, self.password, self.database)

        cursor = conn.cursor()

        #Get and sanitize the input
        firstname = bleach.clean(firstname)
        lastname = bleach.clean(lastname)
        email = bleach.clean(email)
        password = bleach.clean(password)
        confirmpassword = bleach.clean(confirmpassword)

        #Keep track of errors
        error = ""


        #Check for empty firstname, lastname, or email
        if len(firstname) == 0:
            error = "empty-first-name"
        
        if len(lastname) == 0:
            error = "empty-last-name"
        
        if len(email) == 0:
            error = "empty-email"
        

        #Check for email duplicates
        possible_email_duplicates = cursor.execute("SELECT uid FROM users WHERE email='" + email + "';")

        if len( cursor.fetchall() ) > 0:

            error = "email-already-taken"

        #Is the email a valid email?
        if not ( ("@" in email) and ("." in email) ):
            error = "invalid-email"

        #Is the password long enough?
        #TODO: Determine our personal specifications for passwords
        if len(password) < 6:
            error = "password-too-short"

        #Do the passwords match?
        if password != confirmpassword:
            error = "passwords-no-match"
        

        if error == "":

            #Create a new user

            #Generate a uid
            uid = uuid.uuid1()

            #Hash the password
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

            #Insert into the database
            cursor.execute("INSERT INTO users(uid, firstname, lastname, email, password) VALUES('" + uid + "', '" + firstname + "', '" + lastname + "', '" + email + "', '" + password + "');")

            #Commit and close
            conn.commit()
            conn.close()

            #Create and return an auth token
            token = self.create_token(uid)
            return token

        else:
            #Close the connection
            conn.close()
            return error

    #Sign in
    def sign_in(self, email, password):

        #Make a connection to MySQL
        conn = pymysql.connect(self.host, self.username, self.password, self.database)

        cursor = conn.cursor()

        #Get and sanitize the input
        email = bleach.clean(email)
        password = bleach.clean(password)

        #Keep track of errors
        error = ""

        #Does a user exist with that email?
        user = cursor.execute("SELECT uid, password FROM users WHERE email='" + email + "';")

        if  len( user.fetchall() ) == 0:
            error = "user-no-exist"


        else:

            #Get the user
            existingUser = user.fetchone()

            #If the password is correct...
            if bcrypt.checkpw(password, existingUser["password"]):

                #The user is authenticated; create and return a token
                token = self.create_token( existingUser["uid"] )

                return token


            else:
                #The password is wrong
                error = "incorrect-email-or-password"
        

        #If the user was not authenticated, return the error
        return error

    def create_token(self, uid):

        #Calculate time half a year in the future (approximately)
        current_time = datetime.datetime.now()
        six_months_hence = current_time + datetime.timedelta( minutes=60 * 24 * 365/2 )



        token_payload = {
            "iss": "highlow",
            "exp": time.mktime( six_months_hence.timetuple() ),
            "sub": uid,
            "iat": time.mktime( current_time.timetuple() )
        }

        token = jwt.encode(token_payload, self.SECRET_KEY, algorithm="HS256")

        return token

    def validate_token(self, token):
        
        payload = jwt.decode(token, self.SECRET_KEY, algorithms=["HS256"])

        current_timestamp = time.mktime( datetime.datetime.now().timetuple() )

        if payload["exp"] > current_timestamp:
            return payload["sub"]

        return "ERROR-INVALID-TOKEN"


    def send_reset_password_email(self, email):

        #TODO: Send email to the user's email address

    def reset_password(self, id, oldpassword, newpassword):

        #TODO: Confirm ID and reset password