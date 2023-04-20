import sqlite3
sql = sqlite3.connect("roshan.db")

if(sql):
    print("database created successfully")
else:
    print("unable to create database")