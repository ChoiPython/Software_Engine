import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from Option_add_boundary import OptionPopup  # 옵션창 코드 import

# 플레이스홀더 Entry 클래스
class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg'] if 'fg' in kwargs else 'black'

        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

        self._add_placeholder()

    def _clear_placeholder(self, event=None):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def _add_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color

class MenuForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("메뉴 등록")
        self.geometry("750x450")
        self.resizable(False, False)
        self.configure(bg="#ffffff")

        # 비율 계산
        x_ratio = 750 / 600
        y_ratio = 450 / 320

        # 메뉴 사진 프레임 (확대)
        self.photo_frame = tk.Frame(self, width=int(150*x_ratio), height=int(150*y_ratio), highlightbackground="lightgreen", highlightthickness=1)
        self.photo_frame.place(x=int(20*x_ratio), y=int(20*y_ratio))
        self.photo_frame.pack_propagate(False)
        self.photo_label = tk.Label(self.photo_frame, text="메뉴 사진", bg="white")
        self.photo_label.pack(fill="both", expand=True)
        self.photo = None

        # 카테고리 드롭다운
        self.category_var = tk.StringVar(value="카테고리 지정")
        self.category_menu = tk.OptionMenu(self, self.category_var, "카테고리 지정", "한식", "중식", "일식", "양식")
        self.category_menu.config(width=int(23*x_ratio), relief="solid", borderwidth=1, anchor='w')
        self.category_menu.place(x=int(190*x_ratio), y=int(20*y_ratio))

        # 플레이스홀더 Entry 사용
        self.menu_text = PlaceholderEntry(self, placeholder="메뉴명", width=int(25*x_ratio), relief="solid", borderwidth=1)
        self.menu_text.place(x=int(190*x_ratio), y=int(60*y_ratio))

        self.price_txt = PlaceholderEntry(self, placeholder="가격", width=int(25*x_ratio), relief="solid", borderwidth=1)
        self.price_txt.place(x=int(190*x_ratio), y=int(100*y_ratio))

        self.desc_txt = PlaceholderEntry(self, placeholder="메뉴 설명", width=int(25*x_ratio), relief="solid", borderwidth=1)
        self.desc_txt.place(x=int(190*x_ratio), y=int(140*y_ratio))

        # 사진 선택 버튼
        self.image_bt = tk.Button(self, text="사진 선택", width=int(18*x_ratio), highlightbackground="white", highlightcolor="blue", command=self.select_photo, relief="solid", borderwidth=1)
        self.image_bt.place(x=int(20*x_ratio), y=int(180*y_ratio))

        # 옵션 버튼과 + 버튼을 한 줄에 Frame에 넣기
        option_frame = tk.Frame(self, bg="#ffffff")
        option_frame.place(x=int(190*x_ratio), y=int(180*y_ratio))

        self.req_opt_pbt = tk.Button(option_frame, text="필수옵션 설정", relief="solid", borderwidth=1, command=self.open_must_option)
        self.req_opt_pbt.pack(side="left")
        self.plus1 = tk.Button(option_frame, text="+", font=("Arial", int(16*y_ratio)), 
                              relief="flat", borderwidth=0, bg="#ffffff", 
                              command=self.open_must_option, cursor="hand2")
        self.plus1.pack(side="left", padx=5)
        self.add_opt_pbt = tk.Button(option_frame, text="추가옵션 설정", relief="solid", borderwidth=1, command=self.open_add_option)
        self.add_opt_pbt.pack(side="left", padx=(0,5))
        self.plus2 = tk.Button(option_frame, text="+", font=("Arial", int(16*y_ratio)), 
                              relief="flat", borderwidth=0, bg="#ffffff", 
                              command=self.open_add_option, cursor="hand2")
        self.plus2.pack(side="left")

        # 등록/취소 버튼 (위치 바뀜)
        self.menu_add_bt = tk.Button(self, text="등록", width=int(10*x_ratio), relief="solid", borderwidth=1, command=self.submit)
        self.menu_add_bt.place(x=int(370*x_ratio), y=int(220*y_ratio))
        self.bt = tk.Button(self, text="취소", width=int(10*x_ratio), relief="solid", borderwidth=1, command=self.quit)
        self.bt.place(x=int(470*x_ratio), y=int(220*y_ratio))

    def select_photo(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")]
        )
        if file_path:
            x_ratio = 750 / 600
            y_ratio = 450 / 320
            img = Image.open(file_path)
            img = img.resize((int(150*x_ratio), int(150*y_ratio)), Image.LANCZOS)
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
