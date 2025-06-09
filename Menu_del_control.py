
# 데이터 연동
import pymysql
class Menu_del_control:
    def __init__(self):
        pass

    def menu_del(self, menu):
        
        self.conn = pymysql.connect(host='localhost', user = 'soft', password='0000', db='Table_Order')

        self.cursor = self.conn.cursor()      # 데이터 조작할 커서 생성

        # 데이터 - 삽입, 수정, 삭제에 사용됨
        self.delete_query = f"delete from menu where menu='{menu}'"    # 전체 데이터 가져오는 쿼리문
        self.cursor.execute(self.delete_query)   # 쿼리 입력

        # 데이터 확인
        # self.select_query = "select * from menu"    # 전체 데이터 가져오는 쿼리문
        # self.cursor.execute(self.select_query)   # 쿼리 입력
        # self.result = self.cursor.fetchall()  # 명령어 결과 튜플로 반환

        self.conn.commit()       # 입력한 데이터 저장하기(데이터 삽입, 수정, 삭제에 사용됨.)

        self.cursor.close()
        self.conn.close()



if __name__ == "__main__":
    delete_menu = Menu_del_control()
    delete_menu.menu_del('메뉴18')
    # cate = sorted(list((info for info in result if info[0] == '카테고리1')), key = lambda x: x[1])
    # for i in cate :
    #     print(i)




