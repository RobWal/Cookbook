import email
# from ssl import _PasswordType
from unicodedata import name
from flask import Flask, redirect
import os
import psycopg2

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


# User can create an account 'user'
# Create character --> PC or NPC --> takes them through the creation process
# Characters can be public or private (seen by others or not), alterable, default visibile
# A basics page re Jaunt

# 2 tables - users and characters, challenges maybe
# signup/login
# modifiable PC/NPC


# ~~MAKE ALL THESE NOT NULL~~ ~~ADD VALIDATION FOR ALL THESE FIELDS EG. PC/NPC, <7 & >0 FOR COUNTER/LUCK
# UserID: unique key linked to user - foreign key used to join
# Class: PC/NPC - enum
# Name: Example Name - Varchar 30
# Player: - join users table, select username column
# Rift counter: x/6 - smallint
# Good luck: x/6 - smallint
# Bad luck: x/6 - smallint
# Resources(stuff): - smallint
# Resources(lessons): - smallint
# FacetOne: aspect of the PC - text
# Facettwo: aspect of the PC - text
# Body: - smallint
# Body(resistance): - smallint
# Body(coord): - smallint
# Body(vigour): - smallint
# Intellect: - smallint
# Intellect(resistance): - smallint
# Intellect(ingenuity): - smallint
# Intellect(scrutiny): - smallint
# Presence: - smallint
# Presence(resistance): - smallint
# Presence(allure): - smallint
# Presence(guile): - smallint
# Advantage: One time bonus - text
# Advantage2: One time bonus - text
# Utility: Small perk - text
# Utility2: Small perk - text

# ID - serial - primary key
# username - varchar 30
# email - text - unique constraint
# password - varchar 255
