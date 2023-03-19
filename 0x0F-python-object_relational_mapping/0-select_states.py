#!/usr/bin/python3
"""
Module lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
	mysql_user = sys.argv[1]
	mysql_passwd = sys.argv[2]
	mysql_db = sys.argv[3]

	# By default, it will connect to localhost 3306
	db = MySQLdb.connect(user=mysql_user, passwd=mysql_passwd, db=mysql_db)
	cur = db.cursor()

	cur.execute("SELECT * FROM states ORDER BY id")
	rows = cur.fetchall()

	for row in rows:
		print(row)
