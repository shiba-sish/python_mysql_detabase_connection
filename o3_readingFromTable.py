
import mysql.connector as sql
myconn=sql.connect(host="localhost",user="root",passwd="root",database="skillmine")

if myconn.is_connected():
    print("connection successfully")
    c= myconn.cursor()
    c.execute("select * from emp")

    #fetchall() ,fetchone() , fetchmany(<n>)
    allrow=c.fetchall()
    count= c.rowcount
    print("the total noof rows are: "+str(count))
    print("the total noof rows are: ",count)
    print("the total noof rows are: {} ".format(count))

    # eaxct4rows=c.fetchmany(4)
    # for i in eaxct4rows:
    #     print(i)

    for i in allrow:
        print(i)
    c.close()
else:
    print("unable to connect to databse")
    print("unable to fetch data from datbases")
myconn.close()