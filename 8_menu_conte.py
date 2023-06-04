import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QMenu
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Menu pod prawym przyciskiem myszy")
        self.setCentralWidget(self.label)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("Pozycja 1", self))
        context.addAction(QAction("Pozycja 2", self))
        context.addAction(QAction("Pozycja 3", self))
        context.addAction(QAction("Pozycja 4", self))
        context.exec(e.globalPos())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()