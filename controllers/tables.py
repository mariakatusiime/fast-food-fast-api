from controllers.db import Dbase
class Mytables:
    def __init__(self):
        self.cmds=('''CREATE TABLE ORDERS IF NOT EXIST(
            ORDER_NO INT PRIMARY KEY    NOT NULL,
            DISH VARCHAR(320)     NOT NULL,
            PRICE   FLOAT(6)      NOT NULL,
            STATUS  TEXT 
            USER_ID  INT REFERENCES USERS(ID) NOT NULL
             ), 
            CREATE TABLE MENU IF NOT EXIST(
            ID INT PRIMARY KEY    NOT NULL,
            DISH VARCHAR(320)     NOT NULL,
            PRICE   FLOAT(6)      NOT NULL 
             ),
            CREATE TABLE USERS IF NOT EXIST(
            ID INT PRIMARY KEY    NOT NULL,
            USERNAME TEXT,
            EMAIL    VARCHAR(320) NOT NULL,
            PASSWORD VARCHAR(255)    NOT NULL
             ),
            CREATE TABLE ADMIN_USERS IF NOT EXIST(
            ID INT PRIMARY KEY    NOT NULL,
            USERNAME TEXT     NOT NULL,
            EMAIL   VARCHAR(320)      NOT NULL,
            PASSWORD  VARCHAR(255)    NOT NULL
             ), ; '''
        )
    def create_tables(self):
        self.con = Dbase()
        self.cur = self.con.curs
        self.cur.execute(self.cmds)
        print('tables created successfully')


if __name__ == '__main__':
    Mytables().create_tables()    