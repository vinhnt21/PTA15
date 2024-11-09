from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimer, Qt, QRect
from PyQt6.QtGui import QPainter, QColor, QFont
import sys
import random


# Lớp chim (Bird)
class Bird:
    def __init__(self):
        self.x = 50
        self.y = 250
        self.velocity = 0
        self.gravity = 2  # Trọng lực

    def flap(self):
        self.velocity = -10  # Nhảy lên

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity


# Lớp ống (Pipe)
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 60
        self.gap = 150
        self.height_top = random.randint(50, 300)
        self.height_bottom = 500 - self.height_top - self.gap  # Độ cao ống dưới

    def update(self):
        self.x -= 5  # Tốc độ di chuyển của ống


# Lớp trò chơi chính
class FlappyBirdGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flappy Bird Game")
        self.setGeometry(100, 100, 400, 500)
        self.bird = Bird()
        self.pipes = [Pipe(400)]
        self.score = 0
        self.is_game_over = False

        # Hiển thị điểm số
        self.score_label = QLabel(f"Score: {self.score}", self)
        self.score_label.setFont(QFont("Arial", 20))
        self.score_label.move(10, 10)

        # Thiết lập bộ hẹn giờ để cập nhật trò chơi
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(30)  # 30 ms = 33 FPS

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Vẽ con chim
        painter.setBrush(QColor(255, 223, 0))
        painter.drawEllipse(self.bird.x, self.bird.y, 30, 30)

        # Vẽ ống
        painter.setBrush(QColor(34, 139, 34))
        for pipe in self.pipes:
            painter.drawRect(pipe.x, 0, pipe.width, pipe.height_top)
            painter.drawRect(
                pipe.x, 500 - pipe.height_bottom, pipe.width, pipe.height_bottom
            )

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            if self.is_game_over:
                self.restart_game()
            else:
                self.bird.flap()

    def update_game(self):
        if self.is_game_over:
            return

        # Cập nhật vị trí của chim
        self.bird.update()

        # Cập nhật các ống và kiểm tra va chạm
        for pipe in self.pipes:
            pipe.update()
            if pipe.x < -pipe.width:
                self.pipes.remove(pipe)
                self.pipes.append(Pipe(400))  # Thêm ống mới sau khi ống cũ đi qua

            # Kiểm tra va chạm với ống
            if (self.bird.x + 30 > pipe.x and self.bird.x < pipe.x + pipe.width) and (
                self.bird.y < pipe.height_top
                or self.bird.y + 30 > 500 - pipe.height_bottom
            ):
                self.game_over()

            # Kiểm tra khi chim vượt qua ống để tăng điểm
            if pipe.x + pipe.width == self.bird.x:
                self.score += 1
                self.score_label.setText(f"Score: {self.score}")

        # Kiểm tra va chạm với mặt đất hoặc bay lên khỏi màn hình
        if self.bird.y > 470 or self.bird.y < 0:
            self.game_over()

        # Cập nhật lại giao diện
        self.update()

    def game_over(self):
        self.is_game_over = True
        self.score_label.setText(f"Game Over! Final Score: {self.score}")

    def restart_game(self):
        # Khởi động lại trò chơi
        self.bird = Bird()
        self.pipes = [Pipe(400)]
        self.score = 0
        self.is_game_over = False
        self.score_label.setText(f"Score: {self.score}")


# Chạy ứng dụng
app = QApplication(sys.argv)
window = FlappyBirdGame()
window.show()
sys.exit(app.exec())
