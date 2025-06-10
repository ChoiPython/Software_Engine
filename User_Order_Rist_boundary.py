import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def show_order_window_from_cart(menu_list):
    root = tk.Toplevel()
    root.title("주문 내역")
    root.geometry("700x800")

    # ----------------------
    # 테이블 번호 + 주문 내역
    # ----------------------
    top_frame = tk.Frame(root, pady=10)
    top_frame.pack(fill="x")

    tk.Label(top_frame, text="테이블 1", font=("Arial", 20)).pack(side="left", padx=30)
    tk.Label(top_frame, text="주문 내역", font=("Arial", 20)).pack(side="right", padx=30)

    # --------------------------
    # 주문 항목 프레임 + 스크롤
    # --------------------------
    order_frame_container = tk.Frame(root)
    order_frame_container.pack(fill="both", expand=True)

    canvas = tk.Canvas(order_frame_container)
    scrollbar = tk.Scrollbar(order_frame_container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    def sync_scrollable_width(event):
        canvas.itemconfig(window_id, width=event.width)

    canvas.bind("<Configure>", sync_scrollable_width)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # --------------------------
    # 메뉴 항목 생성 함수
    # --------------------------
    def create_menu_item(parent, name, option, qty, price, img_path):
        frame = tk.Frame(parent, relief="solid", bd=1, padx=10, pady=5)
        frame.pack(pady=10, padx=20, fill="x", expand=True)

        try:
            img = Image.open(img_path)
            img = img.resize((100, 100))
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
        tk.Label(info_frame, text=option, font=("Arial", 11)).pack(anchor="w")

        bottom_frame = tk.Frame(frame)
        bottom_frame.pack(fill="x", pady=5)
        tk.Label(bottom_frame, text=qty).pack(side="left")
        tk.Label(bottom_frame, text=price).pack(side="right")

    # --------------------------
    # 총 주문 금액 계산 및 항목 출력
    # --------------------------
    total_price = 0
    for order in menu_list:
        total_price += order['price']
        create_menu_item(
            scrollable_frame,
            name=order['menu_name'],
            option=order['option'],
            qty=f"{order['quantity']}개",
            price=f"{order['price']:,}원",
            img_path=order['image_path']
        )

    # --------------------------
    # 총 주문 금액
    # --------------------------
    total_frame = tk.Frame(root, pady=20)
    total_frame.pack(fill="x")

    tk.Label(total_frame, text="주문금액", font=("Arial", 18)).pack(side="left", padx=20)
    tk.Label(total_frame, text=f"{total_price:,}원", fg="red", font=("Arial", 18, "bold")).pack(side="right", padx=20)

    # --------------------------
    # 버튼 영역
    # --------------------------
    def on_payment():
        messagebox.showinfo("결제 완료", "결제 요청이 완료되었습니다.")
        root.destroy()

    button_frame = tk.Frame(root, pady=20)
    button_frame.pack()

    tk.Button(button_frame, text="결제 요청", width=20, height=2, command=on_payment).pack(side="left", padx=30)
    tk.Button(button_frame, text="닫기", width=20, height=2, command=root.destroy).pack(side="right", padx=30)

    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨기기 (빈 창 안 뜨게 함)

    sample_menu = [
        {
            "menu_name": "돈까스",
            "option": "치즈 추가",
            "quantity": 2,
            "price": 12000,
            "image_path": "test.jpg"
        },
        {
            "menu_name": "우동",
            "option": "계란 추가",
            "quantity": 1,
            "price": 9000,
            "image_path": "test2.jpg"
        }
    ]

    show_order_window_from_cart(sample_menu)

    root.mainloop()