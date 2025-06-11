import pymysql

class OrderControl:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='soft',
            password='0000',
            database='table_order',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def save_order(self, table_num, cart_data):
        try:
            print(cart_data)
            for item in cart_data:
                table_num = item['table_num']
                menu_name = item['menu_name']
                image = item['image']
                quantity = item['quantity']
                option = item['option']
                if isinstance(option, list):
                    option = '+'.join(option)
                price = item['price']

                insert_query = """
                INSERT INTO order_list (table_num, menu_name, image, quantity, opt, price)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
                self.cursor.execute(insert_query, (table_num, menu_name, image, quantity, option, price))

            self.conn.commit()
        finally:
            self.cursor.close()
            self.conn.close()