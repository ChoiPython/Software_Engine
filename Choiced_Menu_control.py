from User_main_boundary import *


class Choiced_Menu_control:
    def __init__(self, user_main):
        self.user_main = user_main
        pass

    
    def add_cart(self, menu_info):
        # menu: 메뉴 이름
        # menu_img: 메뉴 이미지
        # self.selected_required_option_name 선택한 필수 옵션
        # self.select_add_opt: 선택한 추가 옵션 리스트
        # self.quantity: 총 수량
        # self.total: 총 가격
        self.user_main.cart.append(menu_info)
        print(self.user_main.cart)
        pass

    



if __name__ == "__main__":
    pass




