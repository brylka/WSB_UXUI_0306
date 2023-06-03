import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moja aplikacja PyQt")

        self.button = QPushButton("Naciśnij mnie! \nPonieważ lubię byc klikany!\nDziękuję!")

        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("Kliknięty!\nDziękuję!")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()