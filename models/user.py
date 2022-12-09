import database
import bcrypt


def get_user_by_email(email):
    results = database.sql_select(
        "SELECT * FROM jaunt_users WHERE email = %s", [email])
    if len(results) > 0:
        return results[0]
    else:
        return None


def insert_user(username, email, password):
    password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    database.sql_write("INSERT INTO jaunt_users (username, email, password)" +
                       " VALUES(%s, %s, %s)", [username, email, password])


def check_existing_username(username):
    results = database.sql_select(
        "SELECT username FROM jaunt_users WHERE username = %s", [username])
    if len(results) > 0:
        return results[0]
    else:
        return None
