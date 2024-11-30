# Cách liên kết App và Window trong PyQt6 🔗

## 1. Mối quan hệ cơ bản

Hãy tưởng tượng như này:

- `QApplication` (app) giống như một sân chơi lớn
- `QMainWindow` (window) như một khu vui chơi trong sân đó
- Mọi widget (nút bấm, nhãn,...) là các trò chơi trong khu vui chơi

## 2. Cấu trúc phân cấp

```
QApplication (app)
    └── QMainWindow (window)
         ├── Widget 1
         ├── Widget 2
         └── Widget 3
```

## 3. Ví dụ code cơ bản:

```python
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
        self.label.setText("Đã bấm nút!")

# Tạo ứng dụng
app = QApplication(sys.argv)

# Tạo cửa sổ chính
window = MainWindow()
window.show()

# Chạy ứng dụng
app.exec()
```

## 4. Giải thích chi tiết:

### Khởi tạo ứng dụng:

```python
app = QApplication(sys.argv)
```

- Đây là bước đầu tiên, PHẢI CÓ để tạo ứng dụng PyQt6
- Giống như bạn mở một sân chơi mới

### Tạo cửa sổ chính:

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
```

- Tạo một cửa sổ chính kế thừa từ QMainWindow
- Như việc xây dựng một khu vui chơi trong sân

### Liên kết thông qua Parent-Child:

```python
self.button = QPushButton("Bấm vào đây!", self)
self.label = QLabel("Chưa bấm nút", self)
```

- Từ khóa `self` trong widget cho biết widget này thuộc về window
- Giống việc nói "nút này thuộc về cửa sổ này"

### Liên kết qua Signals và Slots:

```python
self.button.clicked.connect(self.button_clicked)
```

- Khi nút được bấm (signal) sẽ gọi hàm button_clicked (slot)
- Như việc nói "khi bấm nút thì làm việc này"

## 5. Một số lưu ý quan trọng:

1. **Thứ tự khởi tạo**:

   - QApplication LUÔN phải được tạo TRƯỚC
   - Window được tạo SAU QApplication
   - Widgets được tạo trong window

2. **Parent-Child**:

   - Mọi widget nên có parent (thường là window)
   - Khi parent bị hủy, tất cả child cũng bị hủy

3. **Show và Exec**:
   ```python
   window.show()  # Hiển thị cửa sổ
   app.exec()     # Chạy vòng lặp sự kiện
   ```
   - `show()` hiển thị cửa sổ
   - `exec()` giữ cho ứng dụng chạy

## 6. Ví dụ thực tế đơn giản:

```python
from PyQt6.QtWidgets import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Máy tính đơn giản")
        self.setGeometry(100, 100, 200, 200)

        # Tạo widget chính
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tạo layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Thêm các widget con
        self.input = QLineEdit()
        self.button = QPushButton("Tính tổng")
        self.result = QLabel("Kết quả: ")

        # Thêm vào layout
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        # Liên kết nút với hàm xử lý
        self.button.clicked.connect(self.calculate)

    def calculate(self):
        try:
            numbers = [int(x) for x in self.input.text().split()]
            self.result.setText(f"Kết quả: {sum(numbers)}")
        except:
            self.result.setText("Lỗi! Hãy nhập các số cách nhau bởi dấu cách")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()
```
