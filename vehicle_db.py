#Define a class to perform database operation on Vehicle table
# create a class named VehicleListCreateRetrieveUpdateDelete with methods
# list()
# create()
# retrieve()
# update()
# delete()

import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",
                                         host="localhost",
                                         password="parvathy",
                                         database="vehicle_db")
        self.c=self.con.cursor()


    def list(self):
        query="select * from vehicle"
        self.c.execute(query)
        record=self.c.fetchall()
        if record:
            for row in record:
                print(row)
        else:
            print("no record found")

    def create(self,brand,model,type,price,year):
        query="insert into vehicle(brand,model,type,price,year)values(%s,%s,%s,%s,%s)"
        data=(brand,model,type,price,year)
        self.c.execute(query,data)
        self.con.commit()
        print("Insert Data Successfully")

    def retrieve(self,id):
        query="select * from vehicle where id=%s"
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            print(record)
        else:
            print("no record found")

    def delete(self,id):
        query="delete from vehicle where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print("Data Deleted")
        else:
            print("No record Found")

    def update(self,brand,model,type,price,year,id):
        query="update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s"
        data=(brand,model,type,price,year,id)
        self.c.execute(query, data)
        self.con.commit()
        if self.c.rowcount>0:
            print("update data successfully")
        else:
            print("no record found")
vehicle_db=VehicleListCreateRetrieveUpdateDelete()
vehicle_db.list()
# vehicle_db.create("Tata","Punch","SUV","5-6 Lakh","2026")
vehicle_db.retrieve(2)
# vehicle_db.delete(1)
vehicle_db.update("Maruti Susuki","Brezza","SUV","7-8 Lakh","2026",1)
