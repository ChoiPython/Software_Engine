from User_main_boundary import *


class Choiced_Menu_control:
    def __init__(self, user_main):
        self.user_main = user_main
        pass

    
    def add_cart(self, menu_info):
        def cart_add_count(menu_info, idx):
            self.user_main.cart[idx][4] += menu_info[4]

        def cart_add_new(menu_info):
            self.user_main.cart.append(menu_info)
            
        def Check_cart(menu_info):
            idx = 0
            check = 0   
            for cart in self.user_main.cart:
                # 메뉴 명이 같고                필수 옵션이 같고        정렬된 추가옵션이 같으면
                if menu_info[0] == cart[0] and menu_info[2] == cart[2] and sorted(menu_info[3]) == sorted(cart[3]):
                    cart_add_count(menu_info, idx)
                    check= 1
                    break
                idx+=1

            if check == 0:  # 새로 추가
                cart_add_new(menu_info)
                    
        # menu: 메뉴 이름
        # menu_img: 메뉴 이미지
        # self.selected_required_option_name 선택한 필수 옵션
        # self.select_add_opt: 선택한 추가 옵션 리스트
        # self.quantity: 총 수량
        # self.total: 총 가격
        Check_cart(menu_info)

        print(self.user_main.cart)
        
        pass

    



if __name__ == "__main__":
    pass




