import database


def insert_character(user_id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance, intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two):
    database.sql_write("INSERT INTO characters(user_id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance, intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two)" +
                       " VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [user_id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance, intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two])


def get_all_characters(user_id):
    results = database.sql_select(
        "SELECT * FROM characters WHERE user_id = %s", [user_id])
    return results


def get_character(id):
    results = database.sql_select(
        "SELECT * FROM characters WHERE id = %s", [id])
    return results


def complete_character_edit_database(id, name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance, intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two):
    database.sql_write("UPDATE characters set name = %s, stuff = %s, lessons = %s, good_luck = %s, bad_luck = %s, rift_counter = %s, body = %s, body_resistance = %s, body_coordination = %s, body_vigour = %s, intellect = %s, intellect_resistance = %s, intellect_ingenuity = %s, intellect_scrutiny = %s, presence = %s, presence_resistance = %s, presence_allure = %s, presence_guile = %s, facet_one = %s, facet_two = %s, advantage_one = %s, advantage_two = %s, utility_one = %s, utility_two = %s WHERE id = %s", [
        name, stuff, lessons, good_luck, bad_luck, rift_counter, body, body_resistance, body_coordination, body_vigour, intellect, intellect_resistance, intellect_ingenuity, intellect_scrutiny, presence, presence_resistance, presence_allure, presence_guile, facet_one, facet_two, advantage_one, advantage_two, utility_one, utility_two, id
    ])


def delete_character_from_database(id):
    database.sql_write("DELETE FROM characters WHERE id = %s", [id])
