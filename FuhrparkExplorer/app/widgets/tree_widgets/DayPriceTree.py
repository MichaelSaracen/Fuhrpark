from typing import Dict

from PySide6.QtCore import Slot, Qt, Signal, QPoint, QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QMenu, QInputDialog, QLineEdit

from app.core import DataMapper, Database
from app.widgets.delegates.TreePriceWidget import TreePriceWidget


class DayPriceTree(QTreeWidget):
    """
    Widget zur Anzeige und Verwaltung von Tagespreisen.

    Dieses Tree-Widget lädt Tagespreise aus der Datenbank, zeigt sie hierarchisch nach Marken und Modellen an
    und ermöglicht das Hinzufügen sowie Bearbeiten von Preisen über Kontextmenüs und Dialoge.

    Signale:
        dataAdded (Signal): Gefeuert, sobald ein neuer Preis hinzugefügt wurde.
        priceChanged (Signal): Gefeuert bei Preisänderung mit Parametern (brand, model, new_price).

    Attribute:
        _price_dict (dict[str, dict[str, float]]): Verschachteltes Dictionary mit Marken, Modellen und ihren Preisen.
    """
    dataAdded: Signal = Signal()
    priceChanged: Signal = Signal(str, str, float)

    _price_dict: dict[str, dict[str, float]]
    def __init__(self, parent: QWidget=None):
        """
        Initialisiert das DayPriceTree und setzt Kontextmenü-Policy.
        """
        super().__init__(parent=parent)

        self._price_dict = {}

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

        # self.currentItemChanged.connect(self.on_current_item_changed)
        #self.on_load_day_prices()

    @property
    def price_dict(self) -> dict:
        """
        Liefert das interne Preis-Dictionary mit Marken und Modellpreisen.
        :return: Verschachteltes Dictionary
        """
        return self._price_dict



    @Slot(list)
    def on_load_day_prices(self, rows) -> None:
        """
        Lädt die Tagespreise aus der Datenbank und fügt diese dem DayPriceTree hinzu.\n

        Das ModelItem setzt die Daten mit:\n
            model_item.setData(0, Qt.ItemDataRole.UserRole, brand)\n
            model_item.setData(0, Qt.ItemDataRole.UserRole + 1, model)\n
            model_item.setData(0, Qt.ItemDataRole.UserRole + 2, price)\n

        Diese können dann später, beim Drücken des Items abgerufen werden.
        :return:
        """
        #rows = Database.call_procedure("p_get_fahrzeug_tagespreis")[0]
        self._price_dict: Dict[str, Dict[str, float]] = DataMapper.map_to_nested_price_dict(rows)
        self.__reload_tree()

    def __reload_tree(self):
        self.clear()
        for brand, values in self._price_dict.items():
            brand_item: QTreeWidgetItem = QTreeWidgetItem([brand])
            self.addTopLevelItem(brand_item)
            for model, price in values.items():
                self.__add_model_item(brand_item, brand, model, price)
        self.expandAll()

    @Slot(str, str, float)
    def on_day_price_added(self, brand: str, model: str, price: float) -> None:
        """
        Fügt einen neuen Tagespreis hinzu oder aktualisiert bestehenden Preis und feuert dataAdded.
        :param brand: Markenname
        :param model: Modellbezeichnung
        :param price: Neuer Tagespreis
        """
        self.clear()

        l = [(brand, model, price)]
        if brand in self._price_dict:
            self._price_dict[brand].update({model: price})
        else:
            self._price_dict.update(DataMapper.map_to_nested_price_dict(l))
        self.__reload_tree()

        self.dataAdded.emit()


    def __add_model_item(self, brand_item: QTreeWidgetItem, brand: str, model: str, price: float) -> None:
        """
        Hilfsmethode zum Hinzufügen eines Modell-Eintrags mit zugehörigem Widget.
        :param brand_item: Parent-Item für die Marke
        :param brand: Markenname
        :param model: Modellbezeichnung
        :param price: Tagespreis
        """
        model_item: QTreeWidgetItem = QTreeWidgetItem()
        model_item.setData(0, Qt.ItemDataRole.UserRole, brand)
        model_item.setData(0, Qt.ItemDataRole.UserRole + 1, model)
        model_item.setData(0, Qt.ItemDataRole.UserRole + 2, price)
        brand_item.addChild(model_item)

        widget: TreePriceWidget = TreePriceWidget(model, price, self)
        model_item.setSizeHint(0, QSize( widget.sizeHint().width(), 24) )
        self.setItemWidget(model_item, 0, widget)

    @Slot(QPoint)
    def on_context_menu(self, pos: QPoint) -> None:
        """
        Öffnet ein Kontextmenü zur Bearbeitung des Preises für das ausgewählte Modell.
        :param pos: Klickposition
        """
        item: QTreeWidgetItem = self.itemAt(pos)

        if not item or not item.parent():
            return

        model: str = item.data(0, Qt.ItemDataRole.UserRole + 1)
        menu: QMenu = QMenu()
        edit_action: QAction = QAction(f"Preis von {model} ändern", self)
        edit_action.triggered.connect(self.on_edit_price)
        menu.addAction(edit_action)

        menu.exec(self.viewport().mapToGlobal(pos))


    @Slot()
    def on_edit_price(self) -> None:
        """
        Öffnet Dialog zur Preisänderung und aktualisiert Datenbank sowie UI bei Bestätigung.
        """
        item: QTreeWidgetItem = self.currentItem()
        if not item:
            return

        brand: str = item.data(0, Qt.ItemDataRole.UserRole)
        model: str = item.data(0, Qt.ItemDataRole.UserRole + 1)
        price: str = str(item.data(0, Qt.ItemDataRole.UserRole + 2))

        text, ok = QInputDialog.getText(
            self,
            "Preis ändern",
            f"Möchtest du den Preis von {brand} {model} ändern?",
            QLineEdit.EchoMode.Normal,
            price
        )

        if ok:
            Database.call_procedure("p_update_tagespreis", (model, text), commit=True)
            self.priceChanged.emit(brand, model, float(text))
            item.setData(0, Qt.ItemDataRole.UserRole + 2, float(text))
            widget: TreePriceWidget = self.itemWidget(item, 0)
            widget.price = float(text)

