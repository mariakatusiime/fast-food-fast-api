from controllers.db import Dbase
from controllers.tables import Mytables
class Users:
    con = Dbase()
    cur = con.curs
    users =[]

    def __init__(self,username,email,password):
    
        self.username = username
        self.email = email
        self.password = password
        
    def user_signup(self):
        query = "INSERT INTO USERS(USERNAME,EMAIL,PASSWORD)VALUES('%s,%s,%s,%s)"
        self.cur.execute(query,(self.username,self.email,self.password))
        user ={
            'username':self.username,
            'email'  : self.email,
            'password':self.password

        }
        return user

        #self.cur.close()

    @classmethod
    def user_login(cls,username,password):
        query = "SELECT EMAIL FROM USERS WHERE USERNAME=%s AND PASSWORD=%s"
        cls.cur.execute(query,(username,password))
        user = {
            'Welcome':username
        }
        cls.users.append(user)
        return user


    def admin_login(self,username,password):
        query = "SELECT EMAIL FROM ADMIN_USERS WHERE USERNAME=%s AND PASSWORD=%s"
        self.cur.execute(query,(username,password))
        return("Admin login successful")