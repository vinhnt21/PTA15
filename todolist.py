from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt6.QtCore import Qt
import sys

# Tài khoản mặc định
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin"


class LoginPage(QWidget):
    def __init__(self, switch_to_main):
        super().__init__()
        self.switch_to_main = switch_to_main
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Tiêu đề
        title = QLabel("Quản lý thú cưng")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #0078D7;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Form đăng nhập
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Tên đăng nhập")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mật khẩu")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_button = QPushButton("Đăng nhập")
        login_button.setStyleSheet(
            "background-color: #0078D7; color: white; font-weight: bold;"
        )
        login_button.clicked.connect(self.check_login)

        # Sắp xếp các widget
        layout.addWidget(title)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            self.switch_to_main()
        else:
            QMessageBox.warning(
                self, "Sai thông tin", "Tên đăng nhập hoặc mật khẩu không đúng."
            )


class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Tiêu đề
        title = QLabel("Quản lý thú cưng")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #0078D7;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bảng quản lý thông tin thú cưng
        self.pet_table = QTableWidget()
        self.pet_table.setColumnCount(3)
        self.pet_table.setHorizontalHeaderLabels(["Tên thú cưng", "Loại", "Tuổi"])
        self.pet_table.horizontalHeader().setStretchLastSection(True)

        # Form thêm thú cưng
        form_layout = QHBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Tên thú cưng")

        self.type_input = QLineEdit()
        self.type_input.setPlaceholderText("Loại")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Tuổi")

        add_button = QPushButton("Thêm")
        add_button.setStyleSheet(
            "background-color: #0078D7; color: white; font-weight: bold;"
        )
        add_button.clicked.connect(self.add_pet)

        delete_button = QPushButton("Xóa")
        delete_button.setStyleSheet(
            "background-color: #ff4d4d; color: white; font-weight: bold;"
        )
        delete_button.clicked.connect(self.delete_pet)

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.type_input)
        form_layout.addWidget(self.age_input)
        form_layout.addWidget(add_button)
        form_layout.addWidget(delete_button)

        # Sắp xếp các thành phần
        layout.addWidget(title)
        layout.addWidget(self.pet_table)
        layout.addLayout(form_layout)

        self.setLayout(layout)

    def add_pet(self):
        name = self.name_input.text()
        pet_type = self.type_input.text()
        age = self.age_input.text()

        if name and pet_type and age:
            row_position = self.pet_table.rowCount()
            self.pet_table.insertRow(row_position)
            self.pet_table.setItem(row_position, 0, QTableWidgetItem(name))
            self.pet_table.setItem(row_position, 1, QTableWidgetItem(pet_type))
            self.pet_table.setItem(row_position, 2, QTableWidgetItem(age))

            # Xóa dữ liệu trong ô nhập sau khi thêm
            self.name_input.clear()
            self.type_input.clear()
            self.age_input.clear()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")

    def delete_pet(self):
        selected_rows = self.pet_table.selectionModel().selectedRows()
        for row in selected_rows:
            self.pet_table.removeRow(row.row())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý thú cưng")
        self.setGeometry(200, 200, 800, 600)

        # Sử dụng QStackedWidget để chuyển đổi giữa các trang
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Tạo các trang
        self.login_page = LoginPage(self.show_main_page)
        self.main_page = MainPage()

        # Thêm các trang vào QStackedWidget
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.main_page)

        # Hiển thị trang đăng nhập ban đầu
        self.stacked_widget.setCurrentWidget(self.login_page)

    def show_main_page(self):
        self.stacked_widget.setCurrentWidget(self.main_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Gradient màu xanh dương cho toàn bộ app
    app.setStyleSheet(
        """
        QMainWindow {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #e0f7fa, stop:1 #0078D7);
        }
    """
    )

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
