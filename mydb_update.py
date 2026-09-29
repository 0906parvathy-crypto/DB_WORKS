import mysql.connector

con = mysql.connector.connect(user="root", password="parvathy", host="localhost", database="school_db")

print(con)

c = con.cursor()

query="update student set place=%s where roll_no=%s"

data=('tvm',101)
c.execute(query,data)
con.commit()
if c.rowcount>0:
    print("data updated successfully")
else:
    print("no records found")
c.close()
con.close()