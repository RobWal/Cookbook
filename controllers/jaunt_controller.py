from flask import Blueprint, render_template
from models.character import get_all_characters

jaunt_controller = Blueprint(
    "jaunt_controller", __name__, template_folder="../templates/jaunt")


@jaunt_controller.route('/learn_the_basics')
def learn_the_basics():
    return render_template('/learn_the_basics.html')


@jaunt_controller.route('/home')
def show_characters():
    character_items = get_all_characters()
    return render_template('home.html', character_items=character_items)
