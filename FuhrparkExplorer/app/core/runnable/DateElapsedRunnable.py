from typing import List

from PySide6.QtCore import QRunnable, QObject, Signal
from mysql.connector.cursor import MySQLCursor

from app.core.Database import call_procedures


class _Signals(QObject):
    finished: Signal = Signal()


class DateElapsedRunnable(QRunnable):
    _car_ids: list[int]

    def __init__(self, car_ids: List[int]):
        super().__init__()
        self.signals = _Signals()
        self._car_ids = car_ids

    def run(self, /):
        call_procedures(
            self.update_elapsed, commit=True
        )

    def update_elapsed(self, cursor: MySQLCursor):
        """
        Count Anzeige laden
        :param cursor:
        :return:
        """
        for car_id in self._car_ids:
            cursor.callproc("p_update_fahrzeug_status_on_elapse_end_date", (car_id, ))

        self.signals.finished.emit()

