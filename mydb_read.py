import mysql.connector

con=mysql.connector.connect(user="root",password="parvathy",host="localhost",database="school_db")

print(con)

c=con.cursor()

# read all records from db table
query="select * from student"

c.execute(query)

records=c.fetchall()
if records:
    for row in records:
        print(row)
else:
    print("no records found")

c.close()
con.close()
