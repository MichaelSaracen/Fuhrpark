from PySide6.QtCore import QObject, Signal, QRunnable
from mysql.connector.cursor import MySQLCursor

from app.core.Database import call_procedures


class _Signals(QObject):
    finished: Signal = Signal()


class UpdateCustomerRunnable(QRunnable):
    def __init__(self, col_name, id_, value):
        super().__init__()
        self._value = value
        self._id_ = id_
        self._col_name = col_name

        self.signals = _Signals()

    def run(self, /):
        call_procedures(self.customer_update, commit=True)

    def customer_update(self, cursor: MySQLCursor):
        cursor.callproc("p_update_kunde_generic", (self._col_name, self._id_, self._value))
        self.signals.finished.emit()