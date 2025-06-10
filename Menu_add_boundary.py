import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from Option_add_boundary import OptionPopup  # 옵션창 코드 import
from Menu_add_control import *  # 메뉴 등록 컨트롤러 import
from Administer_main_boundary import *

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

class MenuForm(tk.Toplevel):
    def __init__(self, menu_list):
        super().__init__()
        self.title("메뉴 등록")
        self.geometry("750x450")
        self.resizable(False, False)
        self.configure(bg="#ffffff")
        self.grab_set()

        self.menu_name = list((menu_name[1] for menu_name in menu_list))    # 등록되어 있는 메뉴들
        self.cate_name = sorted(list(set(cate[0] for cate in menu_list)))   # 등록되어 있는 카테고리들
        print(self.cate_name)
        # print(self.menu)

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
        self.image_path = "기본이미지.jpg"  # 이미지 경로 저장 변수

        # 카테고리 드롭다운
        self.category_var = tk.StringVar(value="카테고리 지정")
        self.category_menu = tk.OptionMenu(self, self.category_var, "카테고리 지정", *self.cate_name)
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

        # 등록/취소 버튼
        self.menu_add_bt = tk.Button(self, text="등록", width=int(10*x_ratio), relief="solid", borderwidth=1, command=self.submit)
        self.menu_add_bt.place(x=int(370*x_ratio), y=int(220*y_ratio))
        self.bt = tk.Button(self, text="취소", width=int(10*x_ratio), relief="solid", borderwidth=1, command=self.quit)
        self.bt.place(x=int(470*x_ratio), y=int(220*y_ratio))

        # 메뉴 등록 컨트롤 클래스 인스턴스 생성
        self.add_control = Menu_add_control()

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
            self.image_path = file_path

    def submit(self):
        # 입력 데이터 수집
        category = self.category_var.get()
        menu_name = self.menu_text.get()
        price = self.price_txt.get()
        description = self.desc_txt.get()

        # 데이터 유효성 검사 및 변환
        # 가격이 숫자가 아니면 등록 불가
        if price not in ["", "가격"] and not price.isdigit():
            messagebox.showerror("입력 오류", "가격은 숫자만 입력하세요.")
            return

        menu_data = {
            'category': category if category != "카테고리 지정" else None,
            'menu': menu_name if menu_name not in ["", "메뉴명"] else None,
            'price': int(price) if price.isdigit() else None,
            'description': description if description not in ["", "메뉴 설명"] else None,
            'image': self.image_path
        }

        # 필수 입력값 체크 (예시: 메뉴명, 가격, 카테고리)
        if menu_data['menu'] == None or menu_data['price'] == None or menu_data['category'] == None: 
            messagebox.showerror("입력 오류", "메뉴명, 가격, 카테고리를 모두 입력하세요.")
            return
        
        # 등록되어 있는 메뉴 알림
        if menu_name in self.menu_name:
            messagebox.showerror("등록 오류", "이미 등록되어 있는 메뉴 입니다.")
            return

        # 메뉴 등록 컨트롤러 호출
        print(menu_data)
        result = self.add_control.menu_add(menu_data)

        # 결과 메시지 출력
        res = messagebox.showinfo("등록 결과", result)
        self.destroy()



    def quit(self):
        self.destroy()

    def open_must_option(self):
        OptionPopup(self, title="필수옵션 등록")

    def open_add_option(self):
        OptionPopup(self, title="추가옵션 등록")

if __name__ == "__main__":
    app = MenuForm()
    app.mainloop()
