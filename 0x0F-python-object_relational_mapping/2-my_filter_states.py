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
    cur.execute("SELECT * FROM states\
                 WHERE BINARY name = '{}'\
                 ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
