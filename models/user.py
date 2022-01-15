import database
import bcrypt


def get_user_by_email(email):
    results = database.sql_select(
        "SELECT * FROM users WHERE email = %s", [email])
    if len(results) > 0:
        return results[0]
    else:
        return None


def insert_user(username, email, password):
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    database.sql_write("INSERT INTO users (username, email, password)" +
                       " VALUES(%s, %s, %s)", [username, email, password])


def check_existing_username(username):
    results = database.sql_select(
        "SELECT username FROM users WHERE username = %s", [username])
    if len(results) > 0:
        return results[0]
    else:
        return None
