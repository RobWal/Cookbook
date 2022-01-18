from webbrowser import get
from flask import Blueprint, request, session, redirect, render_template
from models.user import insert_user, get_user_by_email, check_existing_username

users_controller = Blueprint(
    "users_controller", __name__, template_folder="../templates/users")


@users_controller.route('/signup')
def signup():
    error = request.args.get('error', None)
    return render_template('signup.html', error=error)


@users_controller.route('/users', methods=['POST'])
def create_user():
    username = request.form.get('username')
    if check_existing_username(username):
        return redirect("/signup?error=This+username+isn't+available")
    email = request.form.get('email')
    user = get_user_by_email(email)
    if user:
        return redirect("/signup?error=This+email+isn't+available")
    passwordOne = request.form.get('passwordOne')
    passwordTwo = request.form.get('passwordTwo')
    if passwordOne != passwordTwo:
        return redirect("/signup?error=The+passwords+do+not+match")
    insert_user(username, email, passwordOne)
    user = get_user_by_email(email)
    session['user_id'] = user['id']
    session['user_name'] = user['username']
    return redirect('/')
