# import mysql connector

import mysql.connector as sql

# connecting to my sql

myconn = sql.connect(host = "localhost", user = "root", passwd = "root", database = "skillmine")

if myconn.is_connected():
    print("connection successfull")
    c = myconn.cursor()
    c.execute("select * from emp")
    allrows = c.fetchall()
    count = c.rowcount
    print("Total number of rows are "+ str(count))
    print("Total number of rows are ", count)
    print("Total number of rows are {}".format(count))

    for eachrow in allrows:
        print(eachrow)

    # print()
    # print("************")
    # print("fetching only 4 rows")
    #
    # exact4rows = c.fetchmany(4)
    # for i in exact4rows:
    #     print(i)

    c.close()

else:
    print("unable to connect to database")
    print("unable to fetch the databases")

myconn.close()