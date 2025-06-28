from typing import List

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QTableWidget, QRadioButton

from app.core import add_shadow
from app.gui.Ui_Customers import Ui_Customers
from app.widgets.table_widgets.CustomerTable import CustomerTable


class Customers(QWidget):
    """
    Widget zur Verwaltung und Anzeige von Kunden in einer Tabelle.

    Bietet Funktionen zum Aktivieren/Deaktivieren der Editierbarkeit und zur Suche
    über ein Suchfeld und Radiobuttons zur Auswahl der Suchspalte.
    """

    def __init__(self, parent: QWidget=None):
        """
        Initialisiert das Kunden-Widget, verbindet Buttons und Suchfeld mit Slots
        und fügt Schatten-Effekt hinzu.
        """
        super().__init__(parent=parent)
        self._ui: Ui_Customers = Ui_Customers()
        self._ui.setupUi(self)

        add_shadow(self._ui.widget_3)

        self._ui.btnEdit.clicked.connect(self.on_edit_changed)
        self._ui.leSearch.textChanged.connect(self.on_search)

    @property
    def search_index(self) -> int:
        """
        Ermittelt den Index der aktiven Suchspalte anhand der ausgewählten Radiobuttons.
        :return: Spaltenindex für die Suche
        """
        headers: List[str] = self.table.headers
        rbs: List[QRadioButton] = self.findChildren(QRadioButton)
        index: int = next((headers.index(rb.text()) for rb in rbs if rb.isChecked()), 0)
        return index


    @property
    def table(self) -> CustomerTable:
        """
        Liefert die Tabelle zur Kundenanzeige.
        :return: Instanz von CustomerTable
        """
        return self._ui.tableWidget

    @Slot(bool)
    def on_edit_changed(self, arg: bool) -> None:
        """
        Schaltet die Editierbarkeit der Tabelle um.
        :param arg: True aktiviert Editiermodus, False deaktiviert
        """
        trigger = QTableWidget.EditTrigger.NoEditTriggers if not arg else QTableWidget.EditTrigger.AllEditTriggers
        self.table.setEditTriggers(trigger)

    @Slot(str)
    def on_search(self, text) -> None:
        """
        Führt eine Suche in der Tabelle durch und filtert Einträge entsprechend.
        :param text: Suchbegriff
        """
        self.table.search(self.search_index, text)

    def resizeEvent(self, event, /):
        """
        Passt die Breite des linken Widgets an die Breite des rechten Widgets an.
        Wird bei jeder Fenstergrößenänderung aufgerufen.
        :param event: Resize-Event
        """
        self._ui.widget.setFixedWidth(self._ui.widget_2.width())

