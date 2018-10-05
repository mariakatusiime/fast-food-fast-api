from webapp.controllers.db import Dbase

class CustomerOrders:
    con = Dbase()
    cur = con.curs
    orders = []

    def __init__(self, dish, price, status,user_id):
        
        self.dish = dish
        self.price = price

        self.status = status
        self.user_id = user_id
        

    # function that allows users to make orders
    
    def create_orders(self,quantity):
        
        query = "SELECT * FROM ORDERS WHERE USER_ID=%s"
        self.cur.execute(query,(self.user_id,))
        if query:
            query1 = "UPDATE ORDERS SET QUANTITY= %s WHERE USER_ID = %s"
            self.cur.execute(query1,(quantity+1,self.user_id))
            
        else:   
            query = "INSERT INTO ORDERS(DISH,PRICE,STATUS,USER_ID,QUANTINTY) VALUES (%s,%s,%s,%s,%s)"
           
            self.cur.execute(query,(self.dish,self.price,self.status,self.user_id,1))
            order = {
            
                 'dish'  : self.dish,
                 'price'  :self.price,
                 'status' :self.status,
                 'user_id':self.user_id,
                 
                    }
        self.orders.append(order)
        return order
        #self.cur.close()

    # function that displays all orders to admin    
    @classmethod
    def get_orders(cls):
        query = "SELECT ORDER_NO,DISH,PRICE,STATUS,USER_ID FROM ORDERS"
        
        cls.cur.execute(query)
        orderlist = cls.cur.fetchall()
        for orde in orderlist:
            order = {
                'ORDER_NO': orde[0],
                'DISH'    : orde[1],
                'PRICE'   : orde[2],
                'STATUS'  : orde[3],
                'USER_ID': orde[4]
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
    
    def update_order_status(self,status,order_no):
        query = "UPDATE ORDERS SET STATUS = %s WHERE ORDER_NO = %s "
        self.cur.execute(query,(status,order_no,))
        order = {
            
            'dish'  : self.dish,
            'price'  :self.price,
            'status' :self.status,
            'user_id':self.user_id
        }
        self.orders.append(order)
        return order
 
        #cls.cur.close()
    

    #function for deleting a specific order
    def delete_order(self,order_no):
        query = "DELETE FROM ORDERS WHERE ORDER_NO = %s"
        self.cur.execute(query,(order_no,))
        self.cur.close




