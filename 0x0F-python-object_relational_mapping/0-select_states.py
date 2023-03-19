#!/usr/bin/python3
import sys
import MySQLdb


db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM `states`")
[print(state) for state in c.fetchall()]
