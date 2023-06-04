import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QApplication, QMenu, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test CheckBoxa")

        self.checkbox = QCheckBox("Zaznacz mnie")
        self.checkbox.stateChanged.connect(self.checkbox_action)
        #self.checkbox.setCheckState(Qt.CheckState.Checked)

        self.setCentralWidget(self.checkbox)

    def checkbox_action(self, s):
        if s == 2:
            self.checkbox.setText("Jest zaznaczony")
        else:
            self.checkbox.setText("Nie jest zaznaczony")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()