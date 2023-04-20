# import mysql connector

import mysql.connector as sql

# connecting to my sql

myconn = sql.connect(host = "localhost", user = "root", passwd = "root")

if myconn.is_connected():
    print("connection successfull")

else:
    print("unable to connect to database")

myconn.close()