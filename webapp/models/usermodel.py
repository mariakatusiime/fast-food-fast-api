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
        query ="SELECT USERNAME,EMAIL FROM users WHERE USERNAME = %s AND EMAIL =%s"
        self.cur.execute(query,(self.username,self.email))
        row = self.cur.fetchone()
        if row == None:
            query = "INSERT INTO USERS(USERNAME,EMAIL,PASSWORD,ROLE)VALUES(%s,%s,%s,%s) RETURNING id"
            self.cur.execute(query,(self.username,self.email,self.password, False))
            query = "UPDATE USERS SET ROLE=%s WHERE ID=%s"
            self.cur.execute(query,( True,1))
            user ={
                'username':self.username,
                'email'  : self.email,
                'password':self.password
                  }
            return ("success")

        user = {
            'username':row[0],
            'email':row[1]
              }
        
        if self.username == user['username'] or self.email == user['email'] :
            return("userexists") 

       

        #self.cur.close()
        
    def user_login(self):
        query = "SELECT USERNAME,PASSWORD FROM USERS WHERE USERNAME = %s AND PASSWORD = %s"
        self.cur.execute(query,(self.username,self.password))
        rows = self.cur.fetchone() 
        if rows == None:
            return ("none")
        
        user = {
            'username' : rows[0],
            'password' : rows[1]
            }
        if self.username == user['username']:
          

           return user['username']    

            

    