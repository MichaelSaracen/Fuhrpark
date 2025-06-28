from PySide6.QtCore import QObject, Signal, QRunnable

from app.core.Database import call_procedures


class _Signals(QObject):
    statusOk: Signal = Signal()
    errorOccurred: Signal = Signal(str)

class ConnectionRunnable(QRunnable):
    """
    Die Klasse **ConnectionRunnable** hilft dabei, in einem Timer, die Verbindung zum MySQL Server zu überprüfen.

    Wenn die Verbindung nicht mehr vorhanden ist, wird das Signal **errorOccurred** gefeuert.

    Damit soll gewährleistet werden, dass bei Verbindungsabbruch, nicht mehr versucht werden kann, Anfragen an die
    Datenbank zu schicken.
    """
    def __init__(self):
        super().__init__()
        self.signals = _Signals()

    def run(self, /):
        try:
            call_procedures()
            self.signals.statusOk.emit()
        except Exception as e:
            try:
                self.signals.errorOccurred.emit(e)
            except Exception:
                pass
            # QMetaObject.invokeMethod(self.signals.errorOccurred, "emit", Qt.QueuedConnection,
            #                          Q_ARG(str, str(e)))

