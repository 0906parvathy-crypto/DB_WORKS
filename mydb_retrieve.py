import mysql.connector

con=mysql.connector.connect(user="root",password="parvathy",host="localhost",database="school_db")

print(con)

c=con.cursor()

query="select * from student where roll_no=%s"  # read a specific record from db file

data=(101,)

c.execute(query,data)

record=c.fetchone()

if record:
    print(record)
else:
    print("No record found")

c.close()
con.close()