import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.counter = 0

        self.setWindowTitle("Moja aplikacja PyQt")

        self.button = QPushButton("Naciśnij mnie! \nPonieważ lubię byc klikany!\nDziękuję!")

        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.counter += 1
        #self.button.setText("Kliknięto " + str(self.counter) + " razy!")
        if self.counter == 1:
            self.button.setText(f"Kliknięto 1 raz!")
        else:
            self.button.setText(f"Kliknięto {self.counter} razy!")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()