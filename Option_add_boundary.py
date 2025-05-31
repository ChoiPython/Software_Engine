import tkinter as tk

class OptionPopup(tk.Toplevel):
    def __init__(self, parent, title="옵션 등록"):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)
        self.configure(bg="white")
        self.grab_set()  # 팝업이 떠있는 동안 메인 창 조작 방지

        self.name_entry = tk.Entry(self, width=20, relief="solid", borderwidth=1)
        self.name_entry.insert(0, "옵션명")
        self.name_entry.pack(pady=(5, 2))

        self.price_entry = tk.Entry(self, width=20, relief="solid", borderwidth=1)
        self.price_entry.insert(0, "가격")
        self.price_entry.pack(pady=2)

        btn_frame = tk.Frame(self, bg="white")
        btn_frame.pack(pady=5)

        cancel_btn = tk.Button(btn_frame, text="취소", width=7, relief="solid", borderwidth=1, command=self.destroy)
        cancel_btn.pack(side="left", padx=5)
        submit_btn = tk.Button(btn_frame, text="등록", width=7, relief="solid", borderwidth=1, command=self.submit)
        submit_btn.pack(side="left", padx=5)

    def submit(self):
        # 실제 등록 로직은 여기에 작성
        # 예시: 입력값 가져오기
        name = self.name_entry.get()
        price = self.price_entry.get()
        # 필요시 부모에게 값 전달 가능
        self.destroy()
