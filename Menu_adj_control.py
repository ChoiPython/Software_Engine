import pymysql

class Menu_adj_control:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def menu_adj(self, original_name, new_data):
        """메뉴 정보 업데이트 메서드
        Args:
            original_name (str): 수정 대상 메뉴명
            new_data (dict): {'category':값, 'menu':값, 'image':값, 'price':값, 'description':값}
        """
        try:
            # 1. DB 연결 설정
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='soft@localhost',
                password='0000',
                db='Table_Order'
            )
            self.cursor = self.conn.cursor()

            # 2. 동적 쿼리 생성 로직
            set_clauses = []
            params = []
            for key, value in new_data.items():
                if value is not None:
                    set_clauses.append(f"{key}=%s")
                    params.append(value)
            
            if not set_clauses:
                return "수정할 데이터가 없습니다"

            # 3. 안전한 파라미터 바인딩
            query = f"UPDATE menu SET {', '.join(set_clauses)} WHERE menu=%s"
            params.append(original_name)
            
            self.cursor.execute(query, tuple(params))
            self.conn.commit()
            return "수정 성공"

        except Exception as e:
            if self.conn:
                self.conn.rollback()
            return f"오류 발생: {str(e)}"
        finally:
            # 4. 자원 해제
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
