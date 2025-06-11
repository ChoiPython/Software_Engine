from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from getMenu import *
from Choiced_menu_boundary import *
from Cart_boundary import *

class User_main:
    
    def __init__(self):
        self.data = getMenu()
        self.Menu_list = self.data.getMenu()
        self.cart = []

    def run(self):
        self.user_window = Tk()
        self.user_window.title("사용자 메인화면")
        self.user_window.geometry("1200x800+300+100")
        self.user_window.resizable(False, False)
        self.ShowUi()       # 화면 출력
        self.scrollable_frame = self.y_scrollable_frame()        # 스크롤바 생성
        self.ShowWidget()   # 위젯 출력
        self.setMenu()      # 메뉴 출력
        self.user_window.mainloop()


    # 프레임 세팅
    def ShowUi(self):
        self.head_frame = self.setFrame_pack(self.user_window, 'top', 1200, 100)               # 상단 프레임
        self.left_frame = self.setFrame_pack(self.user_window, 'left', 200, 700)               # 좌측 프레임
        self.right_frame = self.setFrame_pack(self.user_window, 'left', 1000, 700)             # 우측 프레임
        self.right_bottom_frame = self.setFrame_pack(self.right_frame, 'bottom', 1000, 100)    # 우측 하단 프레임
        self.right_top_frame = self.setFrame_pack(self.right_frame, 'top',1000, 600)           # 우측 상단 프레임

        self.table_num = self.setlabel(self.head_frame, 'left', '테이블 1', 10, 1, anc = 'w')         # 테이블 번호 라벨

    def setMenu(self, category = '1.메인메뉴'):      # 메뉴 생성 함수 / 카테고리 변수를 받아서 출력
        self.Menu_list = self.data.getMenu()
        menu = sorted(list((info for info in self.Menu_list if info[0] == category)), key = lambda x: x[1]) # 카테고리에 맞는 메뉴들
        
        for i in range(len(menu)):
            row = i // 4    # 4개씩 출력
            col = i % 4 

            if i == 0:  # 메뉴 프레임 초기화
                for widget in self.scrollable_frame.winfo_children():
                    widget.destroy()

            frame = self.setFrame_grid(self.scrollable_frame, 220, 230, row, col)
            self.setlabel(frame, 'top', None, 220, 150, img = menu[i][2])           # 메뉴 이미지 생성
            self.setlabel(frame, 'top', menu[i][1], 10, 1, anc='w', t_font=("맑은고딕", 13))           # 메뉴명 라벨 생성 
            self.setlabel(frame, 'top', menu[i][3],10, 1, anc='w', t_font=("맑은고딕", 13))         # 메뉴 가격 라벨 생성
            self.add_cart_bt = self.setButton(frame, 'right', '담기', 10, 1, x=10, y=5)                # 담기 버튼 생성
            self.add_cart_bt.config(command = lambda m = menu[i] : self.add_cart_event(m))         


    def ShowWidget(self):
        # 카테고리 버튼 배치
        self.cate = sorted(list(set(cate[0] for cate in self.Menu_list)))   # 카테고리 데이터 불러오기 완료 - 순서를 위해 카테고리 데이터에 번호를 붙임

        for i in self.cate:
            self.setCateBtn(self.left_frame, 'top', i, 15, 3, y=20)
            pass

        # 결제요청, 장바구니, 주문목록 버튼 배치
        self.orderlistui_bt = self.setButton(self.right_bottom_frame, 'right', '주문목록', 15, 3, x=10, y=10)
        self.cart_bt =  self.setButton(self.right_bottom_frame, 'right', '장바구니', 15, 3, x=10, y=10)
        self.req_pay_bt = self.setButton(self.right_bottom_frame, 'right', '결제요청', 15, 3, x=10, y=10)

        # 버튼별 함수 지정
        self.orderlistui_bt.config(command=self.orderlistui_event)
        self.cart_bt.config(command=self.cart_event)
        self.req_pay_bt.config(command=self.req_pay_event)

    # 라벨 생성
    def setlabel(self, frame, pos, txt, wid, hei, anc=None, t_font=("맑은고딕", 20), img = None):             # 라벨 생성 함수
        label = Label(frame, text = txt, width=wid, height=hei, font=t_font)    #, relief='solid', bd=1
        if img != None:
            set_img = Image.open(img).resize((220,150))
            img_adr = ImageTk.PhotoImage(set_img)
            label.config(image=img_adr)
            label.image = img_adr

        if anc != None:
            label.config(anchor=anc)
        
        label.pack(side = pos, fill = 'x')

        return label
        
    # pcak로 생성하는 프레임
    def setFrame_pack(self, frame, pos, wid, hei):             # 프레임 생성 함수
        frame = Frame(frame, width = wid, height=hei, relief="solid", bd = 0.5)    #, background="#C1FFD4"
        frame.pack(side = pos)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        return frame    

    # grid로 생성하는 프레임
    def setFrame_grid(self, frame, wid, hei, row, col):
        frame = Frame(frame, width = wid, height = hei, relief="solid", bd = 0.5)   # , background="#C1FFD4"
        frame.grid(row = row, column= col, padx = 10, pady = 10)
        frame.pack_propagate(False)
        return frame

    # 버튼 생성 함수
    def setButton(self, frame, pos, txt, wid, hei, anc=None, x=10, y=3):            # 버튼 생성 함수
        button = Button(frame, text=txt, width=wid, height=hei, relief='solid', bd=0.5)
        if anc != None:
            button.config(anchor=anc)
        button.pack(side=pos, padx = x, pady = y)
        return button
    

    # 카테고리 버튼 생성 함수
    def setCateBtn(self, frame, pos, txt, wid, hei, x=10, y=3):            # 버튼 생성 함수
        cate_bt = Button(frame, text=txt.split('.')[1], width=wid, height=hei, command = lambda b = txt : self.cate_event(b))   # 카테고리별 번호는 텍스트에서 제외
        cate_bt.pack(side=pos, padx = x, pady = y)

        return cate_bt
    
    # 카테고리 버튼 이벤트  카테고리별 이름을 가져와서 메뉴를 출력할 예정
    def cate_event(self, txt):
        self.setMenu(txt)
        pass

    # 담기 버튼 이벤트
    def add_cart_event(self, menu):
        self.cmb = Choiced_menu_boundary(self, menu)


    # 결제 요청 버튼 이벤트
    def req_pay_event(self):
        messagebox.showinfo("결제요청", "결제가 요청되었습니다.")   # 몇초 후 사라지게 구현??
        
        print("결제를 요청하셨습니다.")
        pass
    
    # 장바구니 버튼 이벤트
    def cart_event(self):
        # print("장바구니가 열림")
        # print(self.cart)
        self.cart_ui = Cart()
        self.cart_ui.show_cart(self.cart)
        print(self.cart)

        
        self.cart_ui.grab_set()


    # 주문목록 버튼 이벤트
    def orderlistui_event(self):
        print("주문목록 화면이 열림")
        from User_Order_Rist_boundary import UserOrderRist
        order_window = UserOrderRist(table_number=1)  # 실제 테이블 번호 연동 가능
        order_window.run()  


        


    # 세로 스크롤 가능한 프레임을 설정하는 함수 (GPT & 제미나이 사용)
    def y_scrollable_frame(self):
        # 캔버스와 스크롤바를 담을 컨테이너 프레임을 right_top_frame 내부에 생성합니다.
        # right_top_frame은 pack으로 관리되므로, 이 컨테이너도 pack으로 배치합니다.
        canvas_scrollbar_container = Frame(self.right_top_frame)
        canvas_scrollbar_container.pack(fill="both", expand=True)
        # canvas_scrollbar_container.pack_propagate(False)

        # 캔버스 생성 (부모를 canvas_scrollbar_container로 변경)
        canvas = Canvas(canvas_scrollbar_container, bg="white")

        # 스크롤바 생성 (부모를 canvas_scrollbar_container로 변경)
        scrollbar = Scrollbar(canvas_scrollbar_container, orient="vertical", command=canvas.yview)

        # 캔버스와 스크롤바를 canvas_scrollbar_container 내에서 pack으로 배치합니다.
        # 스크롤바를 먼저 배치하여 오른쪽에 고정하고, 캔버스가 남은 공간을 채우도록 합니다.
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        # 캔버스와 스크롤바 연결
        canvas.configure(yscrollcommand=scrollbar.set)

        # 스크롤 가능한 내부 프레임 (이 프레임은 캔버스에 의해 관리됩니다 - create_window)
        # 이 프레임 내에서는 grid를 자유롭게 사용할 수 있습니다.
        scrollable_frame = Frame(canvas)

        # 캔버스 안에 윈도우(scrollable_frame) 생성
        # window=scrollable_frame: 캔버스에 표시할 위젯
        # anchor='nw': 위젯의 북서쪽(north-west) 모서리가 캔버스 좌표 (0,0)에 고정되도록 합니다.
        canvas_window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')

        # 스크롤 영역 설정 및 프레임 크기 조절 시 캔버스 너비 조정
        def on_frame_configure(event):
            # 스크롤 영역을 scrollable_frame의 전체 크기로 설정합니다.
            canvas.configure(scrollregion=canvas.bbox("all"))
            # 캔버스 너비를 스크롤 가능한 프레임의 너비와 일치시키기
            # 이렇게 하면 스크롤 가능한 프레임이 캔버스 너비에 맞춰지고 가로 스크롤바가 생기지 않습니다.
            canvas.itemconfig(canvas_window_id, width=canvas.winfo_width())

        # scrollable_frame의 크기가 변경될 때마다 on_frame_configure 함수를 호출합니다.
        scrollable_frame.bind("<Configure>", on_frame_configure)
        # 캔버스 크기가 변경될 때도 on_frame_configure를 호출하여 scrollable_frame의 너비를 조정합니다.
        canvas.bind("<Configure>", on_frame_configure)

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

        # 마우스 휠 스크롤 기능 추가 (전역 바인딩)
        canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", on_mousewheel))
        canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

        # setMenu에서 사용할 수 있도록 scrollable_frame을 반환합니다.
        return scrollable_frame


if __name__ == "__main__":
    mainui = User_main()
    mainui.run()
    


