import database
import bcrypt


def get_user_by_email(email):
    results = database.sql_select(
        "SELECT * FROM users WHERE email = %s", [email])
    if len(results) > 0:
        return results[0]
    else:
        return None
