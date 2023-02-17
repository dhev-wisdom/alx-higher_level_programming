-- script list all cities (table) in database
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDEE BY cities.id
