from flask import Blueprint, render_template, session, redirect, request
from models.character import get_all_characters, get_character, delete_character_from_database, complete_character_edit_database


jaunt_controller = Blueprint(
    "jaunt_controller", __name__, template_folder="../templates/jaunt")


@jaunt_controller.route('/learn_the_basics')
def learn_the_basics():
    return render_template('/learn_the_basics.html')


@jaunt_controller.route('/home', methods=["GET", "POST"])
def show_characters():
    user_id = session.get('user_id')
    character_items = get_all_characters(user_id)
    return render_template('home.html', character_items=character_items)


@jaunt_controller.route('/<id>/delete_character', methods=["POST"])
def delete_character(id):
    delete_character_from_database(id)
    return redirect('/')


@jaunt_controller.route('/<id>/edit_character', methods=["POST"])
def edit_character(id):
    character_dictionary = get_character(id)
    return render_template('edit_character.html', character_dictionary=character_dictionary)


@jaunt_controller.route('/complete_character_edit/<id>', methods=["POST"])
def complete_character_edit(id):
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
    complete_character_edit_database(id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance,
                                     intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two)
    return redirect('/')


# @food_controller.route('/foods/<id>', methods=["POST"])
# def update(id):
#     if not session.get('user_id'):
#         return redirect('/login')
#     name = request.form.get("name")
#     price = request.form.get("price")
#     description = request.form.get("description")
#     image_url = request.form.get("image_url")
#     update_food(id, name, price, description, image_url)
#     return redirect('/')

# @food_controller.route('/foods/<id>', methods=["POST"])
# def update(id):
#     if not session.get('user_id'):
#         return redirect('/login')
#     name = request.form.get("name")
#     price = request.form.get("price")
#     description = request.form.get("description")
#     image_url = request.form.get("image_url")
#     # UPDATE
#     update_food(id, name, price, description, image_url)
#     return redirect('/')
# @food_controller.route('/foods/<id>/delete', methods=["POST"])
# def delete(id):
#     if not session.get('user_id'):
#         return redirect('/login')
#     delete_food(id)
#     return redirect('/')
