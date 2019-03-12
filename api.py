from flask import Flask, session, request
from Auth import Auth

auth = Auth("localhost", "username", "password", "database")

app = Flask(__name__)

#Define app routes
@app.route("/sign_up")
def sign_up():
    return auth.sign_up("First", "Last", "test@test.test", "test", "test")

    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')