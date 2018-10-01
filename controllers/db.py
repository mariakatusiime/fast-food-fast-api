import psycopg2
con = psycopg2.connect(database="fastdb",user="maria",password="mama")
print("Opened database successfully")

curs = con.cursor()
curs.execute('''CREATE TABLE ORDERS(
             ORDER_NO INT PRIMARY KEY    NOT NULL,
             DISH VARCHAR(320)     NOT NULL,
             PRICE   FLOAT(6)     NOT NULL,
             STATUS  
             ); ''')
print("Table created successfully")
#con.commit()

#curs.execute('''CREATE TABLE USERS(
#             ID INT PRIMARY KEY    NOT NULL,
#             USERNAME TEXT     NOT NULL,
#             EMAIL   VARCHAR(320)     NOT NULL,
#             PASSWORD VARCHAR(255)  NOT NULL
#             ); ''')
#print("Table created successfully")
#curs.execute("INSERT INTO USERS(ID,USERNAME,EMAIL,PASSWORD)\
#             VALUES(4,'jacob','jcob@hotmail.com','green');")
#con.commit()
curs.execute("INSERT INTO MENU(ID,DISH,PRICE)\
             VALUES(1,'Fried fish ',1200);")
curs.execute("INSERT INTO MENU(ID,DISH,PRICE)\
             VALUES(2,'Fish in G.NUTS',1800);")
curs.execute("INSERT INTO MENU(ID,DISH,PRICE)\
             VALUES(3,'Beef',1500);")

#curs.execute("UPDATE USERS SET USERNAME ='kevin' WHERE ID = 1 ")
con.commit()
#curs.execute("DELETE FROM USERS WHERE USERNAME = 'kevin'")
#con.commit()
curs.execute("SELECT ID,DISH,PRICE FROM MENU")
dishlist = curs.fetchall()
for dish in dishlist:
    print("ID = ",dish[0])
    print("DISH = ",dish[1])
    print("PRICE = ",dish[2],"\n")
print("Operation succesful")
#con.commit()
con.close()