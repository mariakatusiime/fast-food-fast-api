from webapp.controllers.db import Dbase
from webapp.controllers.tables import Mytables
class Users:
    con = Dbase()
    cur = con.curs
    users =[]

    def __init__(self,username,email,password):

        
        self.username = username
        self.email = email
        self.password = password
    #user and admin signup    
    def user_signup(self):
        query ="SELECT * FROM USERS WHERE USERNAME = %s AND PASSWORD =%s"
        self.cur.execute(query,(self.username,self.email))
        if query:
            return("user with username :{} or email: {} already exists"\
                  .format(self.username,self.email)),409 

        else:
           query = "INSERT INTO USERS(USERNAME,EMAIL,PASSWORD,ROLE)VALUES(%s,%s,%s,%s) RETURNING id"
           self.cur.execute(query,(self.username,self.email,self.password, False))
           query = "UPDATE USERS SET ROLE=%s WHERE ID=%s"
           self.cur.execute(query,( True,1))
           user ={
            'username':self.username,
            'email'  : self.email,
            'password':self.password
            }
        return user

        #self.cur.close()
    def user_login(self,username,password):
        query = "SELECT EMAIL FROM USERS WHERE USERNAME=%s AND PASSWORD=%s"
        self.cur.execute(query,(username,password))
        user = {
            'Welcome':username
        }
        self.users.append(user)
        return user


    def admin_login(self,username,password):
        query = "SELECT EMAIL FROM ADMIN_USERS WHERE USERNAME=%s AND PASSWORD=%s"
        self.cur.execute(query,(username,password))
        return("Admin login successful")