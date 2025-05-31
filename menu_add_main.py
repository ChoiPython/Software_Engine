from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from menu_register_ui import Ui_Form  
from option_ui import Option_Ui_Form
from adt_option_ui import ADT_Option_Ui_Form

class OptionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Option_Ui_Form()
        self.ui.setupUi(self)

class AdtOptionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ADT_Option_Ui_Form()
        self.ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 버튼 클릭 시 함수 연결
        self.ui.pushButton_2.clicked.connect(self.show_option_window)
        self.ui.pushButton_3.clicked.connect(self.show_adt_option_window)

        # 서브 창 인스턴스는 속성으로 보관
        self.option_window = None
        self.adt_option_window = None

    def show_option_window(self):
        if self.option_window is None:
            self.option_window = OptionWindow()
        self.option_window.show()

    def show_adt_option_window(self):
        if self.adt_option_window is None:
            self.adt_option_window = AdtOptionWindow()
        self.adt_option_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())