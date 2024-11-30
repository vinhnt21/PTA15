import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
    QGridLayout,
)


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)
        self.initUI()

    def initUI(self):
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Display line edit
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; height: 50px;")
        self.layout.addWidget(self.display)

        # Button layout
        self.button_layout = QGridLayout()
        self.layout.addLayout(self.button_layout)

        # Buttons
        buttons = [
            ("7", 0, 0),
            ("8", 0, 1),
            ("9", 0, 2),
            ("/", 0, 3),
            ("4", 1, 0),
            ("5", 1, 1),
            ("6", 1, 2),
            ("*", 1, 3),
            ("1", 2, 0),
            ("2", 2, 1),
            ("3", 2, 2),
            ("-", 2, 3),
            ("C", 3, 0),
            ("0", 3, 1),
            ("=", 3, 2),
            ("+", 3, 3),
        ]

        # Add buttons to layout
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; height: 50px;")
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            self.button_layout.addWidget(button, row, col)

        # Internal variable to hold the expression
        self.expression = ""

    def on_button_click(self, text):
        """Handle button clicks."""
        if text == "C":
            self.expression = ""
            self.display.setText("")
        elif text == "=":
            try:
                # Evaluate the expression
                result = eval(self.expression)
                self.display.setText(str(result))
                self.expression = str(result)  # Allow chaining calculations
            except Exception as e:
                self.display.setText("Error")
                self.expression = ""
        else:
            # Add text to the expression
            self.expression += text
            self.display.setText(self.expression)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec())
