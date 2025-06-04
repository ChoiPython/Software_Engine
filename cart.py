import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QScrollArea, QMessageBox, QSizePolicy
)
from PyQt5.QtCore import Qt


class CartItem(QWidget):
    """장바구니에 들어가는 개별 메뉴 항목 UI"""

    def __init__(self, name, option, price, parent):
        super().__init__()
        self.parent = parent  # CartWindow 인스턴스
        self.price = price
        self.count = 1  # 기본 수량 1

        # 전체 레이아웃
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        # 상단: 이미지 + 메뉴명/옵션 + 삭제 버튼
        top_layout = QHBoxLayout()

        # 메뉴 이미지 자리 (현재는 더미 텍스트)
        image = QLabel('메뉴 사진')
        image.setFixedSize(80, 80)
        image.setStyleSheet("border: 1px solid green;")  # 이미지 박스 표시용 테두리
        image.setAlignment(Qt.AlignCenter)
        top_layout.addWidget(image)

        # 메뉴 이름 및 옵션 정보
        info_layout = QVBoxLayout()
        self.name_label = QLabel(name)
        self.option_label = QLabel(option)
        info_layout.addWidget(self.name_label)
        info_layout.addWidget(self.option_label)
        top_layout.addLayout(info_layout, stretch=2)

        # 항목 삭제 버튼
        delete_btn = QPushButton("삭제")
        delete_btn.clicked.connect(self.delete_item)
        delete_btn.setFixedSize(50, 30)
        top_layout.addWidget(delete_btn)

        layout.addLayout(top_layout)

        # 하단: 수량 조절 및 가격 표시
        bottom_layout = QHBoxLayout()

        # 수량 감소 버튼
        minus_btn = QPushButton("-")
        minus_btn.clicked.connect(self.decrease_count)
        minus_btn.setFixedSize(25, 25)
        bottom_layout.addWidget(minus_btn)

        # 수량 표시 라벨
        self.count_label = QLabel("1")
        self.count_label.setFixedWidth(30)
        self.count_label.setAlignment(Qt.AlignCenter)
        bottom_layout.addWidget(self.count_label)

        # 수량 증가 버튼
        plus_btn = QPushButton("+")
        plus_btn.clicked.connect(self.increase_count)
        plus_btn.setFixedSize(25, 25)
        bottom_layout.addWidget(plus_btn)

        # 항목별 총 가격 표시
        self.item_price_label = QLabel(f"{self.price:,.0f}")
        self.item_price_label.setAlignment(Qt.AlignRight)
        self.item_price_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        bottom_layout.addWidget(self.item_price_label)

        layout.addLayout(bottom_layout)

        # 외곽 테두리 설정
        self.setLayout(layout)
        self.setStyleSheet("border: 1px solid gray;")

    def increase_count(self):
        """수량 증가"""
        self.count += 1
        self.update_price()

    def decrease_count(self):
        """수량 감소 (최소 1까지 허용)"""
        if self.count > 1:
            self.count -= 1
            self.update_price()

    def update_price(self):
        """수량 변경 시 개별 금액 및 전체 금액 갱신"""
        self.count_label.setText(str(self.count))
        self.item_price_label.setText(f"{self.get_total():,}")
        self.parent.update_total()

    def delete_item(self):
        """해당 항목 삭제"""
        self.setParent(None)  # UI에서 제거
        self.parent.remove_item(self)  # 부모에 알림

    def get_total(self):
        """항목 총 가격 반환 (수량 반영)"""
        return self.count * self.price


class CartWindow(QWidget):
    """장바구니 전체 창"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("장바구니")
        self.setGeometry(100, 100, 400, 600)

        self.cart_items = []  # 현재 장바구니 항목 목록

        main_layout = QVBoxLayout()

        # 상단 제목 라벨
        title = QLabel("장바구니")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # 스크롤 가능한 항목 영역
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 항상 스크롤 표시

        # 장바구니 항목들이 들어갈 위젯
        self.items_widget = QWidget()
        self.items_layout = QVBoxLayout()
        self.items_layout.setSpacing(10)
        self.items_layout.addStretch()  # 맨 아래 여유 공간 확보
        self.items_widget.setLayout(self.items_layout)

        scroll_area.setWidget(self.items_widget)
        main_layout.addWidget(scroll_area)

        # 전체 금액 라벨
        self.total_label = QLabel("주문금액  0")
        self.total_label.setAlignment(Qt.AlignCenter)
        self.total_label.setStyleSheet("font-size: 18px; color: red;")
        main_layout.addWidget(self.total_label)

        # 하단 버튼 영역 (닫기 / 주문하기)
        btn_layout = QHBoxLayout()
        close_btn = QPushButton("닫기")
        close_btn.clicked.connect(self.close)

        order_btn = QPushButton("주문하기")
        order_btn.clicked.connect(self.order_items)

        btn_layout.addWidget(close_btn)
        btn_layout.addWidget(order_btn)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

        # 샘플 아이템 추가 (화면 테스트용)
        for i in range(10):
            self.add_item(f"메뉴명 {i+1}", "추가 옵션", 10000)

    def add_item(self, name, option, price):
        """장바구니에 항목 추가"""
        item = CartItem(name, option, price, self)
        self.cart_items.append(item)
        # stretch 바로 앞에 위젯 삽입
        self.items_layout.insertWidget(self.items_layout.count() - 1, item)
        self.update_total()

    def remove_item(self, item):
        """장바구니에서 항목 제거"""
        if item in self.cart_items:
            self.cart_items.remove(item)
            item.deleteLater()
            self.update_total()

    def update_total(self):
        """전체 주문 금액 계산 및 표시"""
        total = sum(item.get_total() for item in self.cart_items)
        self.total_label.setText(
            f"<b>주문금액</b>  <span style='color:red;'>{total:,.0f}</span>"
        )

    def order_items(self):
        """주문 처리"""
        total = sum(item.get_total() for item in self.cart_items)
        QMessageBox.information(self, "주문 완료", f"{total:,.0f}원이 주문되었습니다!")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CartWindow()
    win.show()
    sys.exit(app.exec_())
