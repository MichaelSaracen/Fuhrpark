from PySide6.QtCore import QObject, Signal, QRunnable
from mysql.connector.cursor import MySQLCursor

from app.core.Database import call_procedures


class _Signals(QObject):
    customersLoaded: Signal = Signal(list)
    rentedLoaded: Signal = Signal(list)


class UpdatedCustomersRunnable(QRunnable):
    def __init__(self):
        super().__init__()

        self.signals = _Signals()

    def run(self, /):
        call_procedures(self.load_rented, self.load_customers)


    def load_customers(self, cursor: MySQLCursor) -> None:
        """
        Laden der Kunden
        :param cursor:
        :return:
        """
        cursor.execute("SELECT * FROM view_get_all_customers")
        customers =  cursor.fetchall()
        self.signals.customersLoaded.emit(customers)

    def load_rented(self, cursor: MySQLCursor) -> None:
        cursor.execute("SELECT * FROM view_get_fahrzeug_kunde_vermietung_vermietet")
        rented = cursor.fetchall()
        self.signals.rentedLoaded.emit(rented)