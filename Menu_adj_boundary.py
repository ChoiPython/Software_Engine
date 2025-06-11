from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
# from Option_add_boundary import OptionPopup  # 옵션창 코드 import
from Menu_adj_control import *  # 메뉴 등록 컨트롤러 import
from Administer_main_boundary import *
from getMenu import *

# 플레이스홀더 Entry 클래스
class PlaceholderEntry(Entry):
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
            self.delete(0, END)
            self['fg'] = self.default_fg_color

    def _add_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color

class Menu_adj:
    def __init__(self, menu_list, menu,parent_window=None):
        # print(menu)
        self.menu_data = {
            'category':  menu[0],
            'menu':  menu[1],
            'price':  menu[3],
            'description':  menu[4],
            'image': menu[2]
        }
        
        self.req_opt = []
        self.add_opt = []
        self.menu_list = menu_list
        self.get = getMenu()
        self.option_data = self.get.getOption(menu[1])  
        for i in self.option_data:
            # print("i", i)
            if i[3] == 1: # 필수옵션
                data = [i[1], i[2]]
                # print(data)
                self.req_opt.append(data)

            else:   # 추가옵션
                data = [i[1], i[2]]
                self.add_opt.append(data)
        self.menu_name = list((menu_name[1] for menu_name in self.menu_list))    # 등록되어 있는 메뉴들
        self.cate_name = sorted(list(set(cate[0] for cate in self.menu_list)))   # 등록되어 있는 카테고리들
        self.menu = [val for val in menu]    
        if self.menu[4] == None:
            self.menu[4] = "메뉴설명"
        # print(self.menu)

        self.run()

    def run(self):
        self.menu_add_window = Toplevel()
        self.menu_add_window.title("메뉴 수정")
        self.menu_add_window.geometry("1000x600")
        self.menu_add_window.resizable(False, False)
        self.menu_add_window.configure(bg="#ffffff")
        self.menu_add_window.grab_set()



        # 비율 계산
        x_ratio = 750 / 600
        y_ratio = 450 / 320

        
        # 메뉴 사진 프레임 (확대)
        self.image_frame = self.setFrame_pack(self.menu_add_window, 'left', 250, 1000)
        self.image_frame.pack(fill='y')
        self.photo_frame = Frame(self.image_frame, width=int(150*x_ratio), height=int(150*y_ratio), highlightbackground="lightgreen", highlightthickness=1)
        self.photo_frame.pack(side='top', pady=50)
        self.photo_frame.pack_propagate(False)
        self.photo_label = Label(self.photo_frame, text="메뉴 사진", bg="white")
        self.photo_label.pack(fill="both", expand=True)
        self.photo = None
        self.image_path = "기본이미지.jpg"  # 이미지 경로 저장 변수

        # 사진 선택 버튼
        self.image_bt = Button(self.image_frame, text="사진 선택", width=int(18*x_ratio), highlightbackground="white", highlightcolor="blue", command=self.select_photo, relief="solid", borderwidth=1)
        self.image_bt.pack(side= 'top', pady=20)

        
        
  
        # 입력 프레임
        self.ent_frame = self.setFrame_pack(self.menu_add_window, 'top', 750, 250)
        #frame = Frame(frame, width = wid, height=hei, relief="solid", bd = 0.5)    #, background="#C1FFD4"#
        #setFrame_pack(self, frame, pos, wid, hei):             # 프레임 생성 함수
        
        # 카테고리 드롭다운
        if self.menu_data['category'] == None:
            self.category_var = StringVar(value="카테고리 지정")
            self.category_menu = OptionMenu(self.ent_frame, self.category_var, "카테고리 지정", *self.cate_name)
            self.category_menu.config(width=int(23*x_ratio), relief="solid", borderwidth=1, anchor='w')
            self.category_menu.pack(side='top')
        else:
            self.category_var = StringVar(value=self.menu_data['category'])
            self.category_menu = OptionMenu(self.ent_frame, self.category_var, "카테고리 지정", *self.cate_name)
            self.category_menu.config(width=int(23*x_ratio), relief="solid", borderwidth=1, anchor='w')
            self.category_menu.pack(side='top')

        
        # 플레이스홀더 Entry 사용
        '''        self.menu_data = {
            'category': category if category != "카테고리 지정" else None,
            'menu': menu_name if menu_name not in ["", "메뉴명"] else None,
            'price': int(price) if price.isdigit() else None,
            'description': description if description not in ["", "메뉴 설명"] else None,
            'image': self.image_path
        }'''
        # print(self.menu_data)
        if self.menu_data['menu'] == None:
            self.menu_text = PlaceholderEntry(self.ent_frame, placeholder="메뉴명", width=int(25*x_ratio), relief="solid", borderwidth=1)
            self.menu_text.pack(side='top', pady = 20)

        else:
            self.menu_text = PlaceholderEntry(self.ent_frame, placeholder=self.menu_data['menu'], width=int(25*x_ratio), relief="solid", borderwidth=1)
            self.menu_text.pack(side='top', pady = 20)
        
        if self.menu_data['price'] == None:
            self.price_txt = PlaceholderEntry(self.ent_frame, placeholder="가격", width=int(25*x_ratio), relief="solid", borderwidth=1)
            self.price_txt.pack(side='top', pady = 20)

        else:
            self.price_txt = PlaceholderEntry(self.ent_frame, placeholder=self.menu_data['price'], width=int(25*x_ratio), relief="solid", borderwidth=1)
            self.price_txt.pack(side='top', pady = 20)

        if self.menu_data['description'] == None:
            self.desc_txt = PlaceholderEntry(self.ent_frame, placeholder="메뉴 설명", width=int(25*x_ratio), relief="solid", borderwidth=1)
            self.desc_txt.pack(side='top', pady = 20)

        else:
            self.desc_txt = PlaceholderEntry(self.ent_frame, placeholder=self.menu_data['description'], width=int(25*x_ratio), relief="solid", borderwidth=1)
            self.desc_txt.pack(side='top', pady = 20)

        self.opt_frame = self.setFrame_pack(self.menu_add_window, 'top', 750, 350)
        # # 옵션 버튼과 + 버튼을 한 줄에 Frame에 넣기
        # option_frame = Frame(self.menu_add_window, bg="#ffffff")
        # option_frame.place(x=int(190*x_ratio), y=int(180*y_ratio))
        self.req_opt_frame = self.setFrame_pack(self.opt_frame, 'left', 375, 350)
        self.add_opt_frame = self.setFrame_pack(self.opt_frame, 'left', 375, 350)

        if len(self.req_opt) == 0:
            self.req_opt_plabel = Label(self.req_opt_frame, text="필수옵션 설정", width=20, height=1, relief="solid", borderwidth=1, bg="white")
            self.req_opt_plabel.pack(side="top", pady=20)

            self.req_opt_pbt = Button(self.req_opt_frame, text="+", font=("Arial", int(16*y_ratio)), 
                                relief="flat", borderwidth=0,
                                command=self.open_req_option, cursor="hand2")
            self.req_opt_pbt.pack(side="top")

        else:
            for i in self.req_opt:  # 등록되어 있는 옵션들 출력
                Label(self.req_opt_frame, text=i[0] + '\t' + str(i[1]), width=20, height=1, relief="solid", borderwidth=1, bg="white").pack(side="top", pady=10)
                
            self.req_opt_plabel = Label(self.req_opt_frame, text="필수옵션 설정", width=20, height=1, relief="solid", borderwidth=1, bg="white")
            self.req_opt_plabel.pack(side="top", pady=10)

            self.req_opt_pbt = Button(self.req_opt_frame, text="+", font=("Arial", int(16*y_ratio)), 
                                relief="flat", borderwidth=0,
                                command=self.open_req_option, cursor="hand2")
            self.req_opt_pbt.pack(side="top")
            pass

        if len(self.add_opt) == 0:
            self.add_opt_plabel = Label(self.add_opt_frame, text="추가옵션 설정", width=20, height=1, relief="solid", borderwidth=1, bg="white")
            self.add_opt_plabel.pack(side="top", pady=20)

            self.add_opt_pbt = Button(self.add_opt_frame, text="+", font=("Arial", int(16*y_ratio)), 
                                relief="flat", borderwidth=0,
                                command=self.open_add_option, cursor="hand2")
            self.add_opt_pbt.pack(side="top")

        else:
            for i in self.add_opt:  # 등록되어 있는 옵션들 출력
                Label(self.add_opt_frame, text=i[0] + '\t' + str(i[1]), width=20, height=1, relief="solid", borderwidth=1, bg="white").pack(side="top", pady=10)
                
            self.add_opt_plabel = Label(self.add_opt_frame, text="추가 옵션 설정", width=20, height=1, relief="solid", borderwidth=1, bg="white")
            self.add_opt_plabel.pack(side="top", pady=10)

            self.add_opt_pbt = Button(self.add_opt_frame, text="+", font=("Arial", int(16*y_ratio)), 
                                relief="flat", borderwidth=0,
                                command=self.open_add_option, cursor="hand2")
            self.add_opt_pbt.pack(side="top")
            pass

        # 등록/취소 프레임
        self.add_frame = self.setFrame_pack(self.add_opt_frame, 'bottom', 375, 50)
        # 등록/취소 버튼
        self.bt = Button(self.add_frame, text="취소", width=int(10*x_ratio), relief="solid", borderwidth=1, command=self.quit)
        self.bt.pack(side='right')
        self.menu_add_bt = Button(self.add_frame, text="등록", width=int(10*x_ratio), relief="solid", borderwidth=1, command=self.submit)
        self.menu_add_bt.pack(side='right')

        # 메뉴 등록 컨트롤 클래스 인스턴스 생성
        self.adj_control = Menu_adj_control()

    def setFrame_pack(self, frame, pos, wid, hei):             # 프레임 생성 함수
        frame = Frame(frame, width = wid, height=hei, relief="solid", bd = 0.5)    #, background="#C1FFD4"
        frame.pack(side = pos)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        return frame    

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

        # print("test",category, menu_name, price, description)

        # 데이터 유효성 검사 및 변환
        # 가격이 숫자가 아니면 등록 불가
        if price not in ["", "가격"] and not price.isdigit():
            messagebox.showerror("입력 오류", "가격은 숫자만 입력하세요.")
            return

        self.menu_data = {
            'category': category if category != "카테고리 지정" else None,
            'menu': menu_name if menu_name not in ["", "메뉴명"] else None,
            'price': int(price) if price.isdigit() else None,
            'description': description if description not in ["", "메뉴 설명"] else None,
            'image': self.image_path
        }

        # 필수 입력값 체크 (예시: 메뉴명, 가격, 카테고리)
        if self.menu_data['menu'] == None or self.menu_data['price'] == None or self.menu_data['category'] == None: 
            messagebox.showerror("입력 오류", "메뉴명, 가격, 카테고리를 모두 입력하세요.")
            return
        

        result_menu = self.adj_control.menu_adj(self.menu_data, self.menu[1])
        result_opt = self.adj_control.Option_adj(self.menu_data, self.req_opt, self.add_opt)
        res = messagebox.showinfo(f"메뉴 등록 결과 {result_menu}\n옵션 등록 결과{result_opt}")
        # 바뀐 부분 ② : 등록 완료 시 메인 창도 자동 종료
        if self.parent_window is not None:
            self.parent_window.destroy()
        self.menu_add_window.destroy()


    def quit(self):
        self.menu_add_window.destroy()

    def open_req_option(self):
        self.req = self.Option_boundary('필수')
        # print(self.req)



    def open_add_option(self):
        self.add = self.Option_boundary('추가')
        # print(self.add)




    def Option_boundary(self, opt, title="옵션 등록"):
        self.opt_window = Toplevel()
        self.opt_window.title(title)
        self.opt_window.geometry("400x200")
        self.opt_window.resizable(False, False)
        self.opt_window.configure(bg="white")
        self.opt_window.grab_set()  # 팝업이 떠있는 동안 메인 창 조작 방지

        self.option = Entry(self.opt_window, width=20, relief="solid", borderwidth=1)
        self.option.insert(0, "옵션명")
        self.option.pack(pady=(5, 2))

        self.price = Entry(self.opt_window, width=20, relief="solid", borderwidth=1)
        self.price.insert(0, "가격")
        self.price.pack(pady=2)

        btn_frame = Frame(self.opt_window, bg="white")
        btn_frame.pack(pady=5)

        cancel_bt = Button(btn_frame, text="취소", width=7, relief="solid", borderwidth=1, command=self.opt_window.destroy)
        cancel_bt.pack(side="left", padx=5)
        opt_add_bt = Button(btn_frame, text="등록", width=7, relief="solid", borderwidth=1, command=lambda: self.opt_submit(opt))
        opt_add_bt.pack(side="left", padx=5)

    def opt_submit(self, opt):
        # 실제 등록 로직은 여기에 작성
        # 예시: 입력값 가져오기
        name = self.option.get()
        price = self.price.get()
        # 필요시 부모에게 값 전달 가능 가격이 숫자가 아니면 등록 불가
        if price != None and not price.isdigit():
            messagebox.showerror("입력 오류", "가격은 숫자만 입력하세요.")
            return
        
        # 필수 입력값 체크 (예시: 메뉴명, 가격, 카테고리)
        if name == None or price == None : 
            messagebox.showerror("입력 오류", "메뉴명, 가격 모두 입력하세요.")
            return
        
        self.opt_window.destroy()
        
        # 필수 옵션 리스트
        if opt == '필수':
            self.req_opt.append([name, price])
            # print("req_opt: ",self.req_opt)
        
        # 추가 옵션 리스트
        else:
            self.add_opt.append([name, price])
            # print("add_opt: ",self.add_opt)

        # 입력된 데이터 유지
        category = self.category_var.get()
        menu_name = self.menu_text.get()
        price = self.price_txt.get()
        description = self.desc_txt.get()

        
        self.menu_data = {
            'category': category if category != "카테고리 지정" else None,
            'menu': menu_name if menu_name not in ["", "메뉴명"] else None,
            'price': int(price) if price.isdigit() else None,
            'description': description if description not in ["", "메뉴 설명"] else None,
            'image': self.image_path
        }

        self.menu_add_window.destroy()
        self.run()

        return [name, price]

if __name__ == "__main__":
    app = MenuForm()
    app.mainloop()
