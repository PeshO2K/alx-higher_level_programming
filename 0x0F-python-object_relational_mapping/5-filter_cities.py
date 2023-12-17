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
    #cur.execute("SELECT * FROM states")
    #cur.execute("SELECT * FROM cities")
    # cur.execute("TRUNCATE TABLE states")
    #cur.execute("SHOW tables")
    # cur.execute("DROP TABLE states")
    """cur.execute("SELECT * FROM states  WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4]))"""
    cur.execute("SELECT name FROM cities\
                 WHERE state_id = (SELECT id FROM states WHERE name = %s )\
                 ORDER BY cities.id",(sys.argv[4],))

    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
