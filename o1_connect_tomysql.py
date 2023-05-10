#import mysql connector
import mysql.connector as sql
myconn=sql.connect(host="localhost",user="root",passwd="root",database="skillmine")

if myconn.is_connected():
    print("connection successfully")
else:
    print("unable to connect to databse")
myconn.close()