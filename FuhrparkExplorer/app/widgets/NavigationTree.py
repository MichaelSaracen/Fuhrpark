from typing import List

from PySide6.QtCore import Slot, Signal, Qt
from PySide6.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QHeaderView

from app.core import DataMapper
from app.gui.Ui_NavigationTree import Ui_NavigationTree


class NavigationTree(QWidget):
    carInformationChanged: Signal = Signal(dict)

    def __init__(self, parent: QWidget = None):
        """
        Initialisiert das Navigationsbaum-Widget und konfiguriert die Spalten und Suchfunktion.
        """
        super().__init__(parent=parent)
        self._ui: Ui_NavigationTree = Ui_NavigationTree()
        self._ui.setupUi(self)

        # Spaltenanzahl und Resize-Verhalten
        self._ui.carTree.setColumnCount(2)
        header = self._ui.carTree.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

        self._ui.leSearch.textChanged.connect(self.on_search)

    @property
    def car_tree(self):
        """
        Liefert die interne QTreeWidget-Instanz für direkte Manipulation.
        :return: QTreeWidget des Navigationsbaums
        """
        return self._ui.carTree

    @Slot(str)
    def on_search(self, text: str) -> None:
        """
        Sucht nach einem Text in allen Modellen und klappt die passende Marke auf.
        :param text: Suchbegriff, der in den Modellnamen gesucht wird
        """
        for i in range(self._ui.carTree.topLevelItemCount()):
            parent_item: QTreeWidgetItem = self._ui.carTree.topLevelItem(i)
            parent_item.setExpanded(False)

            for j in range(parent_item.childCount()):
                child_item: QTreeWidgetItem = parent_item.child(j)
                if text.lower() in child_item.text(0).lower():
                    parent_item.setExpanded(True)
                    self._ui.carTree.setCurrentItem(child_item)
                    self._ui.carTree.scrollToItem(child_item, QTreeWidget.ScrollHint.PositionAtCenter)
                    return

    @Slot(list)
    def on_update_tree(self, row: List) -> None:
        """
        Fügt einen einzelnen Fahrzeugdatensatz dynamisch in den Baum ein.
        Erstellt Marke und Modell, falls nicht vorhanden, und füllt Detail-Knoten.
        :param row: Liste mit Fahrzeugdaten [image, brand, model, fuel, gearbox, power, consumption, doors, seats, color, price]
        """
        image, brand, model, fuel, gearbox, power, consumption, doors, seats, color, price  = row

        details: dict[str, str] = DataMapper.map_car_details(
            "0", image, fuel, gearbox, power, consumption, doors, seats, color, float(price)
        )
        # 1. Marke (Top-Level) suchen
        brand_item: QTreeWidgetItem | None = None
        for i in range(self._ui.carTree.topLevelItemCount()):
            item = self._ui.carTree.topLevelItem(i)
            if item.text(0) == brand:
                brand_item = item
                break

        # 2. Wenn nicht gefunden: neu erstellen
        if brand_item is None:
            brand_item = QTreeWidgetItem([brand])
            self._ui.carTree.addTopLevelItem(brand_item)

        # 3. Modell-Item erstellen
        model_item = QTreeWidgetItem([model])
        d = {brand: {model: details}}
        model_item.setData(0, Qt.ItemDataRole.UserRole, d)
        brand_item.addChild(model_item)

        # 4. Details als Childs hinzufügen
        for key, val in details.items():
            detail_item = QTreeWidgetItem([key, val])
            model_item.addChild(detail_item)

        brand_item.setExpanded(True)

    @Slot(list)
    def load_in_tree(self, data: List):
        """
        Lädt eine komplette Liste von Fahrzeugdatensätzen in den Navigationsbaum.
        Besteht aus Marken als Top-Level und Modellen mit Details als Unterknoten.
        :param data: Liste von Datensätzen, die zu einer Baumstruktur gemappt werden
        """
        self._ui.carTree.clear()
        for brand, models in DataMapper.map_to_tree_structure(data).items():
            brand_item = QTreeWidgetItem([brand])
            self._ui.carTree.addTopLevelItem(brand_item)
            d = {}
            # Fahrzeug Details und Modell setzen
            for model, details in models.items():
                # Modell setzen
                model_item = QTreeWidgetItem([model])
                brand_item.addChild(model_item)

                # DIct für setData (zum herausfiltern bei currentItemChanged)
                d[brand] = {}
                if model not in d[brand]:
                    d[brand].update({model: details})

                model_item.setData(0, Qt.ItemDataRole.UserRole, d)

                # Details setzen
                model_item.addChildren([
                    QTreeWidgetItem([key, val]) for key, val in details.items()
                ])
























