import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # 이미지 처리를 위해 PIL 사용dyddsdsds
from User_main_boundary import *
from Order_control import OrderControl

class CartItem(tk.Frame):
    """장바구니에 들어가는 개별 메뉴 항목 UI"""

    def __init__(self, cart, master, name, req_option, add_option, quantity, price, parent_window, image_path=None):
        super().__init__(master, bd=1, relief="solid", padx=5, pady=5)
        self.parent_window = parent_window  # 상위 CartWindow 참조
        self.price = price                  # 항목 가격
        self.count = quantity                      # 초기 수량
        self.image_path = image_path        # 이미지 파일 경로


        # --- 상단 영역: 이미지, 메뉴명/옵션, 삭제 버튼 ---
        top_frame = tk.Frame(self)
        top_frame.pack(fill="x", expand=True, pady=4)

        # 이미지 표시 또는 기본 텍스트로 대체
        if self.image_path:
            try:
                img = Image.open(self.image_path)
                img = img.resize((130, 130))  # 적당한 크기로 조절
                self.img_tk = ImageTk.PhotoImage(img)
                image_label = tk.Label(top_frame, image=self.img_tk)
            except Exception as e:
                image_label = tk.Label(top_frame, text="이미지 오류", bg="lightgray", width=15, height=10, relief="solid")
        else:
            image_label = tk.Label(top_frame, text="메뉴 사진", bg="lightgray", width=15, height=10, relief="solid")
        image_label.pack(side="left", padx=5)

        # 메뉴 이름과 옵션 표시
        # self.formatted_opt = req_option + "\n"
        # for i in range(0, len(add_option), 2):
        #     pair = add_option[i:i+2]
        #     line = "\t".join(pair)  # 옵션들 사이 공백
        #     self.formatted_opt += line + "\n"
        #     # print(f"{self.formatted_opt}")
        # self.formatted_opt = self.formatted_opt.strip()
        # info_frame = tk.Frame(top_frame)
        # info_frame.pack(side="left", fill="x", expand=True, padx=10)
        # tk.Label(info_frame, text=name, font=("Arial", 16, "bold"), pady=5).pack(anchor="w")
        if req_option == None :
            self.formatted_opt=""
            for i in range(0, len(add_option), 2):
                pair = add_option[i:i+2]
                line = "\t".join(pair)  # 옵션들 사이 공백
                self.formatted_opt += line + "\n"
                # print(f"{self.formatted_opt}")
            self.formatted_opt = self.formatted_opt.strip()
        else:
            self.formatted_opt = req_option + "\n"
            for i in range(0, len(add_option), 2):
                pair = add_option[i:i+2]
                line = "\t".join(pair)  # 옵션들 사이 공백
                self.formatted_opt += line + "\n"
                # print(f"{self.formatted_opt}")
            self.formatted_opt = self.formatted_opt.strip()
        info_frame = tk.Frame(top_frame)
        info_frame.pack(side="left", fill="x", expand=True, padx=10)
        tk.Label(info_frame, text=name, font=("Arial", 20, "bold"), pady=5).pack(anchor="w")
        tk.Label(info_frame, text=self.formatted_opt, font=("Arial", 13), fg="#555555", pady=2, justify="left", anchor='w').pack(anchor="c")

        # 삭제 버튼
        delete_btn = tk.Button(
            top_frame, 
            text="삭제", 
            command=self.delete_item, 
            height=4, 
            width=15, 
        )
        delete_btn.pack(side="right", padx=5)

        # --- 하단 영역: 수량 조절 버튼과 가격 표시 ---
        bottom_frame = tk.Frame(self)
        bottom_frame.pack(fill="x", expand=True, pady=2)

        # 수량 조절 버튼 및 라벨
        tk.Button(bottom_frame, text="-", command=self.decrease_event, width=5, bg="#eeeeee").pack(side="left", padx=2)
        self.count_label = tk.Label(bottom_frame, text=str(self.count), width=5, font=("Arial", 12))
        self.count_label.pack(side="left", padx=2)
        tk.Button(bottom_frame, text="+", command=self.increase_event, width=5, bg="#eeeeee").pack(side="left", padx=2)

        # 현재 총 금액 표시
        self.item_price_label = tk.Label(
            bottom_frame,
            text=f"{self.price:,.0f}",
            anchor="e",              # 오른쪽 정렬
            justify="right",         # 텍스트 오른쪽 정렬
            font=("Arial", 14, "bold"),  # 글자 크기 키움
            width=10                 # Label 자체 고정 너비 (숫자 칸 확보)
        )       
        self.item_price_label.pack(side="right", padx=10)

        self.user_cart = cart
        # print("test:", self.user_cart)


    def get_total(self):
        """현재 수량 기준 항목 총 가격 반환"""
        return self.price * self.count

    def update_price(self):
        """가격 및 수량 라벨 갱신 + 상위 창 총액 갱신"""
        self.count_label.config(text=str(self.count))
        self.item_price_label.config(text=f"{self.get_total():,}")
        # self.item_price_label.config(text=f"{self.get_total():,}")
        self.parent_window.update_total()

    def increase_event(self):
        """수량 1 증가"""
        self.count += 1
        self.user_cart[4] += 1
        # self.user_cart[5] = self.get_total()
        # print(self.user_cart[5])
        self.update_price()

    def decrease_event(self):
        """수량 1 감소 (최소 1)"""
        if self.count > 1:
            self.count -= 1
            self.user_cart[4] -= 1
            # self.user_cart[5] = self.get_total()
            # print(self.user_cart[5])
            self.update_price()

    def delete_item(self):
        """자기 프레임 제거 및 장바구니에서 삭제"""
        self.destroy()
        self.parent_window.remove_item(self, self.user_cart)


class Cart(tk.Toplevel):
    """장바구니 메인 창 UI"""

    def __init__(self):
        super().__init__()
        # self.show_cart()

    def show_cart(self, cart):
        self.cart = cart

        self.title("장바구니")
        self.geometry("600x800+300+100")  # 창 크기 및 위치
        self.original_cart_data = self.cart
        self.cart_items = []  # 장바구니 항목 목록

        # --- 상단 타이틀 영역 ---
        self.head_frame = tk.Frame(self, height=100)
        self.head_frame.pack(fill="x")
        tk.Label(self.head_frame, text="장바구니", font=("Arial", 20, "bold")).pack(pady=20)

        # --- 스크롤 가능한 항목 리스트 영역 ---
        # --- 스크롤 가능한 항목 리스트 영역 ---
        self.body_frame = tk.Frame(self)
        self.body_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.body_frame)
        scrollbar = tk.Scrollbar(self.body_frame, orient="vertical", command=self.canvas.yview)

        # items_frame의 width를 body_frame에 맞추기 위해 Frame의 width 설정 필요
        self.items_frame = tk.Frame(self.canvas)

        # Canvas에 items_frame 넣기
        self.canvas_window = self.canvas.create_window((0, 0), window=self.items_frame, anchor="nw")

        # 스크롤 영역 업데이트
        self.items_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


        # 마우스 휠 스크롤링 지원
        self.canvas.bind("<Enter>", self._bind_mousewheel)
        self.canvas.bind("<Leave>", self._unbind_mousewheel)
        self.protocol("WM_DELETE_WINDOW", self.close_event)

        # --- 하단: 총금액 + 버튼 영역 ---
        self.bottom_frame = tk.Frame(self, height=100)
        self.bottom_frame.pack(fill="x", pady=10)

        total_frame = tk.Frame(self.bottom_frame)
        total_frame.pack(fill="x", pady=(0, 10))

        self.total_text_label = tk.Label(total_frame, text="주문금액", font=("Arial", 16, "bold"))
        self.total_text_label.pack(side="left", padx=10)

        self.total_label = tk.Label(total_frame, text="00,000", font=("Arial", 16, "bold"), fg="red")
        self.total_label.pack(side="left", padx=10)

        button_frame = tk.Frame(self.bottom_frame)
        button_frame.pack(fill="x")

        # 버튼을 Frame 안에 넣어서 따로 center 정렬
        inner_button_frame = tk.Frame(button_frame)
        inner_button_frame.pack(pady=5)  # 위아래 여백 약간

        tk.Button(inner_button_frame, text="닫기", height=4, width=20, command=self.destroy).pack(side="right", padx=10)
        tk.Button(inner_button_frame, text="주문하기", height=4, width=20, command=self.order_event).pack(side="left", padx=10)
        idx = 0
        for i in self.original_cart_data:
            # menu: 메뉴 이름
            # menu_img: 메뉴 이미지
            # self.selected_required_option_name 선택한 필수 옵션
            # self.select_add_opt: 선택한 추가 옵션 리스트
            # self.quantity: 총 수량
            # self.total: 총 가격
            # print(f"print-i:{i}")
            self.add_item(self.cart[idx], i[0], i[2], i[3], i[4], i[5], i[1])
            idx += 1


    def _on_frame_configure(self, event):
        """items_frame 변경 시 scrollregion 갱신"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        """Canvas 크기 변경 시 items_frame 너비도 변경"""
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)    

    def _bind_mousewheel(self, event):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mousewheel(self, event):
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def add_item(self, cart, name, req_option, add_option, quantity, price, image_path=None):
        """장바구니 항목 추가"""
        item = CartItem(cart, self.items_frame, name, req_option, add_option, quantity, price, self, image_path)
        self.cart_items.append(item)
        item.pack(fill="x", pady=5, padx=10)
        self.update_total()

    def remove_item(self, item, del_cart):
        """항목 삭제 후 총합 갱신"""
        if item in self.cart_items:
            self.cart_items.remove(item)
            self.original_cart_data.remove(del_cart)
            # self.original_cart_data.remove(item)
            self.update_total()

    def update_total(self):
        """장바구니 총 주문 금액 계산"""
        total = sum(item.get_total() for item in self.cart_items)
        self.total_label.config(text=f"{total:,.0f}")

    # 주문하기 버튼 이벤트
    def order_event(self):
    # 장바구니에서 데이터 수집
        cart_data = []

        for item in self.original_cart_data:
            cart_data.append({
                'menu_name': item[0],
                'option': [item[2]] + item[3],  # 필수 + 추가 옵션
                'quantity': item[4],
                'price': item[5],
                'image_path': item[1]
            })

    # ✅ DB에 저장
        order_control = OrderControl()
        table_number = 1  # 하드코딩 or 실제 table_num 받을 수 있게 수정 가능
        order_id = order_control.save_order(table_number, cart_data)

        total = sum(item.get_total() for item in self.cart_items)
        messagebox.showinfo("주문 완료", f"주문번호 {order_id}\n{total:,.0f}원이 주문되었습니다!")
        self.destroy()
    
    def close_event(self):
        self.canvas.unbind_all("<MouseWheel>")
        self.destroy()

        """주문 완료 메시지 및 창 종료"""
        total = sum(item.get_total() for item in self.cart_items)
        if len(self.original_cart_data) == 0:
            messagebox.showinfo("주문실패", "장바구니가 비어 있습니다!")
            # self.destroy()
        else:
            messagebox.showinfo("주문 완료", "주문이 완료되었습니다!") # {total:,.0f}
            self.destroy()

    def close_event(self):
        self.canvas.unbind_all("<MouseWheel>")
        self.destroy()
        
