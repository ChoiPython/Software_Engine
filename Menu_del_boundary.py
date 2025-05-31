import tkinter as tk
from tkinter import ttk

# 메뉴 삭제 UI를 위한 클래스 정의
class DeleteMenuUI:
    def __init__(self):
        # 루트 윈도우 생성
        self.root = tk.Tk()
        self.root.title("메뉴 삭제")  # 윈도우 제목 설정
        self.root.geometry("1200x800+300+100")  # 창 크기 및 위치 설정
        self.root.configure(bg="white")  # 배경 색상 설정

        self.build_ui()  # UI 구성 메서드 호출
        self.root.mainloop()  # 이벤트 루프 시작 (UI 실행 유지)

    def build_ui(self):
        # 전체 UI를 담을 바깥쪽 프레임 생성
        self.outer_frame = self.create_frame(self.root, "white", 10, 10)
        self.outer_frame.pack(fill=tk.BOTH, expand=True)

        # 좌측 카테고리 버튼 영역 생성
        self.create_category_buttons(self.outer_frame)

        # 우측 메뉴 리스트 영역 생성 (스크롤 포함)
        self.create_menu_list(self.outer_frame)

    def create_frame(self, parent, bg, padx=0, pady=0):
        # 프레임 생성 헬퍼 함수
        return tk.Frame(parent, bg=bg, padx=padx, pady=pady)

    def create_category_buttons(self, parent):
        # 카테고리 버튼들을 담을 프레임 생성
        self.category_frame = self.create_frame(parent, "white")
        self.category_frame.pack(side=tk.LEFT, anchor="n", padx=(10, 30), pady=10)

        # 5개의 카테고리 버튼 생성
        for i in range(1, 6):
            btn = tk.Button(
                self.category_frame,
                text=f"카테고리{i}",  # 버튼 텍스트
                width=15, height=2,
                bd=1,
                relief="solid",  # 테두리 스타일
                highlightbackground="green",  # 강조 색상 (MacOS에서는 유효)
                highlightthickness=1  # 강조 테두리 두께
            )
            btn.pack(pady=10)  # 버튼 간 수직 간격 설정

    def create_menu_list(self, parent):
        # 메뉴 목록 스크롤 영역 생성
        self.menu_scroll_frame = self.create_frame(parent, "white")
        self.menu_scroll_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # 메뉴 목록을 담을 캔버스와 스크롤바 생성
        self.canvas = tk.Canvas(self.menu_scroll_frame, bg="white", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.menu_scroll_frame, orient="vertical", command=self.canvas.yview)

        # 스크롤 가능한 프레임 생성 (캔버스 내부에 위치)
        self.scrollable_frame = self.create_frame(self.canvas, "white")

        # 스크롤 이벤트 발생 시, 캔버스의 scrollregion을 업데이트
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # 캔버스에 스크롤 가능한 프레임 추가
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # 캔버스와 스크롤바 배치
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # 메뉴 항목 카드들 생성
        self.create_menu_cards()

    def create_menu_cards(self):
        # 2행 4열 형태로 8개의 메뉴 카드 생성
        for row in range(2):
            for col in range(4):
                card = tk.Frame(
                    self.scrollable_frame,
                    bg="white",
                    bd=1,
                    relief="solid",
                    highlightbackground="green",
                    highlightthickness=1,
                    padx=15, pady=15
                )
                card.grid(row=row, column=col, padx=15, pady=20, sticky="n")

                # 메뉴 사진
                photo = tk.Label(
                    card,
                    text="메뉴 사진",
                    width=18, height=6,
                    bg="white",
                    relief="groove",
                    bd=1,
                    highlightbackground="green",
                    highlightthickness=1
                )
                photo.pack()

                # 하단 정보 및 버튼을 감싸는 영역
                bottom_frame = tk.Frame(card, bg="white")
                bottom_frame.pack(fill="x", pady=(10, 0))

                # 메뉴명과 가격 (왼쪽)
                info_frame = tk.Frame(bottom_frame, bg="white")
                info_frame.pack(side="left", anchor="nw")

                name = tk.Label(info_frame, text="메뉴명", bg="white", font=("Arial", 10), anchor="w")
                name.pack(anchor="w")

                price = tk.Label(info_frame, text="가격", bg="white", font=("Arial", 10), anchor="w")
                price.pack(anchor="w", pady=(5, 0))

                # 삭제 버튼 (오른쪽 아래)
                delete_btn = tk.Button(
                    bottom_frame,
                    text="삭제",
                    width=6,
                    bd=1,
                    relief="solid",
                    highlightbackground="green",
                    highlightthickness=1
                )
                delete_btn.pack(side="right", anchor="se", padx=(10, 0), pady=(20, 0))

        # 닫기 버튼 (메뉴 하단에 위치)
        close_btn = tk.Button(
            self.scrollable_frame,
            text="닫기",
            width=20, height=2,
            bd=1,
            relief="solid",
            highlightbackground="green",
            highlightthickness=1
        )
        close_btn.grid(row=3, column=3)


# 프로그램의 시작점
if __name__ == "__main__":
    app = DeleteMenuUI()  # DeleteMenuUI 클래스의 인스턴스를 생성하여 실행
