from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import pymysql
from Menu_adj_control import Menu_adj_control

class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="", color='grey', **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class Menu_adj:
    def __init__(self, menu_list, bf_menu, parent_window=None):
        self.parent_window = parent_window
        self.menu_list = menu_list
        self.bf_menu = bf_menu
        self.control = Menu_adj_control()
        self.new_menu = {}
        self.req_opt = []
        self.add_opt = []
        
        self.window = Toplevel(parent_window)
        self.window.title("메뉴 수정/등록")
        self.window.geometry("800x600+100+100")
        self.window.resizable(False, False)
        self.setWidget()
        
    def setWidget(self):
        # 상단 프레임
        self.top_frame = Frame(self.window)
        self.top_frame.pack(fill=X, padx=10, pady=10)
        
        # 카테고리 선택
        self.category_var = StringVar()
        self.category_var.set("카테고리 선택")
        categories = list(set([menu[0] for menu in self.menu_list]))
        
        self.category_menu = OptionMenu(self.top_frame, self.category_var, *categories)
        self.category_menu.pack(side=LEFT, padx=5)
        
        # 메뉴명 입력
        self.menu_entry = PlaceholderEntry(self.top_frame, placeholder="메뉴명", width=20)
        self.menu_entry.pack(side=LEFT, padx=5)
        
        # 가격 입력
        self.price_entry = PlaceholderEntry(self.top_frame, placeholder="가격", width=15)
        self.price_entry.pack(side=LEFT, padx=5)
        
        # 설명 입력
        self.desc_entry = PlaceholderEntry(self.top_frame, placeholder="설명", width=30)
        self.desc_entry.pack(side=LEFT, padx=5)
        
        # 중앙 프레임
        self.mid_frame = Frame(self.window)
        self.mid_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # 이미
