import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(600,600)
        self.label = QLabel("kliknij w okno")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e):
        x = e.position().x()
        y = e.position().y()
        self.label.setText(f"Kliknięto ({x}, {y})")

        if x <= 200:
            if y <= 200:
                self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            elif y >= 400:
                self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
            else:
                self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        elif x >= 400:
            if y <= 200:
                self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
            elif y >= 400:
                self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
            else:
                self.label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        else:
            if y <= 200:
                self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
            elif y > 200 and y < 400:
                self.label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
            elif y >= 400:
                self.label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()