#!/usr/bin/python3
"""
Module that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
This time, protect your code against SQL injection

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name searched (str)
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

    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id"
                .format(searched_name, ))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
