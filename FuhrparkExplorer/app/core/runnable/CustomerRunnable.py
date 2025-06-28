from PySide6.QtCore import QObject, Signal, QRunnable
from mysql.connector.cursor import MySQLCursor

from app.core.Database import call_procedures


class _Signals(QObject):
    finished: Signal = Signal(list)

class CustomerRunnable(QRunnable):
    def __init__(self, f_name, name, age, tel, city, zip_, street, h_num, bank, iban):
        super().__init__()
        self._zip = zip_
        self._iban = iban
        self._bank = bank
        self._h_num = h_num
        self._city = city
        self._tel = tel
        self._age = age
        self._name = name
        self._f_name = f_name
        self._street = street
        self.signals = _Signals()

    def run(self, /):
        call_procedures(self.insert_customer, self.load_customers,  commit=True)


    def insert_customer(self, cursor: MySQLCursor):
        cursor.callproc("p_insert_kunde", [
            self._f_name, self._name, self._age, self._tel, self._city, self._zip,
            self._street, self._h_num, self._iban, self._bank
        ])

    def load_customers(self, cursor: MySQLCursor) -> None:
        """
        Laden der Kunden
        :param cursor:
        :return:
        """
        cursor.execute("SELECT * FROM view_get_all_customers")
        customers =  cursor.fetchall()
        self.signals.finished.emit(customers)




