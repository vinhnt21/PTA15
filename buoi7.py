from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from PyQt6 import uic
import sys


DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin"


class Buoi7(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("buoi7.ui", self)

        self.loginBtn.clicked.connect(self.onClickLoginBtn)
        self.loginBtn.clicked.connect(self.nextStep)

    def onClickLoginBtn(self):
        user = self.user_input.text()
        pw = self.pw_input.text()

        if user == DEFAULT_USERNAME and pw == DEFAULT_PASSWORD:
            QMessageBox.information(self, "Thông báo", "Đăng nhập thành công!")
        else:
            QMessageBox.critical(self, "Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

    def nextStep(self):
        QMessageBox.information(self, "Hehe", ":v 😭😭😭😭")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Buoi7()
    window.show()
    sys.exit(app.exec())
