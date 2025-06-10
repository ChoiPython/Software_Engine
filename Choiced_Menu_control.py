from User_main_boundary import *


class Choiced_Menu_control:
    def __init__(self, user_main):
        self.user_main = user_main
        pass

    
    def add_cart(self, menu_info):
        
        def Check_cart(menu_info):
            idx = 0
            check = 0   
            # print(self.user_main.cart)
            for cmp in self.user_main.cart:
                # print(f"선택한 메뉴정보: {menu_info[:4]}")
                # print(f"기존 메뉴정보: {cmp[:4]}")
                # 메뉴 명이 같고                필수 옵션이 같고
                if menu_info[0] == cmp[0] and menu_info[2] == cmp[2]:
                    # 정렬된 추가옵션이 같으면
                    if sorted(menu_info[3]) == sorted(cmp[3]):
                        # 수량만 증가
                        self.user_main.cart[idx][4] += menu_info[4]
                        check= 1
                        break

                idx+=1

            if check == 0:
                print("menu_info: ",menu_info)
                self.user_main.cart.append(menu_info)
                    
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




