from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

class User_Order_rist_Item(QWidget):
    def __init__(self, image_path, menu, option, ammount, menu_price):
        super().__init__()
        layout = QHBoxLayout()
        layout.setSpacing(15)

        # 메뉴 이미지
        image = QLabel()
        image.setFixedSize(80, 80)
        image.setAlignment(Qt.AlignCenter)
        image.setStyleSheet("""
            QLabel {
                border: 1px solid green;
                padding: 0px;
                margin: 0px;
            }
        """)

        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            # ✅ 박스를 꽉 채우도록 비율 무시하고 맞춤
            scaled_pixmap = pixmap.scaled(
                image.size(),
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )
            image.setPixmap(scaled_pixmap)
        else:
            image.setText("이미지 없음")

        layout.addWidget(image)
        
        # 메뉴 정보
        info_layout = QVBoxLayout()
        menu_label = QLabel(f"<b>{menu}</b>")
        option_label = QLabel(option)
        ammount_label = QLabel(f"{ammount}개")
        info_layout.addWidget(menu_label)
        info_layout.addWidget(option_label)
        info_layout.addWidget(ammount_label)
        layout.addLayout(info_layout)

        # 가격 정보
        menu_price_label = QLabel(f"{menu_price:,.0f}원")
        menu_price_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        layout.addWidget(menu_price_label)

        self.setLayout(layout)

class User_Order_rist(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("주문 내역")
        self.setMinimumSize(400, 600)

        self.total_pricea = 0

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        # 스크롤 영역
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QWidget()
        self.vbox = QVBoxLayout(self.container)
        self.vbox.setSpacing(10)
        self.vbox.setContentsMargins(10, 10, 10, 10)
        self.scroll.setWidget(self.container)
        main_layout.addWidget(self.scroll)

        # 총 금액
        self.total_price_label = QLabel("주문금액 <span style='color:red; font-size:18px;'>00,000</span>")
        self.total_price_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        self.total_price_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.total_price_label)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background-color: #0a88ff;")
        line.setFixedHeight(2)
        main_layout.addWidget(line)

        # 버튼들
        btn_layout = QHBoxLayout()
        self.call_staff_bt = QPushButton("결제 요청")
        self.call_staff_bt.clicked.connect(self.call_staff_event)
        self.close_bt = QPushButton("닫기")
        self.close_bt.clicked.connect(self.close_event)

        btn_layout.addWidget(self.call_staff_bt)
        btn_layout.addWidget(self.close_bt)
        main_layout.addLayout(btn_layout)

        self.Show_Order_rist()

    def Show_Order_rist(self):
        # 샘플 더미 데이터
        order_items = [
            ("C:/Users/User/Downloads/food.png", "메뉴명 1", "선택한 추가 옵션", 1, 5000),
            ("img/sample2.png", "메뉴명 2", "선택한 추가 옵션", 2, 8000),
        ]

        for image, menu, option, ammount, price in order_items:
            self.add_order_item(image, menu, option, ammount, price)

    def add_order_item(self, image, menu, option, ammount, price):
        item = User_Order_rist_Item(image, menu, option, ammount, price)
        self.vbox.addWidget(item)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("background-color: #cccccc;")
        separator.setFixedHeight(1)
        self.vbox.addWidget(separator)

        self.total_pricea += price * ammount
        self.update_total_price()

    def update_total_price(self):
        self.total_price_label.setText(f"주문금액 <span style='color:red; font-size:18px;'>{self.total_pricea:,.0f}</span>")

    def call_staff_event(self):
        print("[이벤트] 결제 요청 (call_staff_event)")

    def close_event(self):
        print("[이벤트] 닫기 (close_event)")
        self.close()

    def close0(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = User_Order_rist()
    window.show()
    sys.exit(app.exec_())
