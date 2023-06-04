import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moja aplikacja")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('green'))
        layout2.addWidget(Color('blue'))
        layout1.addLayout(layout2)

        layout1.addWidget(Color('yellow'))

        layout3.addWidget(Color('black'))
        layout3.addWidget(Color('white'))
        layout1.addLayout(layout3)


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()