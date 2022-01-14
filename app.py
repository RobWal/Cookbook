from flask import Flask
import os
import psycopg2

DB_URL = os.environ.get("DATABASE_URL", "dbname=flask_app")
SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT 1', [])  # Query to check that the DB connected
    conn.close()
    return 'Hello, world!'


if __name__ == "__main__":
    app.run(debug=True)

# Create account function
# User can create an account 'user'
# Create character --> PC or NPC --> takes them through the creation process
# Characters can be public or private (seen by others or not), alterable
# A basics page re Jaunt

# 2 tables - users and characters
# signup/login 
# modifiable PC/NPC