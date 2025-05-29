from tkinter import *

def setlabel():             # 라벨 생성 함수
    pass
def setFrame():             # 프레임 생성 함수
    pass
def setButton():            # 버튼 생성 함수
    pass
def setMenu():              # 메뉴 생성 함수
    pass

user_window = Tk()      # 윈도우 생성

# 메인 프레임 생성,background="#BBC43C"
table_num_frame = Frame(user_window, width = 1200, height=100, relief="solid", bd = 0.5, background="#C1FFD4")
cate_frame = Frame(user_window, width = 200, height = 700, relief="solid", bd = 0.5, background="#C1FFD4")
menu_frame = Frame(user_window, width = 1000, height = 700, relief="solid", bd = 0.5, background="#4E77D6")

# 메뉴 프레임 생성
menu_info_frame1 = Frame(menu_frame, width = 250, height = 350, relief="solid", bd = 0.5, background="#C1FFD4")
menu_info_frame2 = Frame(menu_frame, width = 250, height = 350, relief="solid", bd = 0.5, background="#C1FFD4")
menu_info_frame3 = Frame(menu_frame, width = 250, height = 350, relief="solid", bd = 0.5, background="#C1FFD4")
menu_info_frame4 = Frame(menu_frame, width = 250, height = 350, relief="solid", bd = 0.5, background="#C1FFD4")
menu_info_frame5 = Frame(menu_frame, width = 250, height = 350, relief="solid", bd = 0.5, background="#C1FFD4")
menu_info_frame6 = Frame(menu_frame, width = 250, height = 350, relief="solid", bd = 0.5, background="#C1FFD4")

# 라벨생성
table_num = Label(table_num_frame, text = "테이블1", width=10, height=1, font=("맑은고딕",20))


# 카테고리 버튼 생성
cate_but1 = Button(cate_frame, text = '카테고리1', width=15, height=3)
cate_but2 = Button(cate_frame, text = '카테고리2', width=15, height=3)
cate_but3 = Button(cate_frame, text = '카테고리3', width=15, height=3)
cate_but4 = Button(cate_frame, text = '카테고리4', width=15, height=3)


# 카테고리 버튼 배치
cate_but1.pack(pady = 20)
cate_but2.pack(pady = 20)
cate_but3.pack(pady = 20)
cate_but4.pack(pady = 20)



# 테이블번호 라벨 배치
table_num.pack(side = "left")


# 메뉴 프레임 배치
menu_info_frame1.grid(row = 0, column=0)
menu_info_frame2.grid(row = 0, column=1)
menu_info_frame3.grid(row = 0, column=2)
menu_info_frame4.grid(row = 0, column=3)
menu_info_frame5.grid(row = 0, column=4)
menu_info_frame6.grid(row = 1, column=0)



# 메인 프레임 배치
table_num_frame.pack(side = "top")
table_num_frame.pack_propagate(False)   # 위젯에 의해 프레임크기 변경 안되게 함

cate_frame.pack(side = "left", fill='both')
cate_frame.pack_propagate(False)

menu_frame.pack(side = "left", fill='both')
menu_frame.grid_propagate(False)


# 윈도우창 조작
user_window.title("사용자 메인화면")
user_window.geometry("1200x800+300+100")
user_window.resizable(True, True)

user_window.mainloop()

