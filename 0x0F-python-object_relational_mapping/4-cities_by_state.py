#!/usr/bin/python3
"""
Module that that lists all cities from the database hbtn_0e_4_usa

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""


import sys
import MySQLdb


if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_pw = sys.argv[2]
    mysql_db = sys.argv[3]
    searched_name = sys.argv[4]

    # By default, it will connect to localhost:3306
    db = MySQLdb.connect("user=mysql_user, passwd=mysql_pw, db=mysql_db")
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
