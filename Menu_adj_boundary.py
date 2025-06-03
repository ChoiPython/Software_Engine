import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from Option_add_boundary import OptionPopup  # 옵션창 코드 import

class MenuForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("메뉴 등록")
        self.geometry("600x320")
        self.configure(bg="#ffffff")

        # 좌측: 메뉴 사진 영역
        self.photo_frame = tk.Frame(self, width=150, height=150, highlightbackground="lightgreen", highlightthickness=1)
        self.photo_frame.place(x=20, y=20)
        self.photo_label = tk.Label(self.photo_frame, text="메뉴 사진", width=100, height=100, bg="white")
        self.photo_label.pack()
        self.photo = None

        self.image_bt = tk.Button(self, text="사진 선택", width=18, highlightbackground="white", highlightcolor="blue", command=self.select_photo, relief="solid", borderwidth=1)
        self.image_bt.place(x=30, y=180)

        # 우측: 입력 폼
        self.category_var = tk.StringVar(value="카테고리 지정")
        self.category_menu = tk.OptionMenu(self, self.category_var, "카테고리 지정", "한식", "중식", "일식", "양식")
        self.category_menu.config(width=23, relief="solid", borderwidth=1, anchor='w')
        self.category_menu.place(x=200, y=20)

        self.menu_text = tk.Entry(self, width=25, relief="solid", borderwidth=1)
        self.menu_text.insert(0, "메뉴명")
        self.menu_text.place(x=200, y=60)

        self.price_txt = tk.Entry(self, width=25, relief="solid", borderwidth=1)
        self.price_txt.insert(0, "가격")
        self.price_txt.place(x=200, y=100)

        self.desc_txt = tk.Entry(self, width=25, relief="solid", borderwidth=1)
        self.desc_txt.insert(0, "메뉴 설명")
        self.desc_txt.place(x=200, y=140)

        # 옵션 설정 버튼
        self.req_opt_pbt = tk.Button(self, text="필수옵션 설정", relief="solid", borderwidth=1, command=self.open_must_option)
        self.req_opt_pbt.place(x=200, y=180)
        self.plus1 = tk.Label(self, text="+", font=("Arial", 16))
        self.plus1.place(x=320, y=178)
        self.add_opt_pbt = tk.Button(self, text="추가옵션 설정", relief="solid", borderwidth=1, command=self.open_add_option)
        self.add_opt_pbt.place(x=340, y=180)
        self.plus2 = tk.Label(self, text="+", font=("Arial", 16))
        self.plus2.place(x=470, y=178)

        # 취소/등록 버튼
        self.bt = tk.Button(self, text="취소", width=10, relief="solid", borderwidth=1, command=self.quit)
        self.bt.place(x=380, y=240)
        self.menu_add_bt = tk.Button(self, text="등록", width=10, relief="solid", borderwidth=1, command=self.submit)
        self.menu_add_bt.place(x=480, y=240)

    # 아래 메서드들은 반드시 __init__ 밖에서 클래스의 메서드로 정의!
    def select_photo(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")]
        )
        if file_path:
            img = Image.open(file_path)
            img = img.resize((120, 120))
            self.photo = ImageTk.PhotoImage(img)
            self.photo_label.config(image=self.photo, text="")
            self.photo_label.image = self.photo

    def submit(self):
        messagebox.showinfo("등록", "메뉴가 등록되었습니다.")

    def quit(self):
        messagebox.showinfo("취소", "메뉴등록이 취소되었습니다.")

    def open_must_option(self):
        OptionPopup(self, title="필수옵션 등록")

    def open_add_option(self):
        OptionPopup(self, title="추가옵션 등록")

if __name__ == "__main__":
    app = MenuForm()
    app.mainloop()
