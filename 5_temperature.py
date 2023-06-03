import time

import requests as requests
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Parametry okna
        self.setWindowTitle("Dane pogodowe")
        self.setFixedSize(500,300)

        # Dwie labelki: pogodowa i z czasem
        self.temperatute_label = QLabel()
        self.temperatute_label.setStyleSheet("font-size: 36px; qproperty-alignment: 'AlignCenter';")
        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-size: 20px; qproperty-alignment: 'AlignCenter';")

        # Stworzenie layoutu i dodanie labelek
        layout = QVBoxLayout()
        layout.addWidget(self.temperatute_label)
        layout.addWidget(self.time_label)

        # Stworzenie centralnego widzetu
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

        # Stworzenie timera, co minutę pobiera dane z API
        self.timer = QTimer()
        self.timer.timeout.connect(self.fetch_weather_data)
        self.timer.start(60000) # 60000ms = 60s = 1min

        # Pierwsze pobranie danych po uruchomieniu aplikacji
        self.fetch_weather_data()


    def fetch_weather_data(self):
        # Pobranie danych
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Wroclaw&appid=0ec4c77b4de3d2407f33e949c56bcf31')
        data = response.json()
        # Wyłuskanie konkretnych danych
        temperature = data['main']['temp'] - 273.15
        # ZAmiana timestampa na zrozumiały czas
        fetch_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data['dt']))
        local_time = time.strftime('%Y.%m.%d %H:%M:%S', time.localtime())

        # Podmiana tekstu w labelkach
        self.temperatute_label.setText(f"Temperatura: {temperature:.2f} °C")
        self.time_label.setText(f"Czas zarejestrowania danych: {fetch_time}\nCzas pobrania danych z API: {local_time}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()