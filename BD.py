import mysql.connector
class BloodDonation():
    def __init__(self):
        self.con=mysql.connector.connect(user="root",
                            password="parvathy",
                            host="localhost",
                            database="blood_db")
        self.c=self.con.cursor()
    def create(self,name,bloodgroup,phone,city,last_donation):
        query="insert into donor(name,bloodgroup,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
        data=(name,bloodgroup,phone,city,last_donation)
        self.c.execute(query,data)
        self.con.commit()
        print("Data inserted successfully")

    def read(self):
        query="select * from donor"
        self.c.execute(query)
        record=self.c.fetchall()
        if record:
            for row in record:
                print(row)
        else:
                print("no record found")

    def retrieve(self,id):
        query="select * from donor where id=%s"
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            print(record)
        else:
            print("no record found")

    def update(self,name,bloodgroup,phone,city,last_donation,id):
        query="update donor set name=%s,bloodgroup=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data=(name,bloodgroup,phone,city,last_donation,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print("Data Updated Successfully")
        else:
            print("No record found")

    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print("Data Deleted")
        else:
            print("No record Found")

b=BloodDonation()
# b.create("Tanu","O+ve",9778094267,"ekm","2025-06-09")
#b.create("Ravi","A+ve","9446708520","pta","2025-05-12")
b.read()
b.retrieve(1)
b.update("Sanvi","B+ve","9496469748","Tvm","2024-09-08",2)
b.delete(1)
