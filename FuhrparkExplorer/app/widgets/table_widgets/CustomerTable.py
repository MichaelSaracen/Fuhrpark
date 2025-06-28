from typing import List

from PySide6.QtCore import Slot, Signal, QThreadPool, QPoint, QRegularExpression
from PySide6.QtGui import QAction, Qt
from PySide6.QtWidgets import QTableWidget, QWidget, QHeaderView, QTableWidgetItem, QMenu

from app.core.runnable import UpdateCustomerRunnable, RemoveCustomerRunnable
from app.widgets.delegates import RegexDelegate
from app.widgets.delegates.SpinBoxDelegate import SpinBoxDelegate


class CustomerTable(QTableWidget):
    """
    Tabelle zur Anzeige und Bearbeitung von Kunden-Daten.

    Diese Klasse stellt eine QTableWidget-basierte Ansicht für Kundendaten bereit,
    inklusive inline-Bearbeitung per Delegate, Validierung mittels Regex und SpinBox,
    automatische Speicherung von Änderungen über Datenbank-Prozeduren, und Kontextmenü
    zum Entfernen von Kunden.

    Signale:
        customerUpdated (Signal): Wird gefeuert, wenn eine Kundeänderung oder -löschung abgeschlossen ist.

    Klassenattribute:
        HEADERS (List[str]): Liste der Spaltenüberschriften für die Tabelle.
    """

    customerUpdated: Signal = Signal()

    HEADERS: List[str] = [
        "Kundennummer",
        "Vorname",
        "Nachname",
        "Alter",
        "Telefon",
        "Stadt",
        "PLZ",
        "Strasse",
        "Hausnummer",
        "IBAN",
        "Kreditinstitut",
    ]
    def __init__(self, parent: QWidget=None):
        """
        Initialisiert die Kunden-Tabelle, setzt Header und Delegates sowie Kontextmenü-Policy.
        """
        super().__init__(parent=parent)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.setHorizontalHeaderLabels(self.HEADERS)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_custom_context_menu)
        self.cellChanged.connect(self.on_cell_changed)

        delegate = SpinBoxDelegate(self)
        self.setItemDelegateForColumn(3, delegate)

        validators = {
            1: QRegularExpression(r"[A-Za-z]+(?:\-)?[A-Za-z]+"),    # Vorname
            2: QRegularExpression(r"[A-Za-z]+(?:\-)?[A-Za-z]+"),    # Nachname
            4: QRegularExpression(r"\d{4}/\d{4,8}"),                # Telefon
            5: QRegularExpression(r"[A-Za-z]+(?:\-)?[A-Za-z]+"),    # Stadt
            6: QRegularExpression(r"\d{5}"),                        # PLZ
            7: QRegularExpression(r"[A-Za-z]+(?:\-)?[A-Za-z]+"),    # Strasse
            8: QRegularExpression(r"\d{1,4}[A-Za-z]?"),             # Hausnummer
            9: QRegularExpression(r"[A-Z]{2}\d{8,30}")              # IBAN
        }

        regex_delegate = RegexDelegate(validators, self)
        self.setItemDelegate(regex_delegate)


    @property
    def headers(self) -> List[str]:
        """
        Gibt eine List mit den Headern der Tabelle wieder
        :return:
        """
        return self.HEADERS

    @headers.setter
    def headers(self, headers: List[str]) -> None:
        """
        Setzt neue Spaltenüberschriften.
        :param headers: Liste neuer Header
        """
        self.setHorizontalHeaderLabels(headers)

    @Slot(list)
    def on_add_items(self, customers: List) -> None:
        """
        Befüllt die Tabelle mit Kundendaten und deaktiviert Bearbeitung für ID-Spalte.
        :param customers: Liste von Kundendatensätzen
        """
        self.clear()
        self.setRowCount(len(customers))
        self.blockSignals(True)
        for row_index, row_data in enumerate(customers):
            #self.insertRow(row_index)

            for col_index, col_data in enumerate(row_data):
                item: QTableWidgetItem = QTableWidgetItem(str(col_data))

                if col_index == 0:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

                self.setItem(row_index, col_index, item)

        self.headers = self.HEADERS
        self.blockSignals(False)

    @Slot(int, int)
    def on_cell_changed(self, row: int, col: int) -> None:
        """
        Speichert Änderungen in der Datenbank via UpdateCustomerRunnable.
        :param row: Zeilenindex
        :param col: Spaltenindex
        """
        item: QTableWidgetItem = self.item(row, col)
        if not item:
            return

        id_ = int(self.item(row, 0).text())
        col_name: str = self.__map_to_header(self.HEADERS[col])
        col_name = "alter_" if col_name == "alter" else col_name
        value: str = item.text().strip()

        if not value:
            return

        runnable: UpdateCustomerRunnable = UpdateCustomerRunnable(col_name, id_, value)
        runnable.signals.finished.connect(self.customerUpdated)
        QThreadPool.globalInstance().start(runnable)


    @Slot(QPoint)
    def on_custom_context_menu(self, pos: QPoint) -> None:
        """
        Öffnet Kontextmenü zum Entfernen eines Kunden.
        :param pos: Position des Rechtsklicks
        """
        if not self.currentItem():
            return

        row: int = self.currentItem().row()
        item: QTableWidgetItem = self.item(row , 0)

        if not item:
            return

        id_: int = int(item.text())

        menu: QMenu = QMenu()
        delete_action: QAction = QAction("Kunden entfernen", self)
        delete_action.triggered.connect(lambda : self._customer_removed(id_, row))
        menu.addAction(delete_action)

        menu.exec_(self.viewport().mapToGlobal(pos))


    def _customer_removed(self, id_: int, row: int):
        """
        Entfernt Kunden via RemoveCustomerRunnable und aktualisiert UI.
        :param id_: Kunden-ID
        :param row: Zeile in der Tabelle
        """
        runnable: RemoveCustomerRunnable = RemoveCustomerRunnable(id_)
        runnable.signals.finished.connect(self.customerUpdated)
        QThreadPool.globalInstance().start(runnable)
        self.removeRow(row)
        self.setCurrentItem(None)
        self.clearSelection()


    def search(self, index: int, text: str) -> None:
        """
        Suchfunktion: Markiert und scrollt zur ersten Übereinstimmung in gegebener Spalte.
        :param index: Spaltenindex
        :param text: Suchbegriff
        """
        self.clearSelection()

        if not text.strip():
            return

        for row_index in range(self.rowCount()):
            item: QTableWidgetItem = self.item(row_index, index)
            if not item:
                continue

            item_text: str = item.text().lower()
            if text.lower() in item_text:
                self.scrollToItem(item, QTableWidget.ScrollHint.PositionAtCenter)
                item.setSelected(True)
                break

    # noinspection PyMethodMayBeStatic
    def __map_to_header(self, header: str) -> str:
        new_header: str = header.replace("_", "").lower()
        new_header = "id" if header == "Kundennummer" else new_header
        return new_header





