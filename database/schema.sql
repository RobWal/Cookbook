DROP TABLE IF EXISTS jaunt_users;
DROP TABLE IF EXISTS jaunt_characters;

CREATE TABLE jaunt_users (
  id SERIAL PRIMARY KEY,
  username varchar(30) not null unique,
  password varchar(255) not null,
  email varchar(255) not null unique
);

CREATE TABLE jaunt_characters (
  id SERIAL PRIMARY KEY,
  user_id integer not null,
  name varchar(30) not null unique,
  stuff smallint not null,
  lessons smallint not null,
  good_luck smallint not null,
  bad_luck smallint not null,
  rift_counter smallint not null,
  body smallint not null,
  body_resistance smallint not null,
  body_coordination smallint not null,
  body_vigour smallint not null,
  intellect smallint not null,
  intellect_resistance smallint not null,
  intellect_ingenuity smallint not null,
  intellect_scrutiny smallint not null,
  presence smallint not null,
  presence_resistance smallint not null,
  presence_allure smallint not null,
  presence_guile smallint not null,
  facet_one varchar(255) not null,
  facet_two varchar(255) not null,
  advantage_one varchar(255) not null,
  advantage_two varchar(255) not null,
  utility_one varchar(255),
  utility_two varchar(255),
  CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES jaunt_users(id)
);