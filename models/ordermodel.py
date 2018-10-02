from controllers.db import Dbase
from models.tables import Mytables
class CustomerOrders:
    def __init__(self,order_no, dish, price, status,user_id):
        self.order_no = order_no
        self.dish = dish
        self.price = price
        self.status = status
        self.user_id = user_id
        self.con = Dbase()
        self.cur = self.con.curs


    # function that allows users to make orders
    def create_orders(self):
        query = "INSERT INTO ORDERS(ORDER_NO, DISH,PRICE,STATUS,USER_ID) VALUES ('" +self.order_no + "' , '" + \
              self.dish + "',  '" + self.price + "', '"+ self.status +"', '"+ self.user_id +"')"
        
        self.cur.execute(query)
        self.cur.close()

    # function that displays all orders to admin    
    def get_orders(self):
        query = "SELECT ORDER_NO,DISH,PRICE,STATUS,USER_ID FROM ORDERS"
        orders = []
        self.cur.execute(query)
        orderlist = self.cur.fetchall()
        for orde in orderlist:
            order = {
                'ORDER_NO': orde[0],
                'DISH'    : orde[1],
                'PRICE'   : orde[2],
                'STATUS'  : orde[3],
                'USER_ID': orde[4]
            }
            orders.append(order)
        return orders


    def get_order(self,order_no):
        query = "SELECT DISH,PRICE,STATUS,USER_ID FROM ORDERS WHERE ORDER_NO =%d"
        self.cur.execute(query, (order_no,))
        row = self.cur.fetchone()
        order = {
            'ORDER_NO': row[0],
            'DISH': row[1],
            'PRICE': row[2],
            'STATUS': row[3],
            'USER_ID': row[4],
        }
        self.cur.close()
        return order

    #function for updating a particular order status
    def update_order_status(self,order_no,status):
        query = "UPDATE ORDERS SET STATUS = %d WHERE ORDER_NO = %d "
        self.cur.execute(query,(status,order_no))
        self.cur.close()
    

    #function for deleting a specific order
    def delete_order(self,order_no):
        query = "DELETE FROM ORDERS WHERE ORDER_NO = %d"
        self.cur.execute(query,(order_no,))
        self.cur.close




