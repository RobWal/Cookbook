import email
from ssl import _PasswordType
from unicodedata import name
from flask import Flask, redirect
import os
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=flask_app")
SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
@app.route('/menu')
def index():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT 1', [])  # Query to check that the DB connected
    conn.close()
    return 'Hello, world! This is a change I made to test the heroku/git push.'


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
