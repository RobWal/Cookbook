from flask import Blueprint, render_template, session, redirect
from models.character import get_all_characters, delete_character_from_database


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
def edit_character():
    # PUT IN ALL THE VARIABLES HERE TO BE PARSED IN THE EDIT_CHARACTER PARAMETERS
    # edit_character(id)
    return redirect('/')


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
