import sqlite3
sql = sqlite3.connect("roshan.db")

if(sql):
    print("database created successfully")
    c= sql.cursor()
    c.execute("create table if not exists student(name varchar(100), address varchar(100) )")
    print("table created successfully")
    c.execute("insert into student(name , address) values ('rajesh' , 'hyderabad')")
    c.execute("select * from student")
    allrows = c.fetchall()
    for eachrow in allrows:
        print(eachrow)
    sql.commit()
    c.close()

else:
    print("unable to create database")
sql.close()