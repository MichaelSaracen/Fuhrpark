from PySide6.QtCore import QObject, Signal, QRunnable
from mysql.connector.cursor import MySQLCursor

from app.core.Database import call_procedures


class _Signals(QObject):
    finished: Signal = Signal()

class InsertCarRunnable(QRunnable):
    def __init__(self, img, brand, modell, fuel, gear, power, consum, doors, seats, color, price):
        super().__init__()
        self.img = img
        self.brand = brand
        self.modell = modell
        self.fuel = fuel
        self.gear = gear
        self.power = power
        self.consum = consum
        self.doors = doors
        self.seats = seats
        self.color = color
        self.price = price
        self.signals = _Signals()

    def run(self, /):
        call_procedures(self.insert_car, commit=True)

    def insert_car(self, cursor: MySQLCursor):
        cursor.callproc("p_insert_fahrzeug", [
            self.img, self.brand, self.modell, self.fuel, self.gear, self.power, self.consum, self.doors, self.seats,
            self.color, self.price
        ])

        self.signals.finished.emit()

