from typing import List, Tuple

from PySide6.QtCore import QRunnable, QObject, Signal
from mysql.connector.cursor import MySQLCursor

from app.core import DataMapper
from app.core.Database import call_procedures


class _Signals(QObject):
    countsLoaded: Signal = Signal(int, int, int)


class StatusCountRunnable(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = _Signals()

    def run(self, /):
        call_procedures(
            self.load_counts,
        )

    def load_counts(self, cursor: MySQLCursor):
        """
        Count Anzeige laden
        :param cursor:
        :return:
        """
        cursor.execute("SELECT * FROM get_status_counts")
        counts: List[Tuple[int]] = cursor.fetchall()
        converted: List[int] = DataMapper.extract_first_rows(counts)
        available, reserved, in_repair = converted
        self.signals.countsLoaded.emit(available, reserved, in_repair)

