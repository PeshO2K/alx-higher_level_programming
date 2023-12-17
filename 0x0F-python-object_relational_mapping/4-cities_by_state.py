#!/usr/bin/python3
"""Custom filter state module"""
import MySQLdb
import sys
if __name__ == "__main__":
    """for arg in sys.argv:
        print (arg)"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities\
                 LEFT JOIN states ON cities.state_id = states.id\
                 WHERE states.id = state_id\
                 ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
