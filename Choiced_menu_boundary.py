from tkinter import *
from PIL import Image, ImageTk

class Choiced_menu:

    def __init__(self):
        # 메인 윈도우 생성
        self.Choiced_menu_window = Tk()
        self.Choiced_menu_window.title("메뉴 선택 화면")
        self.Choiced_menu_window.geometry("600x800+300+100")
        self.Choiced_menu_window.resizable(True, True)

        # 메뉴 데이터 (기본 가격, 필수 옵션, 추가 옵션, 이미지 등)
        self.menu_data = {
            "base_price": 5000,
            "menu_name": "메뉴 A",
            "image_path": "test.jpg",   # 이미지 경로
            "required_options": [
                {"name": "필수 옵션 A", "price": 0},
                {"name": "필수 옵션 B", "price": 1000},
                {"name": "필수 옵션 C", "price": 1500},
                {"name": "필수 옵션 D", "price": 2000},
            ],
            "additional_options": [
                {"name": "추가 옵션 A", "price": 500},
                {"name": "추가 옵션 B", "price": 700},
                {"name": "추가 옵션 C", "price": 300},
                {"name": "추가 옵션 D", "price": 600},
                {"name": "추가 옵션 E", "price": 400},
                {"name": "추가 옵션 F", "price": 800},
            ]
        }

        # 상태 변수 초기화
        self.selected_required_option_name = None
        self.required_option_buttons = {}    # 필수 옵션 버튼 저장

        self.selected_additional_options = set()  # 추가 옵션 이름 set
        self.additional_option_buttons = {}   # 추가 옵션 버튼 저장

        self.quantity = 1    # 초기 수량

        # UI 표시
        self.ShowUi()

        # 메인 이벤트 루프
        self.Choiced_menu_window.mainloop()

    def ShowUi(self):
        # 전체 레이아웃 구성
        self.left_frame = self.setFrame_pack(self.Choiced_menu_window, 'left', 200, 800)  # 좌측 프레임 (사진, 메뉴명, 수량, 총금액)
        self.right_frame = self.setFrame_pack(self.Choiced_menu_window, 'left', 400, 800)  # 우측 프레임 (옵션 선택)

        self.right_top_frame = self.setFrame_pack(self.right_frame, 'top', 400, 700)      # 옵션 선택 영역
        self.right_bottom_frame = self.setFrame_pack(self.right_frame, 'bottom', 400, 100) # 버튼 영역 (닫기, 장바구니)

        # 각 영역에 UI 요소 표시
        self.showLeftUi()
        self.showOptions()
        self.showBottomButtons()

    def showLeftUi(self):
        # 메뉴 사진 표시
        try:
            image_path = self.menu_data.get("image_path", "")
            img = Image.open(image_path)
            img = img.resize((180, 180), Image.LANCZOS)

            self.menu_photo = ImageTk.PhotoImage(img)  # 이미지 메모리 유지
            Label(self.left_frame, image=self.menu_photo).pack(pady=10)
        except Exception as e:
            # 이미지 로드 실패 시 텍스트 표시
            Label(self.left_frame, text="(이미지 없음)", width=20, height=10, relief="solid").pack(pady=10)

        # 메뉴명 표시
        menu_name = self.menu_data.get("menu_name", "메뉴명")
        Label(self.left_frame, text=menu_name, font=("Arial", 12, "bold")).pack(pady=5)

        # 수량 조절 버튼 +, -
        qty_frame = Frame(self.left_frame)
        qty_frame.pack(pady=10)

        Button(qty_frame, text="-", width=3, command=self.decrease_quantity).pack(side="left")
        self.qty_label = Label(qty_frame, text=str(self.quantity), width=5)
        self.qty_label.pack(side="left")
        Button(qty_frame, text="+", width=3, command=self.increase_quantity).pack(side="left")

        # 합계 금액 표시
        self.total_label = Label(self.left_frame, text="합계금액 0 원", fg="red", font=("Arial", 12))
        self.total_label.pack(pady=10)

    def setFrame_pack(self, frame, pos, wid, hei):
        # Frame 생성 후 고정 크기로 배치
        frame = Frame(frame, width=wid, height=hei, relief="solid", bd=0.5)
        frame.pack(side=pos)
        frame.pack_propagate(False)
        frame.grid_propagate(False)
        return frame

    def showOptions(self):
        # 필수 옵션 영역
        Label(self.right_top_frame, text="* 필수 옵션", fg="red").pack(anchor="w", pady=(5,0))

        required_frame = Frame(self.right_top_frame)
        required_frame.pack(pady=5)

        req_left_frame = Frame(required_frame)
        req_left_frame.pack(side="left", padx=10)

        req_right_frame = Frame(required_frame)
        req_right_frame.pack(side="left", padx=10)

        # 필수 옵션 버튼 배치
        half = (len(self.menu_data["required_options"]) + 1) // 2
        for idx, option in enumerate(self.menu_data["required_options"]):
            target_frame = req_left_frame if idx < half else req_right_frame
            btn = Button(
                target_frame,
                text=f"{option['name']} {option['price']}원",
                width=18,
                relief="raised",
                command=lambda name=option['name'], price=option['price']: self.select_required_option(name, price)
            )
            btn.pack(anchor="w", pady=2)
            self.required_option_buttons[option['name']] = (btn, option['price'])

        # 추가 옵션 영역
        Label(self.right_top_frame, text="  추가 옵션").pack(anchor="w", pady=(10,0))

        additional_frame = Frame(self.right_top_frame)
        additional_frame.pack(pady=5)

        add_left_frame = Frame(additional_frame)
        add_left_frame.pack(side="left", padx=10)

        add_right_frame = Frame(additional_frame)
        add_right_frame.pack(side="left", padx=10)

        # 추가 옵션 버튼 배치
        half = (len(self.menu_data["additional_options"]) + 1) // 2
        for idx, option in enumerate(self.menu_data["additional_options"]):
            target_frame = add_left_frame if idx < half else add_right_frame
            btn = Button(
                target_frame,
                text=f"{option['name']} {option['price']}원",
                width=18,
                relief="raised",
                command=lambda name=option['name'], price=option['price']: self.toggle_additional_option(name, price)
            )
            btn.pack(anchor="w", pady=2)
            self.additional_option_buttons[option['name']] = (btn, option['price'])

    def showBottomButtons(self):
        # 하단 버튼: 닫기, 장바구니 담기
        Button(self.right_bottom_frame, text="닫기", width=15, command=self.close_window).pack(side="left", padx=20, pady=20)
        Button(self.right_bottom_frame, text="장바구니 담기", width=15, command=self.add_to_cart).pack(side="left", padx=20, pady=20)

    def select_required_option(self, name, price):
        # 필수 옵션 선택 처리
        if self.selected_required_option_name == name:
            return  # 이미 선택된 경우 무시

        # 이전 선택 해제
        if self.selected_required_option_name:
            prev_btn, _ = self.required_option_buttons[self.selected_required_option_name]
            prev_btn.config(relief="raised", bg="SystemButtonFace")

        # 현재 선택 표시
        self.selected_required_option_name = name
        selected_btn, _ = self.required_option_buttons[name]
        selected_btn.config(relief="sunken", bg="#FFA07A")

        self.update_total()

    def toggle_additional_option(self, name, price):
        # 추가 옵션 토글 처리
        btn, _ = self.additional_option_buttons[name]

        if name in self.selected_additional_options:
            # 선택 해제
            self.selected_additional_options.remove(name)
            btn.config(relief="raised", bg="SystemButtonFace")
        else:
            # 선택 추가
            self.selected_additional_options.add(name)
            btn.config(relief="sunken", bg="#90EE90")

        self.update_total()

    def update_total(self):
        # 총금액 계산
        base_price = self.menu_data["base_price"]

        # 필수 옵션 금액
        required_price = 0
        if self.selected_required_option_name:
            _, required_price = self.required_option_buttons[self.selected_required_option_name]

        # 추가 옵션 금액 합산
        additional_price = sum(
            self.additional_option_buttons[name][1]
            for name in self.selected_additional_options
        )

        # 최종 합계 금액 표시
        total = (base_price + required_price + additional_price) * self.quantity
        self.total_label.config(text=f"합계금액 {total:,} 원")

    def increase_quantity(self):
        # 수량 증가
        self.quantity += 1
        self.qty_label.config(text=str(self.quantity))
        self.update_total()

    def decrease_quantity(self):
        # 수량 감소 (최소 1)
        if self.quantity > 1:
            self.quantity -= 1
            self.qty_label.config(text=str(self.quantity))
            self.update_total()

    def close_window(self):
        self.Choiced_menu_window.destroy()

    def add_to_cart(self):
        print("장바구니 담기 실행")

# 프로그램 시작
if __name__ == "__main__":
    mainui = Choiced_menu()
