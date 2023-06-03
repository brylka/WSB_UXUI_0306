from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QTextEdit
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moja aplikacja")

        self.label = QLabel()
        self.label.setFixedWidth(300)
        #self.input = QLineEdit()
        self.input = QTextEdit()
        self.input.setFixedWidth(300)
        #self.input.textChanged.connect(self.label.setText)
        self.input.textChanged.connect(self.update_label_text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def update_label_text(self):
        self.label.setText(self.input.toPlainText())



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()