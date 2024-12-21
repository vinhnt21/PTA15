from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)


class DangKi(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("dangki.ui", self)

        self.registerButton.clicked.connect(self.register)
        self.showUserListButton.clicked.connect(self.show_user_list)

    def register(self):
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        confirm_password = self.confirm_passwordInput.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")
            return
        if not password == confirm_password:
            QMessageBox.warning(self, "Lỗi", "Mật khẩu không khớp")
            return
        user = User(username, password)
        user_manager.add_user(user)
        QMessageBox.information(self, "Thông báo", "Đăng kí thành công")
        dangki.close()
        dangnhap.show()

    def show_user_list(self):
        str = ""
        for user in user_manager.users:
            str += f"Username: {user.username}\n"
        QMessageBox.information(self, "Danh sách người dùng", str)


class DangNhap(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("dangnhap.ui", self)


if __name__ == "__main__":
    user_manager = UserManager()
    app = QApplication(sys.argv)
    dangki = DangKi()
    dangnhap = DangNhap()
    dangki.show()

    sys.exit(app.exec())
