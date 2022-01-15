from flask import Blueprint, render_template

jaunt_controller = Blueprint(
    "jaunt_controller", __name__, template_folder="../templates/jaunt")


@jaunt_controller.route('/home')
def home():
    return render_template('home.html')
