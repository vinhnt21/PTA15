from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Thiết lập cửa sổ
        self.setWindowTitle("Ví dụ về liên kết")
        self.setGeometry(100, 100, 400, 300)  # (x, y, width, height)

        # Tạo nút bấm
        self.button = QPushButton("Bấm vào đây!", self)
        self.button.setGeometry(150, 100, 100, 30)
        self.button.clicked.connect(self.button_clicked)

        # Tạo nhãn
        self.label = QLabel("Chưa bấm nút", self)
        self.label.setGeometry(150, 150, 100, 30)

    def button_clicked(self):
        self.label.setText("Nhật đẹp trai!")

# Tạo ứng dụng
app = QApplication(sys.argv)

# Tạo cửa sổ chính
window = MainWindow()
window.show()

# Chạy ứng dụng
app.exec()
