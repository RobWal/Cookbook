from webbrowser import get
from flask import Blueprint, request, session, redirect, render_template
from models.user import get_user_by_email
from models.character import insert_character
import bcrypt

session_controller = Blueprint(
    "session_controller", __name__, template_folder="../templates/session")


@session_controller.route('/login')
def loginpage():
    error = request.args.get('error', None)
    return render_template('login.html', error=error)


@session_controller.route('/sessions/create', methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user_by_email(email)
    valid = user and bcrypt.checkpw(
        password.encode(), user['password'].encode())
    if valid:
        session['user_id'] = user['id']
        session['user_name'] = user['username']
        return redirect('/')
    else:
        return redirect('/login?error=Incorrect+username+or+password')


@session_controller.route('/sessions/destroy', methods=["GET", "POST"])
def logout():
    session.clear()
    return redirect('/')


@session_controller.route('/create_page', methods=["GET", "POST"])
def create_page():
    return render_template('create_page.html')


@session_controller.route('/create_character', methods=["POST"])
def create_character():
    user_id = session['user_id']
    name = request.form.get('name')
    stuff = request.form.get('stuff')
    lessons = request.form.get('lessons')
    good_luck = request.form.get('good_luck')
    bad_luck = request.form.get('bad_luck')
    rift_counter = request.form.get('rift_counter')
    body = request.form.get('body')
    body_resistance = request.form.get('body_resistance')
    body_coordination = request.form.get('body_coordination')
    body_vigour = request.form.get('body_vigour')
    intellect = request.form.get('intellect')
    intellect_resistance = request.form.get('intellect_resistance')
    intellect_ingenuity = request.form.get('intellect_ingenuity')
    intellect_scrutiny = request.form.get('intellect_scrutiny')
    presence = request.form.get('presence')
    presence_resistance = request.form.get('presence_resistance')
    presence_allure = request.form.get('presence_allure')
    presence_guile = request.form.get('presence_guile')
    facet_one = request.form.get('facet_one')
    facet_two = request.form.get('facet_two')
    advantage_one = request.form.get('advantage_one')
    advantage_two = request.form.get('advantage_two')
    utility_one = request.form.get('utility_one')
    utility_two = request.form.get('utility_two')
    insert_character(user_id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance,
                     intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two)
    error = request.args.get('error', "Character created successfully!")
    return render_template('create_page.html', error=error)


@session_controller.route('/profile_settings', methods=["GET", "POST"])
def profile_settings():
    return render_template('profile_settings.html')
