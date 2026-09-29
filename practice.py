import mysql.connector



con=mysql.connector.connect(user="root",
                            password="parvathy",
                            host="localhost",
                            database="market")
c=con.cursor()
print("connection successful")
#  READ
# query="select * from customer"
# c.execute(query)
# record=c.fetchall()
# if record:
#     for row in record:
#         print(row)
# else:
#     print("no record found")


# UPDATE
# query="update customer set place=%s where customer_id=%s"
# data=("pta",3)
# c.execute(query,data)
# con.commit()
# if c.rowcount>0:
#     print("record updated")
# else:
#     print("no record found")

# DELETE
# query="delete from customer where customer_id=%s"
# data=(2,)
# c.execute(query,data)
# con.commit()
# if c.rowcount>0:
#     print("record deleted")
# else:
#     print("no record found")

# RETRIEVE

query="select * from customer"
c.execute(query)
records=c.fetchone()
if records:
    print(records)
else:
    print("no record found")