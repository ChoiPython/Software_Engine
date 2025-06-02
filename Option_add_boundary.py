import tkinter as tk

class OptionPopup(tk.Toplevel):
    def __init__(self, parent, title="옵션 등록"):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)
        self.configure(bg="white")
        self.grab_set()  # 팝업이 떠있는 동안 메인 창 조작 방지

        self.option = tk.Entry(self, width=20, relief="solid", borderwidth=1)
        self.option.insert(0, "옵션명")
        self.option.pack(pady=(5, 2))

        self.price = tk.Entry(self, width=20, relief="solid", borderwidth=1)
        self.price.insert(0, "가격")
        self.price.pack(pady=2)

        btn_frame = tk.Frame(self, bg="white")
        btn_frame.pack(pady=5)

        cancel_bt = tk.Button(btn_frame, text="취소", width=7, relief="solid", borderwidth=1, command=self.destroy)
        cancel_bt.pack(side="left", padx=5)
        opt_add_bt = tk.Button(btn_frame, text="등록", width=7, relief="solid", borderwidth=1, command=self.submit)
        opt_add_bt.pack(side="left", padx=5)

    def submit(self):
        # 실제 등록 로직은 여기에 작성
        # 예시: 입력값 가져오기
        name = self.option.get()
        price = self.price.get()
        # 필요시 부모에게 값 전달 가능
        self.destroy()
