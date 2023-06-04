import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QMenu, QCheckBox, QComboBox, QListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Listy")

        list = QListWidget()
        list.addItems(["Pierwszy", "Drugi", "Trzeci", "Czwarty"])
        #list.setEditable(True)

        list.currentItemChanged.connect(self.index_changed)
        list.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(list)

    def index_changed(self, i):
        print(i.text())

    def text_changed(self, s):
        print(s)



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()