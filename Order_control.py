import pymysql

class OrderControl:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='0000',
            database='sys',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def save_order(self, table_num, cart_data):
        try:
            for item in cart_data:
                menu_name = item['menu_name']
                option = item['option']
                quantity = item['quantity']
                price = item['price']
                image_path = item['image_path']

                insert_query = """
                INSERT INTO order_list (table_num, menu_name, option, ammount, prise, image_path)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                self.cursor.execute(insert_query, (table_num, menu_name, option, quantity, price, image_path))

            self.conn.commit()
        finally:
            self.cursor.close()
            self.conn.close()