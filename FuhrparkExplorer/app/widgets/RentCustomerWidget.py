from typing import List, Any

from PySide6.QtCore import QSize, Qt, Slot, Signal
from PySide6.QtWidgets import QWidget, QListWidgetItem, QRadioButton

from app.core import DataMapper
from app.gui.Ui_RentCustomerWidget import Ui_RentCustomerWidget
from app.widgets.delegates import CustomerListItem


class RentCustomerWidget(QWidget):
    customerDataRequested: Signal = Signal(list)
    customerIDSelected: Signal = Signal(int)
    def __init__(self, parent: QWidget=None):
        """
        Initialisiert das Kunden-Widget für die Vermietung und verbindet UI-Elemente mit Slots.
        """
        super().__init__(parent=parent)
        self._ui: Ui_RentCustomerWidget = Ui_RentCustomerWidget()
        self._ui.setupUi(self)

        self._ui.listWidget.itemClicked.connect(self.on_item_clicked)
        self._ui.lineEdit.textChanged.connect(self.on_search_changed)

    @Slot(list)
    def on_add_items(self, items: List[Any]) -> None:
        """
        Fügt neue Kunden-Datensätze in das ListWidget ein.
        Jeder Datensatz wird als CustomerListItem dargestellt.
        :param items: Liste von Kunden-Daten, jede Zeile enthält [id, vorname, nachname, ...]
        """
        self._ui.listWidget.clear()

        for i, row in enumerate(items):
            id_, f_name, name, age, tel, city, zip_, street, h_num, bank, iban = row

            item: QListWidgetItem = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, [id_, f_name, name, age, tel, city, zip_, street, h_num, bank, iban])
            widget: CustomerListItem = CustomerListItem(row=i, id_=id_, first_name=f_name, last_name=name, telephone=tel)

            item.setSizeHint(QSize(widget.sizeHint().width(), 24))

            self._ui.listWidget.addItem(item)
            self._ui.listWidget.setItemWidget(item, widget)

    @Slot(QListWidgetItem)
    def on_item_clicked(self, item: QListWidgetItem) -> None:
        """
        Reagiert auf Klicks in der Liste und sendet ausgewählte Kundendaten über Signale.
        :param item: das angeklickte ListWidgetItem
        """
        data: List = item.data(Qt.ItemDataRole.UserRole)
        if data:
            self.customerDataRequested.emit(data)
            self.customerIDSelected.emit(int(data[0]))

    @Slot(str)
    def on_search_changed(self, text: str) -> None:
        """
        Filtert das ListWidget basierend auf der Sucheingabe und dem ausgewählten Kriterium.
        :param text: Suchbegriff
        """
        for i in range(self._ui.listWidget.count()):
            item: QListWidgetItem = self._ui.listWidget.item(i)
            mapped = DataMapper.map_customer_data_to_dict(item.data(Qt.ItemDataRole.UserRole))
            firstname = mapped.get(self.selected_radio_text())
            _match = text.lower() in firstname.lower()
            item.setHidden(not _match)

    def selected_radio_text(self) -> str:
        """
        Gibt den Text des aktuell ausgewählten Radiobuttons zurück, um das Suchkriterium zu bestimmen.
        :return: Text des ausgewählten Radiobuttons
        """
        return list(filter(lambda rb: rb.isChecked(), self.findChildren(QRadioButton)))[0].text()




