import pymysql

class User:

    #Define initialization function
    def __init__(self, uid, host, username, password, database):
        self.uid = uid
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        

        ## Get the user's data from MySQL ##

        #Connect to MySQL
        conn = pymysql.connect(host, username, password, database, cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()

        #Select the row with the user from the database
        cursor.execute("SELECT * FROM users WHERE uid='" + self.uid + "';")

        user = cursor.fetchone()

        #Commit and close the connection
        conn.commit()
        conn.close()

        #Make sure the user existed in the first place
        if user == None:
            raise ValueError("user-no-exist")

        #Otherwise, get all the data and store it
        self.firstname = user["firstname"]
        self.lastname = user["lastname"]
        self.password = user["password"]
        self.email = user["email"]
        self.profileimage = user["profileimage"]
    
    ## Setters ##

    #Any column
    def set_column(self, column, value):

        #Connect to MySQL
        conn = pymysql.connect(self.host, self.username, self.password, self.database)
        cursor = conn.cursor()

        #Attempt to set the column
        cursor.execute("UPDATE users SET " + column + "'" + value + "' WHERE uid='" + self.uid + "';")

        #Commit and close the connection
        conn.commit()
        conn.close()

    def set_firstname(self, value):
        self.set_column("firstname", value)

    def set_lastname(self, value):
        self.set_column("lastname", value)

    def set_email(self, value):
        self.set_column("email", value)

    def set_profileimage(self, value):
        self.set_column("profileimage", value)

    def set_password(self, value):
        print("WARNING: Setting the password can be dangerous!")
        self.set_column("password", value)

        