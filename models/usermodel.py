from controllers.db import Dbase
from controllers.tables import Mytables
class Users:
    def __init__(self,user_id,username,email,password):
        self.user_id = user_id 
        self.username = username
        self.email = email
        self.password = password
        self.con = Dbase()
        self.cur = self.con.curs

    def user_signup(self):
        query = "INSERT INTO USERS(ID,USERNAME,EMAIL,PASSWORD)VALUES('"+self.user_id+"','"+self.user_id+"'\
        ,'"+self.username+"','"+self.email+"','"+self.password+"')"
        self.cur.execute(query)
        self.cur.close()
    def user_login(self,username,password):
        query = "SELECT EMAIL FROM USERS WHERE USERNAME=%s AND PASSWORD=%s"
        self.cur.execute(query,(username,password))
        return("login successful")
    def admin_login(self,username,password):
        query = "SELECT EMAIL FROM ADMIN_USERS WHERE USERNAME=%s AND PASSWORD=%s"
        self.cur.execute(query,(username,password))
        return("Admin login successful")