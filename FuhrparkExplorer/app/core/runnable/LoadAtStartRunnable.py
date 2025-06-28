from PySide6.QtCore import QRunnable, QObject, Signal
from mysql.connector.cursor import MySQLCursor

from app.core.Database import call_procedures


class _Signals(QObject):
    carsLoaded: Signal = Signal(list)
    pricesLoaded: Signal = Signal(list)
    customersLoaded: Signal = Signal(list)
    statusLoaded: Signal = Signal(list)
    rentedLoaded: Signal = Signal(list)
    statisticLoaded: Signal = Signal(list)
    statisticModelsLoaded: Signal = Signal(list)
    historyLoaded: Signal = Signal(list)

class LoadAtStartRunnable(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = _Signals()

    def run(self, /):
        call_procedures(
            self.load_cars,
            self.load_prices,
            self.load_customers,
            self.load_status,
            self.load_rented,
            self.load_statistics,
            self.load_statistics_models,
            self.load_all_statistics
        )

    def load_cars(self, cursor: MySQLCursor):
        """
        Fahrzeuge laden.
        :param cursor:
        :return:
        """
        cursor.callproc("p_get_fahrzeuge")
        cars = [result.fetchall() for result in cursor.stored_results()]
        self.signals.carsLoaded.emit(cars[0])

    def load_prices(self, cursor: MySQLCursor):
        """
        Preis Übersicht laden
        :param cursor:
        :return:
        """
        cursor.callproc("p_get_fahrzeug_tagespreis")
        prices = [result.fetchall() for result in cursor.stored_results()]
        self.signals.pricesLoaded.emit(prices[0])

    def load_customers(self, cursor: MySQLCursor) -> None:
        """
        Laden der Kunden
        :param cursor:
        :return:
        """
        cursor.execute("SELECT * FROM view_get_all_customers")
        customers =  cursor.fetchall()
        self.signals.customersLoaded.emit(customers)

    def load_status(self, cursor: MySQLCursor) -> None:
        cursor.execute("SELECT * FROM view_get_fahrzeugstatus")
        status = cursor.fetchall()
        self.signals.statusLoaded.emit(status)

    def load_rented(self, cursor: MySQLCursor) -> None:
        cursor.execute("SELECT * FROM view_get_fahrzeug_kunde_vermietung_vermietet")
        rented = cursor.fetchall()
        self.signals.rentedLoaded.emit(rented)

    def load_statistics(self, cursor: MySQLCursor) -> None:
        cursor.execute("SELECT * FROM view_get_statistik_marke_anzahl")
        statistic = cursor.fetchall()
        self.signals.statisticLoaded.emit(statistic)

    def load_statistics_models(self, cursor: MySQLCursor) -> None:
        cursor.execute("SELECT * FROM view_get_statístik_modell_anzahl")
        statistic = cursor.fetchall()
        self.signals.statisticModelsLoaded.emit(statistic)

    def load_all_statistics(self, cursor: MySQLCursor) -> None:
        cursor.execute("SELECT * FROM FahrzeugVermietungStatistik ORDER BY datum_end DESC")
        statistic = cursor.fetchall()
        self.signals.historyLoaded.emit(statistic)
