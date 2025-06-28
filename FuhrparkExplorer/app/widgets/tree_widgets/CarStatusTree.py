from PySide6.QtCore import Signal, Qt, Slot, QThreadPool, QPoint
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QMenu

from app.core import Database
from app.core.runnable import StatusCountRunnable
from app.widgets.delegates.TreeStatusWidget import TreeStatusWidget


class CarStatusTree(QTreeWidget):
    """
    Widget zur Anzeige und Verwaltung des Fahrzeugstatus.

    Dieses Tree-Widget zeigt Fahrzeugstatus-Gruppen ("vermietet", "verfügbar", "in Reparatur")
    als Top-Level-Knoten und darunter die einzelnen Fahrzeuge mit ihren Details an.
    Über Kontextmenüs kann der Status eines Fahrzeugs geändert werden (außer im Status "vermietet").

    Signale:
        statusCountChanged (Signal): Enthält die Anzahl der Fahrzeuge in den Statusgruppen (vermietet, verfügbar, in Reparatur).
        statusChanged (Signal): Wird gefeuert, sobald ein Fahrzeugstatus geändert wurde.
    """

    statusCountChanged: Signal = Signal(int, int, int)
    statusChanged: Signal = Signal()
    def __init__(self, parent: QWidget=None):
        """
        Initialisiert das CarStatusTree-Widget und setzt Kontextmenü-Policy.
        """
        super().__init__(parent=parent)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def load_status(self, results) -> None:
        """
        Lädt Statusdaten in das Tree-Widget und startet das Zählen pro Status.

        :param results: Verschachteltes Dictionary mit Status -> Marken -> Modelle -> (s_id, car_id, pic)
        """
        self.clear()
        for status, car in results.items():
            status_item: QTreeWidgetItem = QTreeWidgetItem([status])
            self.addTopLevelItem(status_item)

            for brand, models in car.items():
                for model, (s_id, car_id, pic) in models.items():
                    model_item: QTreeWidgetItem = QTreeWidgetItem()
                    model_item.setData(
                        0,
                        Qt.ItemDataRole.DisplayRole,
                        {
                            "Status" : status,
                            "Marke": brand,
                            "Modell": model,
                            "Fahrzeugnummer": car_id
                        }
                    )
                    status_item.addChild(model_item)
                    widget: TreeStatusWidget = TreeStatusWidget(status, brand, model, car_id, pic, self)
                    self.setItemWidget(model_item, 0, widget)
        self.expandAll()

        runnable: StatusCountRunnable = StatusCountRunnable()
        runnable.signals.countsLoaded.connect(self.statusCountChanged.emit)
        QThreadPool.globalInstance().start(runnable)

    @Slot(QPoint)
    def on_context_menu(self, pos: QPoint) -> None:
        """
        Öffnet das Kontextmenü zum Ändern des Fahrzeugstatus (ausgenommen vermietet).

        :param pos: Position des Rechtsklicks relativ zum Widget
        """
        item: QTreeWidgetItem = self.itemAt(pos)
        if not item:
            return

        data: dict[str, str] = item.data(0, Qt.ItemDataRole.DisplayRole)
        status: str = data.get("Status")
        if status and  "vermietet" in status:
            return

        model: str = data.get("Modell")
        menu: QMenu = QMenu()

        if "in Reparatur" in status:
            available_action: QAction = QAction("verfügbar", self)
            available_action.triggered.connect(lambda: self.on_status_changed(model, "verfügbar"))
            menu.addAction(available_action)

        if "verfügbar" in status:
            repair_action: QAction = QAction("in Reparatur", self)
            repair_action.triggered.connect(lambda : self.on_status_changed(model, "in Reparatur"))
            menu.addAction(repair_action)

        menu.exec(self.viewport().mapToGlobal(pos))

    @Slot(str, str)
    def on_status_changed(self, model: str, status: str) -> None:
        """
        Ändert den Status eines Fahrzeugs in der Datenbank und feuert das statusChanged-Signal.

        :param model: Modellname des Fahrzeugs
        :param status: Neuer Status (z. B. "verfügbar", "in Reparatur")
        """
        Database.call_procedure("p_insert_fahrzeug_status", (model, status), commit=True)
        self.statusChanged.emit()
