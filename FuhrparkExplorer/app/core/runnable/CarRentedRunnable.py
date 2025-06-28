from PySide6.QtCore import QRunnable, QObject, Signal
from mysql.connector.cursor import MySQLCursor

from app.core.Database import call_procedures


class _Signals(QObject):
    statusLoaded: Signal = Signal(list)
    rentedLoaded: Signal = Signal(list)
    finished: Signal = Signal()

class CarRentedRunnable(QRunnable):
    """
    Runnable für das Handlen von Vermietungen.

    - Ein Fahrzeug wird vermietet, dann wird dieses in die Datenbank aufgenommen
    - Der neue Status wird komplett aus der DB geholt und der alter überschrieben (sieht, CarStatus)
    - Status - vermietet wird in eine Liste aufgenommen

    """
    def __init__(self, customer_id: int, model_name: str, from_date: str, to_data: str, total_price: float):
        super().__init__()
        self._customer_id = customer_id
        self._from_date = from_date
        self._to_data = to_data
        self._model_name = model_name
        self._total_price = total_price

        self.signals = _Signals()

    def run(self, /):
        call_procedures(self.insert_car_rented, self.load_status, self.load_rented,  commit=True)

    def insert_car_rented(self, cursor: MySQLCursor):
        cursor.callproc("p_insert_fahrzeug_kunde_vermietung",  (
            self._customer_id,
            self._model_name,
            self._from_date,
            self._to_data,
            self._total_price
        ))

    def load_status(self, cursor: MySQLCursor) -> None:
        cursor.execute("SELECT * FROM view_get_fahrzeugstatus")
        status = cursor.fetchall()
        self.signals.statusLoaded.emit(status)
        # self.signals.finished.emit() # TODO

    def load_rented(self, cursor: MySQLCursor) -> None:
        cursor.execute("SELECT * FROM view_get_fahrzeug_kunde_vermietung_vermietet")
        rented = cursor.fetchall()
        self.signals.rentedLoaded.emit(rented)





















