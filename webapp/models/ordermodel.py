from webapp.controllers.db import Dbase

class CustomerOrders:
    con = Dbase()
    cur = con.curs
    orders = []

    def __init__(self, dish, price,quantity, status,user_id):
        
        self.dish = dish
        self.price = price
        self.quantity = quantity

        self.status = status
        self.user_id = user_id
        

    # function that allows users to make orders
    
    def create_orders(self):
        
        query = "INSERT INTO ORDERS(DISH,PRICE,STATUS,USER_ID,QUANTITY) VALUES (%s,%s,%s,%s,%s)"    
        self.cur.execute(query,(self.dish,self.price,self.status,self.user_id,self.quantity))
        query ="UPDATE ORDERS SET QUANTITY = %s WHERE USER_ID=%s"
        self.cur.execute(query,(self.quantity+1,self.user_id))

        order = {
            
                 'dish'  : self.dish,
                 'price'  :self.price,
                 'quantity': self.quantity,
                 'status' :self.status,
                 'user_id':self.user_id,
                 
                }
        self.orders.append(order)
        return order
        #self.cur.close()


    # function that displays all orders to admin    
    @classmethod
    def get_orders(cls):
        query = "SELECT ORDER_NO,DISH,PRICE,QUANTITY,STATUS,USER_ID FROM ORDERS"
        
        cls.cur.execute(query)
        orderlist = cls.cur.fetchall()
        for orde in orderlist:
            order = {
                'ORDER_NO': orde[0],
                'DISH'    : orde[1],
                'PRICE'   : orde[2],
                'QUANTITY': orde[3],
                'STATUS'  : orde[4],
                'USER_ID': orde[5]
            }
            cls.orders.append(order)
        return cls.orders

    @classmethod
    def get_order(cls,order_no):
        query = "SELECT DISH,PRICE,STATUS,USER_ID FROM ORDERS WHERE ORDER_NO =%s"
        cls.cur.execute(query, (order_no,))
        row = cls.cur.fetchone()
        
        order = {
            'DISH': row[0],
            'PRICE': row[1],
            'STATUS': row[2],
            'USER_ID': row[3]
        }
        #cls.cur.close()
        return order

    #function for updating a particular order status
    @classmethod
    def update_order_status(cls,status,order_no):
        
        query = "UPDATE ORDERS SET STATUS = %s WHERE ORDER_NO = %s "
        cls.cur.execute(query,(status,order_no))
    
        order = {
            
            'status' :status
        }
        cls.orders.append(order)
        return order
 
        #cls.cur.close()
    

    #function for deleting a specific order
    def delete_order(self,order_no):
        query = "DELETE FROM ORDERS WHERE ORDER_NO = %s"
        self.cur.execute(query,(order_no,))
        self.cur.close




