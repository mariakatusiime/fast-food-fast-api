import psycopg2
class Dbase:
    def __init__(self):
        try:
            self.con = psycopg2.connect(database="fastdb",user="maria",password="mama")
            #print("Opened database successfully")
            self.curs = self.con.cursor()
            self.con.autocommit = True
        except(Exception,psycopg2.DatabaseError) as error:
            print(error)
            #curs.execute()
#print("Table created successfully")
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
#curs.execute("INSERT INTO ORDERS(ORDER_NO,DISH,PRICE,STATUS)\
#             VALUES(1,'Fried fish ',1200,'ACCEPTED');")

#curs.execute("UPDATE USERS SET USERNAME ='kevin' WHERE ID = 1 ")
#con.commit()
#curs.execute("DELETE FROM USERS WHERE USERNAME = 'kevin'")
#con.commit()
#curs.execute("SELECT ORDER_NO,DISH,PRICE,STATUS FROM ORDERS")
#dishlist = curs.fetchall()
#for dish in dishlist:
#    print("ORDER_NO = ",dish[0])
#    print("DISH = ",dish[1])
#    print("PRICE = ",dish[2])
#    print("STATUA = ",dish[3],"\n")
#print("Operation succesful")
#con.commit()
        #    con.close()