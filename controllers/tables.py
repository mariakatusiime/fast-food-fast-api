from .db import Dbase
class Mytables:
    def __init__(self):
        self.cmds=('''
            CREATE TABLE IF NOT EXISTS USERS (
            ID INT PRIMARY KEY    NOT NULL,
            USERNAME TEXT,
            EMAIL    VARCHAR(320) NOT NULL,
            PASSWORD VARCHAR(255)    NOT NULL
             );

            
            CREATE TABLE IF NOT EXISTS MENU (
            ID INT PRIMARY KEY    NOT NULL,
            DISH VARCHAR(320)     NOT NULL,
            PRICE   FLOAT(6)      NOT NULL 
             );

            CREATE TABLE IF NOT EXISTS ORDERS (
            ORDER_NO SERIAL PRIMARY KEY   NOT NULL,
            DISH VARCHAR(320)     NOT NULL,
            PRICE   FLOAT(6)      NOT NULL,
            STATUS  VARCHAR(255)  NOT NULL,
            USER_ID  INT REFERENCES USERS(ID) NOT NULL
             );

            CREATE TABLE IF NOT EXISTS ADMIN_USERS(
            ID INT PRIMARY KEY    NOT NULL,
            USERNAME TEXT     NOT NULL,
            EMAIL   VARCHAR(320)      NOT NULL,
            PASSWORD  VARCHAR(255)    NOT NULL
             ) ; '''
        )
    def create_tables(self):
        self.con = Dbase()
        self.cur = self.con.curs
        self.cur.execute(self.cmds)
        print('tables created successfully')
        self.cur.close()



      