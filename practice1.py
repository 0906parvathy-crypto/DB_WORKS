import mysql.connector
class customer():
    def __init__(self):
        self.con=mysql.connector.connect(user="root",
                                         password="parvathy",
                                         host="localhost",
                                         database="market")
        self.c=self.con.cursor()

    def create(self,customer_id,name,age,place):
        query="insert into customer(name,age,place) values(%s,%s,%s)"
        data=(name,age,place)
        self.c.execute(query,data)
        self.con.commit()
        print("Data Inserted")

market=customer()
market.create(1,"Tanvi",24,"Kannur")
