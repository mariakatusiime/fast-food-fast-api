from controllers.db import Dbase
from controllers.tables import Mytables
class CustomerOrders:
    def __init__(self, dish, price, status,user_id):
        
        self.dish = dish
        self.price = price
        self.status = status
        self.user_id = user_id
        self.con = Dbase()
        self.cur = self.con.curs
        self.orders = []


    # function that allows users to make orders
    def create_orders(self):
        query = "INSERT INTO ORDERS(DISH,PRICE,STATUS,USER_ID) VALUES (%s,%s,%s,%s)"
        
        print("#####",self.dish)
        self.cur.execute(query,(self.dish,self.price,self.status,self.user_id,))
        order = {
            
            'dish'  :self.dish,
            'price'  :self.price,
            'status' :self.status,
            'user_id':self.user_id
        }
        self.orders.append(order)
        return order
        #self.cur.close()

    # function that displays all orders to admin    
    def get_orders(self):
        query = "SELECT ORDER_NO,DISH,PRICE,STATUS,USER_ID FROM ORDERS"
        
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
            self.orders.append(order)
        return self.orders


    def get_order(self,order_no):
        query = "SELECT DISH,PRICE,STATUS,USER_ID FROM ORDERS WHERE ORDER_NO =%s"
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
        query = "UPDATE ORDERS SET STATUS = %s WHERE ORDER_NO = %s "
        self.cur.execute(query,(status,order_no))
        self.cur.close()
    

    #function for deleting a specific order
    def delete_order(self,order_no):
        query = "DELETE FROM ORDERS WHERE ORDER_NO = %s"
        self.cur.execute(query,(order_no,))
        self.cur.close




