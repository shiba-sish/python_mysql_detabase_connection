import sqlite3

sql=sqlite3.connect("shiba.db")

if(sql):
    print("database created successfully")
    c=sql.cursor()
    c.execute("create table if not exists student(id integer primary key autoincrement, name text, address text)")
    print("table get created successfully")
    c.execute("insert into student(name ,address)values('ram','pune')")
    c.execute("select * from student")
    allrow= c.fetchall()
    for i in allrow:
        print(i)
    sql.commit()

else:
    print("unable to connect ")

c.close()
sql.close()