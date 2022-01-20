import email
# from ssl import _PasswordType
from unicodedata import name
from flask import Flask, redirect
import os
# import psycopg2

from controllers.jaunt_controller import jaunt_controller
from controllers.session_controller import session_controller
from controllers.users_controller import users_controller


SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def home():
    return redirect('/home')


app.register_blueprint(jaunt_controller)
app.register_blueprint(session_controller)
app.register_blueprint(users_controller)


if __name__ == "__main__":
    app.run(debug=True)


# IDEALLY HAVE MODEL:CONTROLLER, WHERE SESSION = LOGIN/LOGOUT, USERS = ANYTHING TO DO WITH THE USER / PROFILE, CHARACTER = ANYTHING TO DO WITH CHARACTER
