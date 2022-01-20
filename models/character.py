import database


def insert_character(user_id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance, intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two):
    database.sql_write("INSERT INTO characters(user_id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance, intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two)" +
                       " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [user_id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance, intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two])


def get_all_characters(user_id):
    results = database.sql_select(
        "SELECT * FROM characters WHERE user_id = %s", [user_id])
    return results


def edit_character(id, name, price, description, image_url):
    database.sql_write("UPDATE foods set name = %s, price = %s, description = %s, image_url = %s WHERE id = %s", [
        name,
        float(price) * 100,
        description,
        image_url,
        id
    ])

# DELETE FOOD FROM DB


def delete_character_from_database(id):
    database.sql_write("DELETE FROM characters WHERE id = %s", [id])
