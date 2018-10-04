from webapp.controllers.db import Dbase
from webapp.controllers.tables import Mytables
class Menu:
    con = Dbase()
    cur = con.curs
    menu = []
    def __init__(self,dish,price):
        
        self.dish = dish
        self.price = price
    def add_menu_items(self):
        query = "INSERT INTO MENU(DISH,PRICE)VALUES(%s,%s)"
        self.cur.execute(query,(self.dish,self.price))
        menu_item = {
            "dish":self.dish,
            "price":self.price
        }
        self.menu.append(menu_item)
        return menu_item

    @classmethod
    def get_menu(cls):
        query ="SELECT DISH,PRICE FROM MENU"
        cls.cur.execute(query)
        menu_list = cls.cur.fetchall()
        for item in menu_list:
            menu_items={
                "dish":item[0],
                "price": item[1]
            }
            cls.menu.append(menu_items)
        return cls.menu
    def delete_menu_item(self,id):
        query = "DELETE FROM MENU WHERE ID=%s"
        self.cur.excecute(query,(id,))
        return("Deleted")


    def edit_menu_item(self,price,id):
        query = "UPDATE MENU SET PRICE = %s WHERE ID = %s"
        self.cur.excecute(query,(self.price,id))
        menu_item = {
            "dish" : self.dish,
            "price": self.price
        }
        self.menu.append(menu_item)

        