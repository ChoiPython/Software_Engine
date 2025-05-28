
from tkinter import *
mainui = Tk()


def menu_add_event(bt_txt):
    print("버튼누르기")
    pass

menu_add_bt = Button(mainui, padx=9, pady=3, text = "담기", command = menu_add_event)
menu_bt = Button(mainui, padx=9, pady=3, text = "담기", command = menu_add_event)

menu_frame = Frame(mainui, width=300, height=300, background="#C1FFD4")



# 위젯 배치
menu_add_bt.pack()


# 프레임 배치
menu_frame.pack()

# 윈도우창 조작
mainui.title("메인화면")
mainui.geometry("1080x720+100+100")
mainui.resizable(False, False)


mainui.mainloop()
### 수정
print("hello World!")
print("hello World!")
print("hello World!")
print("hello World!")