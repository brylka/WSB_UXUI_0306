import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QMenu, QCheckBox, QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Comboboxa")

        combobox = QComboBox()
        combobox.addItems(["Pierwszy", "Drugi", "Trzeci", "Czwarty"])
        combobox.setEditable(True)

        combobox.currentIndexChanged.connect(self.index_changed)
        combobox.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(combobox)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()