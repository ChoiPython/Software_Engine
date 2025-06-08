
# 데이터 연동
import pymysql
class getMenu:
    def __init__(self):
        pass

    def get(self):
        self.conn = pymysql.connect(host='127.0.0.1', user = 'soft@localhost', password='0000', db='Table_Order')

        self.cursor = self.conn.cursor()      # 데이터 조작할 커서 생성
        self.select_query = "select * from menu"    # 전체 데이터 가져오는 쿼리문

        self.cursor.execute(self.select_query)   # 쿼리 입력
        self.result = self.cursor.fetchall()  # 명령어 결과 튜플로 반환

        self.conn.commit()       # 입력한 데이터 저장하기(데이터 삽입, 수정, 삭제에 사용됨.)

        self.cursor.close()
        self.conn.close()

        return self.result

if __name__ == "__main__":
    getmenu = getMenu()
    result = getmenu.get()
    cate = sorted(list((info for info in result if info[0] == '카테고리1')), key = lambda x: x[1])
    for i in cate :
        print(i)



        # 데이터 - 삽입, 수정, 삭제에 사용됨
        # self.cate = '카테고리3'
        # self.menu_name = '물컵'
        # self.image = '기본이미지.jpg'
        # self.price = 0
        # self.menu_desc = None
        # self.soldout = False
        # self.data = (self.cate, self.menu_name, self.image, self.price, self.menu_desc, self.soldout)
        # self.insert_query = "insert into menu values (%s, %s, %s, %s, %s, %s)"   # 쿼리문
