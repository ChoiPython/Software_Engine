# Order_control.py
import pymysql
import datetime

class OrderControl:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='soft',
            password='0000',
            db='',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def save_order(self, table_num, cart_data):
        # 1) 주문 테이블에 주문 기본정보 추가
        now = datetime.datetime.now()
        order_time = now.strftime('%Y-%m-%d %H:%M:%S')

        insert_order_query = """
            INSERT INTO orderlist (table_num, order_time)
            VALUES (%s, %s)
        """
        self.cursor.execute(insert_order_query, (table_num, order_time))
        self.conn.commit()

        # 방금 추가된 주문번호 가져오기
        order_id = self.cursor.lastrowid

        # 2) 주문 상세 테이블에 항목별 메뉴 추가
        insert_detail_query = """
            INSERT INTO order_detail (order_id, menu_name, option_desc, quantity, price, image_path)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for item in cart_data:
            option_desc = '\n'.join(item['option']) if isinstance(item['option'], list) else item['option']
            self.cursor.execute(insert_detail_query, (
                order_id,
                item['menu_name'],
                option_desc,
                item['quantity'],
                item['price'],
                item['image_path']
            ))

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

        return order_id