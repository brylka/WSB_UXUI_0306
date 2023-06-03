import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Przeglądanie danych MySQL")
        self.setFixedSize(600,300)

        layout = QVBoxLayout()


        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='xxx'
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")

            records = cursor.fetchall()

        for record in records:
            id, name, surname, email = record
            record_label = QLabel(f"ID: {id:>3} Imię: {name:<15} Nazwisko: {surname:<15} Email: {email:<30}")
            layout.addWidget(record_label)

            #print(f"ID: {id}, Imię: {name}, Nazwisko: {surname}, Email: {email}")
            #print(f"ID: {id:>3} Imię: {name:<15} Nazwisko: {surname:<15} Email: {email:<30}")

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()