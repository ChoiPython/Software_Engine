import tkinter as tk
from tkinter import ttk

# 루트 창
root = tk.Tk()
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

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# --------------------------
# 메뉴 항목 생성 함수
# --------------------------
def create_menu_item(parent, qty="1개", price="00,000"):
    frame = tk.Frame(parent, relief="solid", bd=1, padx=10, pady=5)
    frame.pack(pady=10, padx=20, fill="x")

    # 메뉴 사진 영역 (왼쪽)
    photo_frame = tk.Frame(frame, width=100, height=100, bg="lightgray")
    photo_frame.pack(side="left")
    photo_frame.pack_propagate(False)
    tk.Label(photo_frame, text="메뉴\n사진", font=("Arial", 10)).pack()

    # 메뉴 설명 영역 (오른쪽)
    info_frame = tk.Frame(frame)
    info_frame.pack(side="left", padx=15, fill="x", expand=True)

    tk.Label(info_frame, text="메뉴명", font=("Arial", 14, "bold")).pack(anchor="w")
    tk.Label(info_frame, text="선택한 추가 옵션", font=("Arial", 11)).pack(anchor="w")

    # 수량과 가격
    bottom_frame = tk.Frame(frame)
    bottom_frame.pack(fill="x", pady=5)
    tk.Label(bottom_frame, text=qty).pack(side="left")
    tk.Label(bottom_frame, text=price).pack(side="right")

# 예시로 메뉴 8개 생성
for i in range(8):
    create_menu_item(scrollable_frame, f"{i+1}개", "00,000")

# --------------------------
# 총 주문 금액
# --------------------------
total_frame = tk.Frame(root, pady=20)
total_frame.pack(fill="x")

tk.Label(total_frame, text="주문금액", font=("Arial", 18)).pack(side="left", padx=20)
tk.Label(total_frame, text="00,000", fg="red", font=("Arial", 18, "bold")).pack(side="right", padx=20)

# --------------------------
# 버튼 영역
# --------------------------
button_frame = tk.Frame(root, pady=20)
button_frame.pack()

tk.Button(button_frame, text="결제 요청", width=20, height=2).pack(side="left", padx=30)
tk.Button(button_frame, text="닫기", width=20, height=2).pack(side="right", padx=30)

# 실행
root.mainloop()
