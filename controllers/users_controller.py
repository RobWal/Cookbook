from webbrowser import get
from flask import Blueprint, request, redirect, render_template
from models.user import insert_user, get_user_by_email, check_existing_username

users_controller = Blueprint(
    "users_controller", __name__, template_folder="../templates/users")


@users_controller.route('/signup')
def signup():
    error = request.args.get('error', None)
    return render_template('signup.html', error=error)


@users_controller.route('/users', methods=['POST'])
def create_user():
    username = request.form.get('name')
    if check_existing_username(username):
        return redirect("/signup?error=This+username+isn't+available")
    email = request.form.get('email')
    user = get_user_by_email(email)
    if user:
        return redirect("/signup?error=This+email+isn't+available")
    password = request.form.get('password')
    insert_user(username, email, password)
    return redirect('/')
