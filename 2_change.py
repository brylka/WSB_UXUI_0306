import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moja aplikacja")

        self.button = QPushButton("Naciśnij mnie!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("Kliknąłeś mnie!")
        self.button.setEnabled(False)

        self.setWindowTitle("Kliknięto przycisk")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()