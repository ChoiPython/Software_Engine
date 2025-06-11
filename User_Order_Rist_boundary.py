# User_Order_Rist_boundary.py

import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

class UserOrderRist:

    def __init__(self, table_number=1):
        self.table_number = table_number
        self.total_price = 0

    def fetch_orders_by_table(self):
        conn = mysql.connector.connect(
            host='localhost',
            user='soft',
            password='0000',
            database='table_order',
            charset='utf8'
        )
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM order_list WHERE table_num = %s"
        cursor.execute(query, (self.table_number,))
        results = cursor.fetchall()

        conn.close()
        return results

    def show_payment_popup(self):
        messagebox.showinfo("결제 완료", "결제 요청이 완료되었습니다.")
        self.root.destroy()

    def create_menu_item(self, parent, name, option, qty, price, img_path):
        frame = tk.Frame(parent, relief="solid", bd=1, padx=10, pady=5)
        frame.pack(pady=10, padx=20, fill="x", expand=True)

        try:
            img = Image.open(img_path).resize((100, 100))
            photo = ImageTk.PhotoImage(img)
        except:
            photo = None

        photo_frame = tk.Frame(frame, width=100, height=100, bg="lightgray")
        photo_frame.pack(side="left")
        photo_frame.pack_propagate(False)

        if photo:
            label_img = tk.Label(photo_frame, image=photo)
            label_img.image = photo
            label_img.pack()
        else:
            tk.Label(photo_frame, text="이미지 없음").pack()

        info_frame = tk.Frame(frame)
        info_frame.pack(side="left", padx=15, fill="x", expand=True)

        tk.Label(info_frame, text=name, font=("Arial", 14, "bold")).pack(anchor="w")
        option_list = option.split('+') if isinstance(option, str) else [str(option)]
        for opt in option_list:
            tk.Label(info_frame, text=f"- {opt}", font=("Arial", 11)).pack(anchor="w")

        bottom_frame = tk.Frame(frame)
        bottom_frame.pack(fill="x", pady=5)
        tk.Label(bottom_frame, text=qty).pack(side="left")
        tk.Label(bottom_frame, text=price).pack(side="right")

    def run(self):
        self.root = tk.Toplevel()
        self.root.title("주문 내역")
        self.root.geometry("700x800")

        # 상단
        top_frame = tk.Frame(self.root, pady=10)
        top_frame.pack(fill="x")
        tk.Label(top_frame, text=f"테이블 {self.table_number}", font=("Arial", 20)).pack(side="left", padx=30)
        tk.Label(top_frame, text="주문 내역", font=("Arial", 20)).pack(side="right", padx=30)

        # 스크롤 프레임
        order_frame_container = tk.Frame(self.root)
        order_frame_container.pack(fill="both", expand=True)

        canvas = tk.Canvas(order_frame_container)
        scrollbar = tk.Scrollbar(order_frame_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.bind("<Configure>", lambda e: canvas.itemconfig(window_id, width=e.width))

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # 주문 불러오기
        orders = self.fetch_orders_by_table()
        print(orders)
        for order in orders:
            self.total_price += order['price']
            self.create_menu_item(
                scrollable_frame,
                name=order['menu_name'],
                option=order['opt'],
                qty=f"{order['quantity']}개",
                price=f"{order['price']:,}원",
                img_path=order['image']
            )

        # 총액
        total_frame = tk.Frame(self.root, pady=20)
        total_frame.pack(fill="x")
        tk.Label(total_frame, text="주문금액", font=("Arial", 18)).pack(side="left", padx=20)
        tk.Label(total_frame, text=f"{self.total_price:,}원", fg="red", font=("Arial", 18, "bold")).pack(side="right", padx=20)

        # 버튼
        button_frame = tk.Frame(self.root, pady=20)
        button_frame.pack()
        tk.Button(button_frame, text="결제 요청", width=20, height=2, command=self.show_payment_popup).pack(side="left", padx=30)
        tk.Button(button_frame, text="닫기", width=20, height=2, command=self.root.destroy).pack(side="right", padx=30)

        # 마우스 휠
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.root.mainloop()