from typing import List

from PySide6.QtCore import Slot, QPoint, QDate
from PySide6.QtGui import Qt, QAction
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QTableWidget, QMenu, QRadioButton, \
    QAbstractItemView

from app.core import add_shadow
from app.gui.Ui_RentedCarsByCustomers import Ui_RentedCarsByCustomers

LABELS: List[str] = [
    "ID", "Kundennummer", "Vorname", "Nachname", "Telefon", "Fahrzeugnummer", "Marke", "Modell",
    "von", "bis", "Gesamtpreis (€)"
]

class RentedCarsByCustomers(QWidget):
    def __init__(self, parent: QWidget=None):
        """
        Initialisiert das Widget zur Anzeige vermieteter Fahrzeuge und richtet die Tabelle sowie Steuerelemente ein.
        """
        super().__init__(parent=parent)
        self._ui: Ui_RentedCarsByCustomers = Ui_RentedCarsByCustomers()
        self._ui.setupUi(self)

        add_shadow(self._ui.widget)

        self._ui.tableWidget.setColumnCount(11)
        self._ui.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self._ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ SIGNALS & SLOTS
        # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ contextMenu
        self._ui.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self._ui.tableWidget.customContextMenuRequested.connect(self.on_context_menu_open)

        # ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Suche
        self._ui.leSearch.textChanged.connect(self.on_search)


    @property
    def _current_radio_button(self) -> int:
        """
        Ermittelt den Index der aktuell ausgewählten Suchkategorie anhand der Radiobuttons.
        :return: Spaltenindex, der zum Suchkriterium gehört
        """
        rbs: List[QRadioButton] = self.findChildren(QRadioButton)
        text: str = next((rb.text() for rb in rbs if rb.isChecked()), None)
        return LABELS.index(text) if text else 1

    @Slot(QPoint)
    def on_context_menu_open(self, pos: QPoint) -> None:
        """
        Öffnet das Kontextmenü beim Rechtsklick auf eine Tabellenzeile.
        :param pos: Position des Klicks relativ zur Tabelle
        """
        table: QTableWidget = self._ui.tableWidget
        item: QTableWidgetItem = table.itemAt(pos)

        if not item:
            return

        menu: QMenu = QMenu(self)
        edit_action: QAction = QAction("Kunde bearbeiten", table)

        menu.addAction(edit_action)

        menu.exec(table.viewport().mapToGlobal(pos))

    @Slot(list)
    def on_add_items(self, items: list) -> None:
        """
        Befüllt die Tabelle mit Datensätzen zu vermieteten Fahrzeugen.
        :param items: Liste von Datensätzen, wobei jeder Eintrag einer Tabellenzeile entspricht
        """
        self._ui.tableWidget.clear()
        self._ui.tableWidget.setRowCount(0)
        self._ui.tableWidget.setHorizontalHeaderLabels(LABELS)

        for row_data in items:
            row_index: int = self._ui.tableWidget.rowCount()
            self._ui.tableWidget.insertRow(row_index)

            for col_index, value in enumerate(row_data):
                item: QTableWidgetItem = QTableWidgetItem(str(value))
                item.setData(Qt.ItemDataRole.UserRole + col_index, str(value))
                self._ui.tableWidget.setItem(row_index, col_index, item)


    def elapsed_dates(self) -> List[int]:
        """
        Prüft, welche Mietzeiträume abgelaufen sind, und liefert die IDs betroffener Fahrzeuge.
        Diese Methode wird periodisch im Hauptfenster aufgerufen.
        :return: Liste von Fahrzeug-IDs mit abgelaufenen Mietperioden
        """
        table: QTableWidget = self._ui.tableWidget
        results: List[int] = []

        for row_index in range(table.rowCount()):
            item_fz_id: QTableWidgetItem = table.item(row_index, 5)
            item_end_date: QTableWidgetItem = table.item(row_index, 9)

            if item_fz_id and item_end_date:
                end_date: str = item_end_date.text()

                if QDate.currentDate() >= QDate.fromString(end_date, "yyyy-MM-dd"):
                    id_: int = int(item_fz_id.text())
                    #print(id_, QDate.currentDate() , QDate.fromString(end_date, "yyyy-MM-dd"))
                    results.append(id_)

        return results


    @Slot(str)
    def on_search(self, text: str) -> None:
        """
        Sucht in der Tabelle nach dem eingegebenen Text und markiert gefundene Zeilen.
        Die Spalte wird durch den ausgewählten Radiobutton bestimmt.
        :param text: Suchbegriff
        """
        table: QTableWidget = self._ui.tableWidget
        text = text.lower()
        col: int = self._current_radio_button
        table.clearSelection()  # Selection wieder entfernen

        if not text:
            return

        for row in range(table.rowCount()):
            item: QTableWidgetItem = table.item(row, col)
            if not item:
                continue

            match_: bool = text in item.text().lower()
            # table.setRowHidden(row, not match_)
            if match_:
                item.setSelected(True)
                table.scrollToItem(item, QAbstractItemView.ScrollHint.PositionAtCenter)
