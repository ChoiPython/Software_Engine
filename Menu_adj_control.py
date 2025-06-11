
# 데이터 연동
import pymysql
class Menu_adj_control:
    def __init__(self):
        pass

    def menu_adj(self, new_menu, bf_menu):
        
        """
        메뉴 등록 메서드
        Args:
            menu_data (dict): {
                {'category': '한식', 
                'menu': '돈까스', 
                'price': 10000, 'description': 
                '바삭한 돼지고기 돈까스', 
                'image': 'C:/Users/wndud/Desktop/25-1학기/소프트웨어공학/5. 구현/기본이미지.jpg'}
            }"""
        
        self.conn = pymysql.connect(host='localhost', user = 'soft', password='0000', db='Table_Order')
        self.cursor = self.conn.cursor()      # 데이터 조작할 커서 생성
        # ['한식', '돈까스', 10000, '바삭한 돼지고기 돈까스', 'C:/Users/wndud/Desktop/25-1학기/소프트웨어공학/5. 구현/기본이미지.jpg']
        self.menu_data = [val for k, val in new_menu.items() ]
        self.menu_data[4] = self.menu_data[4].split("/")[-1]    # 경로빼고 이미지 이름만
        print(self.menu_data)
        print(bf_menu)
        # # 데이터 - 삽입, 수정, 삭제에 사용됨
        self.update_query = f"update menu set category = '{self.menu_data[0]}', menu ='{self.menu_data[1]}', image='{self.menu_data[4]}', price={self.menu_data[2]}, menu_desc = '{self.menu_data[3]}', soldout='0' where menu = '{bf_menu}'"    # 전체 데이터 가져오는 쿼리문
        self.cursor.execute(self.update_query)   # 쿼리 입력

        self.conn.commit()       # 입력한 데이터 저장하기(데이터 삽입, 수정, 삭제에 사용됨.)

        self.cursor.close()
        self.conn.close()
        return "메뉴 등록 완료"

    def Option_adj(self, menu, req_opt, add_opt):
        self.conn = pymysql.connect(host='localhost', user = 'soft', password='0000', db='Table_Order')
        self.cursor = self.conn.cursor()      # 데이터 조작할 커서 생성
        # ['한식', '돈까스', 10000, '바삭한 돼지고기 돈까스', 'C:/Users/wndud/Desktop/25-1학기/소프트웨어공학/5. 구현/기본이미지.jpg']
        self.menu_data = [val for k, val in menu.items() ]
        print(self.menu_data[1])
        print("req_opt", req_opt)
        print("add_opt", add_opt)

        self.select_query = f"select * from `option` where menu='{self.menu_data[1]}'"    # 전체 데이터 가져오는 쿼리문
        self.cursor.execute(self.select_query)   # 쿼리 입력
        self.result = self.cursor.fetchall()  # 명령어 결과 튜플로 반환
    
        # # 데이터 - 삽입, 수정, 삭제에 사용됨

        print(type(menu), type(req_opt), type(add_opt))
        for i in range(len(req_opt)):   # 필수 옵션 저장
            # print(self.menu_data[1] in self.result[0] and req_opt[i][0] in self.result[1] and self.result[i][-1] == 1)
            if self.menu_data[1] in self.result[0] and req_opt[i][0] in self.result[1] and self.result[i][-1] == 1:   # 이미 등록되어 있기 때문에 등록 x
                pass

            else:
                self.insert_query = f"insert into `option` values('{self.menu_data[1]}', '{req_opt[i][0]}', '{req_opt[i][1]}', '1')"    # 전체 데이터 가져오는 쿼리문
                self.cursor.execute(self.insert_query)   # 쿼리 입력
                self.conn.commit()       # 입력한 데이터 저장하기(데이터 삽입, 수정, 삭제에 사용됨.)

        for i in range(len(add_opt)):   # 추가 옵션 저장
            if self.menu_data[1] in self.result[0] and add_opt[i][0] in self.result[1] and self.result[i][-1] == 1:   # 이미 등록되어 있기 때문에 등록 x
                pass

            else:
                self.insert_query = f"insert into `option` values('{self.menu_data[1]}',  '{add_opt[0]}', '{add_opt[1]}', '0')"    # 전체 데이터 가져오는 쿼리문
                self.cursor.execute(self.insert_query)   # 쿼리 입력
                self.conn.commit()       # 입력한 데이터 저장하기(데이터 삽입, 수정, 삭제에 사용됨.)

if __name__ == "__main__":
    delete_menu = Menu_adj_control()
    menu = {'category': '1.메인메뉴', 
            'menu': '오뎅탕', 
            'price': 10000,
            'description': '얼큰한 오뎅탕', 
            'image': '기본이미지.jpg'}

    delete_menu.menu_add(menu)
    # cate = sorted(list((info for info in result if info[0] == '카테고리1')), key = lambda x: x[1])
    # for i in cate :
    #     print(i)




