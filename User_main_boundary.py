from tkinter import *

class User_main:
    def __init__(self):
        self.user_window = Tk()
        self.user_window.title("사용자 메인화면")
        self.user_window.geometry("1200x800+300+100")
        self.user_window.resizable(True, True)
        self.ShowUi()       # 화면 출력
        self.ShowWidget()   # 위젯 출력
        self.user_window.mainloop()

    # 프레임 세팅
    def ShowUi(self):
        self.head_frame = self.setFrame_pack(self.user_window, 'top', 1200, 100)               # 상단 프레임
        self.left_frame = self.setFrame_pack(self.user_window, 'left', 200, 700)               # 좌측 프레임
        self.right_frame = self.setFrame_pack(self.user_window, 'left', 1000, 700)             # 우측 프레임
        self.right_top_frame = self.setFrame_pack(self.right_frame, 'top',1000, 600)           # 우측 상단 프레임
        self.right_bottom_frame = self.setFrame_pack(self.right_frame, 'bottom', 1000, 100)    # 우측 하단 프레임

        self.setlabel(self.head_frame, '테이블 1', 10, 1)         # 테이블 번호 라벨



    def ShowWidget(self):
        # 카테고리 버튼 배치
        self.cate = ['카테고리1', '카테고리2', '카테고리3', '카테고리4', '카테고리5']
        self.setButton(self.left_frame, 'top', self.cate[0], 15, 3, y=20)
        self.setButton(self.left_frame, 'top', self.cate[1], 15, 3, y=20)
        self.setButton(self.left_frame, 'top', self.cate[2], 15, 3, y=20)
        self.setButton(self.left_frame, 'top', self.cate[3], 15, 3, y=20)
        self.setButton(self.left_frame, 'top', self.cate[4], 15, 3, y=20)

        # 결제요청, 장바구니, 주문목록 버튼 배치
        # req_pay_bt = Button(right_bottom_frame, text='결제요청', width= 15, height= 3)
        # cart_bt = Button(right_bottom_frame, text='장바구니', width= 15, height= 3)
        # orderlist_bt = Button(right_bottom_frame, text='주문목록', width= 15, height= 3)
        self.setButton(self.right_bottom_frame, 'right', '결제요청', 15, 3, x=10, y=0)
        self.setButton(self.right_bottom_frame, 'right', '장바구니', 15, 3, x=10, y=0)
        self.setButton(self.right_bottom_frame, 'right', '주문목록', 15, 3, x=10, y=0)

    # 라벨 생성
    def setlabel(self, frame, txt, wid, hei, t_font=("맑은고딕", 20)):             # 라벨 생성 함수
        label = Label(frame, text = txt, width=wid, height=hei, font=t_font)
        label.pack(side = "left")
        
    # pcak로 생성하는 프레임
    def setFrame_pack(self, frame, pos, wid, hei):             # 프레임 생성 함수
        frame = Frame(frame, width = wid, height=hei, relief="solid", bd = 0.5)    #, background="#C1FFD4"
        frame.pack(side = pos)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        return frame

    # grid로 생성하는 프레임
    def setFrame_grid(self, frame, wid, hei, row, col):
        frame = Frame(frame, width = wid, height = hei, relief="solid", bd = 0.5)
        frame.grid(row = row, column= col)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        return frame

    def setButton(self, frame, pos, txt, wid, hei, x=10, y=3):            # 버튼 생성 함수
        button = Button(frame, text=txt, width=wid, height=hei)
        button.pack(side=pos, padx = x, pady = y)
        return button
        

    def setMenu():              # 메뉴 생성 함수
        pass

    # user_window = Tk()      # 윈도우 생성

    # 메인 프레임 생성 
    # head_frame = setFrame_pack(user_window, 'top', 1200, 100)               # 상단 프레임
    # left_frame = setFrame_pack(user_window, 'left', 200, 700)               # 좌측 프레임
    # right_frame = setFrame_pack(user_window, 'left', 1000, 700)             # 우측 프레임
    # right_top_frame = setFrame_pack(right_frame, 'top',1000, 600)           # 우측 상단 프레임
    # right_bottom_frame = setFrame_pack(right_frame, 'bottom', 1000, 100)    # 우측 하단 프레임


    # 메뉴 프레임 생성
    # right_top_frame1 = setFrame_grid(right_top_frame, 250, 250, 0, 0)      # , background="#C1FFD4"
    # right_top_frame2 = setFrame_grid(right_top_frame, 250, 250, 0, 1)      # , background="#C1FFD4"
    # right_top_frame3 = setFrame_grid(right_top_frame, 250, 250, 0, 2)      # , background="#C1FFD4"
    # right_top_frame4 = setFrame_grid(right_top_frame, 250, 250, 0, 3)      # , background="#C1FFD4"
    # right_top_frame5 = setFrame_grid(right_top_frame, 250, 250, 1, 0)      # , background="#C1FFD4"
    # right_top_frame6 = setFrame_grid(right_top_frame, 250, 250, 1, 1)      # , background="#C1FFD4"
    # right_top_frame7 = setFrame_grid(right_top_frame, 250, 250, 1, 2)      # , background="#C1FFD4"
    # right_top_frame8 = setFrame_grid(right_top_frame, 250, 250, 1, 3)      # , background="#C1FFD4"


    # 라벨생성
    # setlabel(head_frame, '테이블 1', 10, 1)         # 테이블 번호 라벨


    # 결제요청, 장바구니, 주문목록 버튼 생성
    # req_pay_bt = Button(right_bottom_frame, text='결제요청', width= 15, height= 3)
    # cart_bt = Button(right_bottom_frame, text='장바구니', width= 15, height= 3)
    # orderlist_bt = Button(right_bottom_frame, text='주문목록', width= 15, height= 3)

    # # 결제요청, 장바구니, 주문목록 버튼 배치
    # orderlist_bt.pack(side = 'right', padx = 10)
    # cart_bt.pack(side = 'right', padx = 10)
    # req_pay_bt.pack(side = 'right', padx = 10)



    # # 카테고리 버튼 생성
    # cate_but1 = Button(left_frame, text = '카테고리1', width=15, height=3)
    # cate_but2 = Button(left_frame, text = '카테고리2', width=15, height=3)
    # cate_but3 = Button(left_frame, text = '카테고리3', width=15, height=3)
    # cate_but4 = Button(left_frame, text = '카테고리4', width=15, height=3)


    # # 카테고리 버튼 배치
    # cate_but1.pack(pady = 20)
    # cate_but2.pack(pady = 20)
    # cate_but3.pack(pady = 20)
    # cate_but4.pack(pady = 20)


    # # 윈도우창 조작
    # user_window.title("사용자 메인화면")
    # user_window.geometry("1200x800+300+100")
    # user_window.resizable(True, True)

    # user_window.mainloop()


if __name__ == "__main__":
    mainui = User_main()