from tkinter import *

class User_main:
    def __init__(self):
        pass

    def setlabel(frame, txt, wid, hei, t_font=("맑은고딕", 20)):             # 라벨 생성 함수
        label = Label(frame, text = txt, width=wid, height=hei, font=t_font)
        label.pack(side = "left")
        
    def setFrame_pack(frame, pos, wid, hei):             # 프레임 생성 함수
        frame = Frame(frame, width = wid, height=hei, relief="solid", bd = 0.5)    #, background="#C1FFD4"
        frame.pack(side = pos)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        return frame

    def setFrame_grid(frame, wid, hei, row, col):
        frame = Frame(frame, width = wid, height = hei, relief="solid", bd = 0.5)
        frame.grid(row = row, column= col)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        return frame

    def setButton():            # 버튼 생성 함수
        pass
    def setMenu():              # 메뉴 생성 함수
        pass

    user_window = Tk()      # 윈도우 생성

    # 메인 프레임 생성 
    head_frame = setFrame_pack(user_window, 'top', 1200, 100)               # 상단 프레임
    left_frame = setFrame_pack(user_window, 'left', 200, 700)               # 좌측 프레임
    right_frame = setFrame_pack(user_window, 'left', 1000, 700)             # 우측 프레임
    right_top_frame = setFrame_pack(right_frame, 'top',1000, 600)           # 우측 상단 프레임
    right_bottom_frame = setFrame_pack(right_frame, 'bottom', 1000, 100)    # 우측 하단 프레임


    # 메뉴 프레임 생성
    right_top_frame1 = setFrame_grid(right_top_frame, 250, 250, 0, 0)      # , background="#C1FFD4"
    right_top_frame2 = setFrame_grid(right_top_frame, 250, 250, 0, 1)      # , background="#C1FFD4"
    right_top_frame3 = setFrame_grid(right_top_frame, 250, 250, 0, 2)      # , background="#C1FFD4"
    right_top_frame4 = setFrame_grid(right_top_frame, 250, 250, 0, 3)      # , background="#C1FFD4"
    right_top_frame5 = setFrame_grid(right_top_frame, 250, 250, 1, 0)      # , background="#C1FFD4"
    right_top_frame6 = setFrame_grid(right_top_frame, 250, 250, 1, 1)      # , background="#C1FFD4"
    right_top_frame7 = setFrame_grid(right_top_frame, 250, 250, 1, 2)      # , background="#C1FFD4"
    right_top_frame8 = setFrame_grid(right_top_frame, 250, 250, 1, 3)      # , background="#C1FFD4"


    # 라벨생성
    setlabel(head_frame, '테이블 1', 10, 1)         # 테이블 번호 라벨


    # 결제요청, 장바구니, 주문목록 버튼 생성
    req_pay_bt = Button(right_bottom_frame, text='결제요청', width= 15, height= 3)
    cart_bt = Button(right_bottom_frame, text='장바구니', width= 15, height= 3)
    orderlist_bt = Button(right_bottom_frame, text='주문목록', width= 15, height= 3)

    # 결제요청, 장바구니, 주문목록 버튼 배치
    orderlist_bt.pack(side = 'right', padx = 10)
    cart_bt.pack(side = 'right', padx = 10)
    req_pay_bt.pack(side = 'right', padx = 10)



    # 카테고리 버튼 생성
    cate_but1 = Button(left_frame, text = '카테고리1', width=15, height=3)
    cate_but2 = Button(left_frame, text = '카테고리2', width=15, height=3)
    cate_but3 = Button(left_frame, text = '카테고리3', width=15, height=3)
    cate_but4 = Button(left_frame, text = '카테고리4', width=15, height=3)


    # 카테고리 버튼 배치
    cate_but1.pack(pady = 20)
    cate_but2.pack(pady = 20)
    cate_but3.pack(pady = 20)
    cate_but4.pack(pady = 20)


    # 윈도우창 조작
    user_window.title("사용자 메인화면")
    user_window.geometry("1200x800+300+100")
    user_window.resizable(True, True)

    user_window.mainloop()

