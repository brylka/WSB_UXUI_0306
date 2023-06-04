import sys

from PyQt6.QtGui import QPalette, QColor, QAction
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel


class Cokolwiek(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        menu_bar = self.menuBar()

        hello_action = QAction("Hello", self)
        hello_action.triggered.connect(self.hello)

        file_menu = menu_bar.addMenu("Plik")
        file_menu.addAction(hello_action)

        view_action = QAction("Widok", self)
        view_action.triggered.connect(self.view)
        menu_bar.addAction(view_action)




        self.setWindowTitle("Przykład menu w Qt6")


        self.label = QLabel("test")


        layout = QVBoxLayout()
        layout.addWidget(self.label)

        central = QWidget()
        central.setLayout(layout)

        self.setCentralWidget(central)

    def hello(self):
        self.label.setText("Witaj Świecie!!!!!")

    def view(self):
        self.resize(500,300)


aap = QApplication(sys.argv)
xyz = Cokolwiek()
xyz.show()
aap.exec()
