from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QLineEdit,
)
import sys


class Window2(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Cửa sổ 2")
        self.setGeometry(400, 200, 400, 300)

        layout = QVBoxLayout()

        # Label hiển thị
        self.label = QLabel("Đây là cửa sổ 2")
        self.label.setStyleSheet("font-size: 20px; margin: 10px;")

        # Nút quay lại
        back_button = QPushButton("Quay lại cửa sổ chính")
        back_button.setStyleSheet(
            """
            QPushButton {
                padding: 10px;
                font-size: 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )
        back_button.clicked.connect(self.go_back)

        # Nút đến cửa sổ 3
        next_button = QPushButton("Đến cửa sổ 3")
        next_button.setStyleSheet(
            """
            QPushButton {
                padding: 10px;
                font-size: 16px;
                background-color: #008CBA;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #007399;
            }
        """
        )
        next_button.clicked.connect(self.go_to_window3)

        layout.addWidget(self.label)
        layout.addWidget(back_button)
        layout.addWidget(next_button)

        self.setLayout(layout)

    def go_back(self):
        self.parent.show()
        self.hide()

    def go_to_window3(self):
        self.window3 = Window3(self)
        self.window3.show()
        self.hide()


class Window3(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Cửa sổ 3")
        self.setGeometry(500, 300, 400, 300)

        layout = QVBoxLayout()

        # Label và input
        self.label = QLabel("Đây là cửa sổ 3")
        self.label.setStyleSheet("font-size: 20px; margin: 10px;")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Nhập gì đó...")
        self.input.setStyleSheet(
            """
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
        """
        )

        # Nút quay lại
        back_button = QPushButton("Quay lại cửa sổ 2")
        back_button.setStyleSheet(
            """
            QPushButton {
                padding: 10px;
                font-size: 16px;
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """
        )
        back_button.clicked.connect(self.go_back)

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def go_back(self):
        self.parent.show()
        self.hide()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Cửa sổ Chính")
        self.setGeometry(300, 100, 400, 300)

        # Widget trung tâm
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()

        # Label chào mừng
        welcome_label = QLabel("Chào mừng đến với ứng dụng!")
        welcome_label.setStyleSheet(
            """
            QLabel {
                font-size: 20px;
                color: #333;
                margin: 10px;
            }
        """
        )

        # Nút chuyển đến cửa sổ 2
        next_button = QPushButton("Đến cửa sổ 2")
        next_button.setStyleSheet(
            """
            QPushButton {
                padding: 10px;
                font-size: 16px;
                background-color: #008CBA;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #007399;
            }
        """
        )
        next_button.clicked.connect(self.show_window2)

        layout.addWidget(welcome_label)
        layout.addWidget(next_button)

        central_widget.setLayout(layout)

        # Thiết lập style cho cửa sổ
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #f0f0f0;
            }
        """
        )

    def show_window2(self):
        self.window2 = Window2(self)
        self.window2.show()
        # self.hide()


def main():
    app = QApplication(sys.argv)

    # Thiết lập style chung cho ứng dụng
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
