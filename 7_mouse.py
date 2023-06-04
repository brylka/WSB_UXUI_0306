import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500,300)
        self.label = QLabel("kliknij w okno")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e):
        x = e.position().x()
        y = e.position().y()
        self.label.setText(f"Kliknięto w okno w pozycji o współrzędnych ({x}, {y})")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()