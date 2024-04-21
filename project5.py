'''import mysql.connector
mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password = ""
)
mycursor=mydb.cursor()
mycursor.execute("Create database Emp_Mam")
print("Database created sucessfully")'''

'''import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Emp_Mam"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE emp_table(id int(2) primary key auto_increment, name varchar(120), address varchar(120), phone varchar(10), mail varchar(100), department varchar(100))")

print("Table created successfully")'''


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Emp_Mam"
)

mycursor = mydb.cursor()
sql ="insert into emp_table(id,name,address,phone,mail,department) values(%s,%s,%s,%s,%s,%s)"
val =[
    ("","Mr.Das","Kolkata","579281541","das65gmail.com","Sales"),
    ("","Mr.Adhakari","Darjeeling","6724843266","Adhakari76@.gmail.com","Accounts"),
    ("","Mr.Sem","Kurseong","4664664462","Sem121@gmial.com","Purchase")
]

mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"row/s insented")
sql ="select * from emp_table"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for u in myresult:
    print(u)

mycursor=mydb.cursor()
sql="insert into emp_table(id, name, address, phone, mail, department)values(%s,%s,%s,%s,%s,%s)"
val=[
    ('',"Mr.Das","Kolkata","621922810","das220@gmail.com","Sales"),
    ('',"Mrs.Adhikari","Darjeeling","7299017771","ashi22@gmail.com","Account"),
    ('',"Mr.Sen","Kurseong","9336622190","sen_221@gmail.com","Purchase")
]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"row/s ineserted")

sql="select *from emp_table"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for u in myresult:
    print(u)

sql="update emp_table set name=%s where name=%s"
val=("Mrs.Das","Mr.Das")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"row/s affected")

