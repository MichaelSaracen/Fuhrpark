from typing import Dict, Callable, Any

from PySide6.QtCore import Slot, Signal, Qt, QPoint
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QMenu

from app.core import DataMapper, Database, WidgetType, TreeTools
from app.core.Utils import find_parent_by_name
from app.widgets.dialogs.LineEditDialog import LineEditDialog
from app.widgets.dialogs.SimpleDialog import SimpleDialog


class CarTree(QTreeWidget):
    carInformationChanged: Signal = Signal(dict)
    carRemoved: Signal = Signal(str)

    def __init__(self, parent: QWidget=None):
        """
        Initialisiert den Fahrzeug-Baum mit Kontextmenü und Verknüpfung der relevanten Signale.
        """
        super().__init__(parent=parent)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu_open)

        self.currentItemChanged.connect(self.on_current_item_changed)
        self.carRemoved.connect(self.on_car_removed)

    @Slot(QPoint)
    def on_context_menu_open(self, position: QPoint) -> None:
        """
        Öffnet das Kontextmenü zum Bearbeiten oder Löschen von Baumknoten.
        :param position: Klick-Position relativ zum Widget
        """
        item: QTreeWidgetItem = self.itemAt(position)

        if not item:
            return

        key = item.text(0)
        value = item.text(1) if self.columnCount() > 1 else ""

        menu: QMenu = QMenu(self)

        if not value and item.parent() is not None:
            delete_action: QAction = QAction(f"{key} löschen", self)
            delete_action.triggered.connect(lambda k=key: self.on_delete_car(key))
            menu.addAction(delete_action)
        # wenn val vorhanden, dann die Edit-Funktionalität setzen
        if value:
            self.__edit_action(menu, item, key, value)

        menu.exec(self.viewport().mapToGlobal(position))

    def _line_edit_dialog(self, key: str, old_value, widget_type: WidgetType, callback: Callable) -> None:
        """
        Öffnet einen Dialog zur Bearbeitung eines Knoteneintrags.
        :param key: Bezeichner des zu ändernden Attributes
        :param old_value: Aktueller Wert als Ausgangsbasis
        :param widget_type: Typ des Eingabe-Widgets im Dialog
        :param callback: Funktion, die bei Speichern aufgerufen wird
        """
        mw = find_parent_by_name(self, "MainWindow")
        dialog: LineEditDialog = LineEditDialog(key, old_value, widget_type, mw)
        dialog.saved.connect(callback)
        mw.sizeChanged.connect(dialog.resize)

    def on_line_edit_changed(self, key: str, old_value, widget_type: WidgetType, proc_name: str, model_name: str, item: QTreeWidgetItem) -> None:
        """
        Slot für die Initialisierung des Edit-Dialogs mit passender Datenbankprozedur.
        :param key: Name des Felds
        :param old_value: Alter Wert
        :param widget_type: Eingabetyp
        :param proc_name: Name der DB-Prozedur zum Update
        :param model_name: Modellbezeichnung
        :param item: TreeWidgetItem, das aktualisiert wird
        """
        self._line_edit_dialog(
            key,
            old_value,
            widget_type,
            lambda new_val: self._update_item_and_db(proc_name, new_val, model_name, item)
        )

    def _update_item_and_db(self, proc_name: str, new_val: Any, model_name: str, item: QTreeWidgetItem) -> None:
        """
        Führt die DB-Prozedur aus und aktualisiert den Baumknoten-Text und Daten.
        :param proc_name: Name der Datenbank-Prozedur
        :param new_val: Neuer Wert
        :param model_name: Modellname
        :param item: Das geänderte TreeWidgetItem
        """
        Database.call_procedure(proc_name, [model_name, new_val], commit=True)

        # Suffix basierend auf Prozedur
        suffix = "L" if proc_name == "p_update_verbrauch" \
            else "PS" if proc_name == "p_update_leistung" \
            else "€" if proc_name == "p_update_grundpreis" \
            else ""

        item.setText(1, str(new_val) + suffix)
        model_item: QTreeWidgetItem = item.parent()
        if not model_item:
            return

        # Daten-Dict holen
        data: Dict = model_item.data(0, Qt.ItemDataRole.UserRole)
        if not data:
            return

        brand = next(iter(data))
        model = next(iter(data[brand]))
        details = data[brand][model]

        details[item.text(0)] = str(new_val) + suffix

        model_item.setData(0, Qt.ItemDataRole.UserRole, data)

        self.on_current_item_changed(model_item, None)

    @Slot(str)
    def on_delete_car(self, car: str) -> None:
        """
        Öffnet einen Lösch-Dialog und entfernt bei Bestätigung das Fahrzeug.
        :param car: Modellname des Fahrzeugs
        """
        mw = find_parent_by_name(self, "MainWindow")
        if not mw:
            return
        dialog: SimpleDialog = SimpleDialog(
            "Fahrzeug entfernen",
            f"Möchtest du wirklich **{car}** entfernen? Das Fahrzeug wird somit **unwiderruflich** entfernt!",
            mw
        )
        mw.sizeChanged.connect(dialog.resize)
        dialog.ok.connect(lambda c=car: (self.remove_car(c), dialog.close()))

    def remove_car(self, car: str) -> None:
        """
        Entfernt das Fahrzeug aus der Datenbank mit der Prozedur: **p_delete_fahrzeug_by_modell**
        :param car:
        :return:
        """
        Database.call_procedure("p_delete_fahrzeug_by_modell", [car], commit=True)
        self.carRemoved.emit(car)

    @Slot(str)
    def on_car_removed(self, car: str) -> None:
        """
        Aktualisiert den Baum nach dem Entfernen eines Fahrzeugs.
        :param car: Modellname des entfernten Fahrzeugs
        """
        TreeTools.check_removed_car(self, car, self.carRemoved.emit, car)

    @Slot(QTreeWidgetItem, QTreeWidgetItem)
    def on_current_item_changed(self, current: QTreeWidgetItem, _previous: QTreeWidgetItem) -> None:
        """
        Slot, der auf Änderungen der Auswahl reagiert und Fahrzeuginformationen sendet.
        :param current: Aktuelles Item
        :param _previous: Vorheriges Item (unbenutzt)
        """
        if not current:
            return

        if current.parent() is not None and current.childCount() > 0:
            data = current.data(0, Qt.ItemDataRole.UserRole)
            converted: Dict = DataMapper.convert_tree_structure_to_view(data)
            if converted:
                self.carInformationChanged.emit(converted)

    def __edit_action(self, menu, item, key, value):
        """
        Fügt dem Kontextmenü Edit-Aktionen für Fahrzeugdetails hinzu.
        :param menu: Kontextmenü
        :param item: Das bearbeitete TreeWidgetItem
        :param key: Name des Feldes
        :param value: Aktueller Wert
        """
        edit_action: QAction = QAction(f"{key} {value} bearbeiten", self)
        model_name = item.parent().text(0)

        match key:
            case "Getriebe":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.ComboBox, "p_update_getriebe", model_name,
                                                      item)
                )
            case "Kraftstoff":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.ComboBox, "p_update_kraftstoff", model_name,
                                                      item)
                )
            case "Leistung":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.SpinBox, "p_update_leistung", model_name,
                                                      item)
                )
            case "Verbrauch":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.SpinBox, "p_update_verbrauch", model_name,
                                                      item)
                )
            case "Türen":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.SpinBox, "p_update_tueren", model_name,
                                                      item)
                )
            case "Sitze":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.SpinBox, "p_update_sitze", model_name,
                                                      item)
                )
            case "Farbe":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.LineEdit, "p_update_farbe", model_name,
                                                      item)
                )
            case "Grundpreis":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.DoubleSpinBox, "p_update_grundpreis", model_name,
                                                      item)
                )
            case "Bild":
                edit_action.triggered.connect(
                    lambda: self.on_line_edit_changed(key, value, WidgetType.LineEdit, "p_update_bild", model_name,
                                                      item)
                )
            case _:
                pass

        menu.addAction(edit_action)