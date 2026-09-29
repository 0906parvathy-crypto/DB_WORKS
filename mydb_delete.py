# import mysql.connector
#
# con=mysql.connector.connect(user="root",password="parvathy",host="localhost",database="school_db")
#
# print(con)
#
# c=con.cursor()
#
# query="delete from student where roll_no=%s"
#
# data=(101,)
#
# c.execute(query,data)
# con.commit()
#
# if c.rowcount>0:
#     print("data is deleted")
# else:
#     print("no record found")
#
# c.close()
# con.close()


import mysql.connector

con = mysql.connector.connect(user="root", password="parvathy", host="localhost", database="school_db")

print(con)

c = con.cursor()

query = "delete from student where roll_no=%s"

data = (102,)

c.execute(query, data)
con.commit()

if c.rowcount>0:
    print("data is deleted")
else:
    print("no record found")

c.close()
con.close()