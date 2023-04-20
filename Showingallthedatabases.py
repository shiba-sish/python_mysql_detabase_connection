# import mysql connector

import mysql.connector as sql

# connecting to my sql

myconn = sql.connect(host = "localhost", user = "root", passwd = "root")

if myconn.is_connected():
    print("connection successfull")
    c = myconn.cursor()
    c.execute("show databases")
    alldatabases = c.fetchall()

    for eachdatabse in alldatabases:
        print(eachdatabse)
    c.close()

else:
    print("unable to connect to database")
    print("unable to fetch the databases")

myconn.close()