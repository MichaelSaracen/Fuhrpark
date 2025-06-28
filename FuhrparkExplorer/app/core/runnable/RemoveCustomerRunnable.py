from PySide6.QtCore import QObject, Signal, QRunnable
from mysql.connector.cursor import MySQLCursor

from app.core.Database import call_procedures


class _Signals(QObject):
    finished: Signal = Signal()

class RemoveCustomerRunnable(QRunnable):
    def __init__(self, id_: int):
        super().__init__()
        self._id_ = id_

        self.signals = _Signals()

    def run(self, /):
        call_procedures(self.remove_customer, commit=True)

    def remove_customer(self, cursor: MySQLCursor) -> None:
        cursor.callproc ("p_delete_kunde_and_from_vermietung", (self._id_, ))
        self.signals.finished.emit()