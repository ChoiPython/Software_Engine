import pymysql

class Menu_add_control:
    def __init__(self):
        pass

    def menu_add(self, menu_data):
        """
        메뉴 등록 메서드
        Args:
            menu_data (dict): {
                'category': ...,
                'menu': ...,
                'image': ...,
                'price': ...,
                'description': ...
            }
        """
        try:
            self.conn = pymysql.connect(host='localhost', user = 'soft', password='0000', db='Table_Order')
            self.cursor = self.conn.cursor()

            # 컬럼명과 값 분리
            columns = []
            values = []
            placeholders = []
            for key, value in menu_data.items():
                if value is not None:
                    columns.append(key)
                    values.append(value)
                    placeholders.append('%s')

            if not columns:
                return "등록할 데이터가 없습니다."

            # INSERT 쿼리 생성
            insert_query = f"INSERT INTO menu ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"
            self.cursor.execute(insert_query, tuple(values))
            self.conn.commit()
            return "등록 성공"
        except Exception as e:
            if self.conn:
                self.conn.rollback()
            return f"오류 발생: {str(e)}"
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()

# 사용 예시
if __name__ == "__main__":
    add_menu = Menu_add_control()
    menu_data = {
        'category': '한식',
        'menu': '비빔밥',
        'image': 'bibimbap.jpg',
        'price': 9000,
        'description': '신선한 야채와 고추장'
    }
    result = add_menu.menu_add(menu_data)
    print(result)
