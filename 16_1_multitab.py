import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, \
    QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabliczka mnożenia")
        self.resize(500,500)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createOutputArea()
        self._createMultiplicationTable()


    def _createMultiplicationTable(self):
        buttonsLayout = QGridLayout()
        self.buttonMap = {}

        for a in range(1,11):
            for b in range(1,11):
                result = a*b
                button = QPushButton(str(result))
                button.clicked.connect(self.showMultiplication)
                buttonsLayout.addWidget(button, a, b)
                self.buttonMap[str(result)] = (a,b)

        self.generalLayout.addLayout(buttonsLayout)

    def _createOutputArea(self):
        self.outputArea = QTextEdit()
        self.outputArea.setReadOnly(True)
        self.generalLayout.addWidget(self.outputArea)

    def showMultiplication(self):
        button_text = self.sender().text()
        a, b = self.buttonMap[button_text]
        #self.outputArea.setText(str(a) + ' * ' + str(b) + ' = ' + str(button_text))
        self.outputArea.setText(f"{a} * {b} = {button_text}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()