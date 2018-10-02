import psycopg2
class Dbase:
    def __init__(self):
        try:
            self.con = psycopg2.connect(database="fastdb",user="maria",password="mama")
            
            self.curs = self.con.cursor()
            self.con.autocommit = True
        except(Exception,psycopg2.DatabaseError) as error:
            print(error)
            