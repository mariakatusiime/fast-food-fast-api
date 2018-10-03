from controllers.db import Dbase
from controllers.tables import Mytables
class Menu:
    con = Dbase()
    cur = con.curs
    menu = []
    def __init__(self,dish,price):
        self.dish = dish
        self.price = price
    def add_menu_items(self):
        pass
    def 