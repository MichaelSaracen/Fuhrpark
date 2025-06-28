import mysql.connector
from PySide6.QtCore import QRunnable, QObject, Signal


class FieldLoaderSignals(QObject):
    finished: Signal = Signal(list)

class InitFieldRunnable(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = FieldLoaderSignals()

    def run(self):
        from app.core.Utils import get_db_config
        cfg = get_db_config()
        conn = mysql.connector.connect(
            host=cfg["host"],
            user=cfg["user"],
            password=cfg["password"],
            database=cfg["database"]
        )

        cursor = conn.cursor()
        results = []
        for procname in ["p_get_fuel", "p_get_brands", "p_get_gearbox"]:
            cursor.callproc(procname)
            for result in cursor.stored_results():
                results.append(result.fetchall())

        cursor.close()
        conn.close()

        self.signals.finished.emit(results)
