
class Menu_Add:
    all_cate = []           # 전체 카테고리
    menu_data = []          # 모든 메뉴명 데이터
    select_cate = str()     # 선택한 카테고리
    menu = str()            # 메뉴명
    price = int()           # 가격
    menu_desc = str()       # 메뉴설명
    image_adr = str()       # 이미지 주소
    option = []             # 옵션 내용

    def __init__(self):
        pass

    def Menu_Add(self):
        
        if self.menu not in self.menu_data and self.select_cate != 'NULL' and self.menu != 'NULL' and self.price != 'NULL':
            print("메뉴를 등록하였습니다.")

        else:
            print("메뉴가 등록되어 있거나 필수값을 입력하지 않으셨습니다.")
        pass

# -------------------------------------------------------------------------------------------------------------------------------------------------
        if self.menu not in self.menu_data:
            if self.select_cate != 'NULL' and self.menu != 'NULL' and self.price != 'NULL':
                print("메뉴가 등록되었습니다.")
                

            else:
                print("필수값이 입력되지 않았습니다.")
                pass

        else:
            print("메뉴가 이미 등록되어 있습니다.")




    def getMenu():
        print("메뉴를 조회하였습니다.")
        



menu_add = Menu_Add()
menu_add.getMenu()
menu_add.Menu_Add()

# github 테스트
# github 테스트2
# 작업수행
# 수정