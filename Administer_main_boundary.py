from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Menu_adj_control import Menu_adj_control
from Menu_adj_boundary import Menu_adj

class Administer_main:
    def __init__(self):
        self.window = Tk()
        self.window.title("관리자 메인")
        self.window.geometry("1200x800+100+100")
        self.data = Menu_adj_control()
        self.Menu_list = self.data.getMenu()
        self.ShowUi()
        self.window.mainloop()

    def ShowUi(self):
        # 프레임 구성
        self.head_frame = Frame(self.window, height=60, bg="#f0f0f0")
        self.head_frame.pack(side=TOP, fill=X)
        self.left_frame = Frame(self.window, width=200, bg="#e0e0e0")
        self.left_frame.pack(side=LEFT, fill=Y)
        self.right_frame = Frame(self.window, bg="#ffffff")
        self.right_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        self.right_top_frame = Frame(self.right_frame)
        self.right_top_frame.pack(side=TOP, fill=BOTH, expand=True)
        self.right_bottom_frame = Frame(self.right_frame, height=60)
        self.right_bottom_frame.pack(side=BOTTOM, fill=X)

        # 헤더
        Label(self.head_frame, text="메뉴 관리", font=("맑은 고딕", 20, "bold"), bg="#f0f0f0").pack(pady=10)

        # 카테고리 버튼
        self.cate_buttons = []
        self.cate_var = StringVar()
        self.cate_var.set("1.메인메뉴")
        self.ShowWidget()

        # 메뉴 표시
        self.setMenu(self.cate_var.get())

    def ShowWidget(self):
        # 카테고리 추출 및 버튼 생성
        for widget in self.left_frame.winfo_children():
            widget.destroy()
        self.cate_list = sorted(list(set(info[0] for info in self.Menu_list)))
        for cate in self.cate_list:
            btn = Button(self.left_frame, text=cate, width=20, height=2, command=lambda c=cate: self.cate_event(c))
            btn.pack(pady=5)
            self.cate_buttons.append(btn)

    def cate_event(self, category):
        self.cate_var.set(category)
        self.setMenu(category)

    def setMenu(self, category='1.메인메뉴'):
        # 메뉴 표시 영역 초기화
        for widget in self.right_top_frame.winfo_children():
            widget.destroy()

        # 해당 카테고리 메뉴만 추출
        menu = sorted([info for info in self.Menu_list if info[0] == category], key=lambda x: x[1])

        # 스크롤 가능한 캔버스
        canvas = Canvas(self.right_top_frame, bg="#ffffff")
        scrollbar = Scrollbar(self.right_top_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#ffffff")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # 메뉴 아이템 표시 (4열 그리드)
        for i, m in enumerate(menu):
            frame = Frame(scrollable_frame, bd=2, relief="groove", width=250, height=250)
            frame.grid(row=i // 4, column=i % 4, padx=10, pady=10)
            frame.grid_propagate(False)

            # 이미지 표시
            try:
                img = Image.open(m[4])
            except Exception:
                img = Image.open("기본이미지.jpg")
            img = img.resize((220, 150))
            img_tk = ImageTk.PhotoImage(img)
            label_img = Label(frame, image=img_tk)
            label_img.image = img_tk
            label_img.pack(pady=5)

            # 메뉴명, 가격, 설명
            Label(frame, text=m[1], font=("맑은 고딕", 14, "bold")).pack()
            Label(frame, text=f"{m[2]}원", font=("맑은 고딕", 12)).pack()
            Label(frame, text=m[3], font=("맑은 고딕", 10), wraplength=200, justify=LEFT).pack()

            # 수정 버튼
            btn = Button(frame, text="수정", command=lambda menu=m: self.menu_adj_event(menu))
            btn.pack(pady=5)

    def menu_adj_event(self, menu):
        # parent_window로 self.window 전달
        menu_adj = Menu_adj(self.Menu_list, menu, parent_window=self.window)
        self.window.wait_window(menu_adj.window)

if __name__ == "__main__":
    Administer_main()
