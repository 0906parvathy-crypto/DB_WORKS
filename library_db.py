import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",
                                         host="localhost",
                                         password="parvathy",
                                         database="library_db")

        self.c=self.con.cursor()

        # this part can be done in workbench

        # self.title=input("enter title")
        # self.author=input("enter author")
        # self.price=int(input("enter price"))
        # self.language=input("enter language")
        # self.page=int(input("enter pages"))
        #
        # query="insert into book(title,author,price,language,page)values(%s,%s,%s,%s,%s)"
        # data=(self.title,self.author,self.price,self.language,self.page)
        # self.c.execute(query,data)
        # self.con.commit()


    def list(self):
        query="select * from book"     #Reading all records from db table
        self.c.execute(query)
        record=self.c.fetchall()
        if record:
            for row in record:
                print(row)
            else:
                print("no record found")
#
    def create(self,title,author,price,language,page):             #creating a new record
        query="insert into book(title,author,price,language,page)values(%s,%s,%s,%s,%s)"
        data=(title,author,price,language,page)
        self.c.execute(query,data)
        self.con.commit()
        print("Inserted Data Successfully")

#
    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            print(record)
        else:
            print("no record found")

    def update(self,title,author,price,language,page,id):
        query="update book set title=%s,author=%s,price=%s,language=%s,page=%s where id=%s"
        data=(title,author,price,language,page,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print("update data successfully")
        else:
            print("no record found")
#
    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            print("data deleted")
        else:
            print("no record found")

book_instance=BookListCreateRetrieveUpdateDelete()
book_instance.list()
# book_instance.create("Wings of Fire","APJ",800,"English",1000)
book_instance.retrieve(2)
# book_instance.delete(4)
book_instance.update("ABC","John",500,"Hindi",600,1)