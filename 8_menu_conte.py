import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QFont
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QMenu
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Menu pod prawym przyciskiem myszy")
        self.setCentralWidget(self.label)

        self.font_size = 6

    def contextMenuEvent(self, e):
        context = QMenu(self)

        action1 = QAction("Zmień rozmiar okna", self)
        action1.triggered.connect(self.resize_window)

        action2 = QAction("Zmień tekst", self)
        action2.triggered.connect(self.change_text)

        action3 = QAction("Zwiększ tekst", self)
        action3.triggered.connect(self.change_font_size)

        action4 = QAction("Zamknij aplikację", self)
        action4.triggered.connect(self.close_app)

        context.addAction(action1)
        context.addAction(action2)
        context.addAction(action3)
        context.addAction(action4)
        context.exec(e.globalPos())

    def resize_window(self):
        self.resize(600,400)

    def change_text(self):
        self.label.setText("Witaj Świecie!")

    def change_font_size(self):
        self.font_size += 2
        self.label.setFont(QFont("Arial", self.font_size))

    def close_app(self):
        self.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()