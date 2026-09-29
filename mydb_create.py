import mysql.connector
#
#
# # Establish connection between mysql server and python code
# con=mysql.connector.connect(user="root",password="parvathy",host="localhost")
# # it returns connection object
# print(con)
#
# # cursor object--for executing sql queries
# c=con.cursor()
#
# query="create database school_db"
# c.execute(query)
# print("Database file created")
# c.close()
# con.close()






# creating table
con=mysql.connector.connect(user="root",password="parvathy",host="localhost",database="school_db")
# c=con.cursor()
# query="""create table student(
#        roll_no int not null primary key,
#        name varchar(20),
#        age int,
#        place varchar(20),
#        phone varchar(20),
#        total_marks int)""";
# c.execute(query)
# print("table created")

# create new table/insert data
c=con.cursor()

query="insert into student(roll_no,name,age,place,phone,total_marks) values(%s,%s,%s,%s,%s,%s)"
data= (101,"Arun",22,"ekm","9087654321",145)

c.execute(query,data)
con.commit()
print("insert data successfully")

c.close()
con.close()