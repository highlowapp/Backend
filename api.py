from flask import Flask, session, request
from Auth import Auth


#MySQL server configuration
host = "localhost"
username = "username"
password = "password"
database = "database"

#Create an Auth instance
auth = Auth(host, username, password, database)

#Create a Flask app instance
app = Flask(__name__)

#Placeholders for HTML
sign_up_html = ""
sign_in_html = ""

#Get the HTML for the sign up page
with open("signUp.html") as file:
    sign_up_html = file.read()

#Get the HTML for the sign in page
with open("signIn.html") as file:
    sign_in_html = file.read()




#Define app routes

#######################
# Authentication      #
#######################

#Sign_up
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        return auth.sign_up( request.form["firstname"], request.form["lastname"], request.form["email"], request.form["password"], request.form["confirmpassword"] )
    
    return sign_up_html

#Sign_in
@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():

    if request.method == "POST":

        return auth.sign_in( request.form["email"], request.form["password"] )

    return sign_in_html



#Run the app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')