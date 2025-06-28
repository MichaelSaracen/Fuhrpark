from typing import List

from PySide6.QtCore import Slot
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QWidget

from app.core import add_shadow
from app.gui.Ui_Statistic import Ui_Statistic


class Statistic(QWidget):

    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_Statistic = Ui_Statistic()
        self._ui.setupUi(self)

        add_shadow(self._ui.widget)

        self._ui.pieChart.title = "Verfügbarkeit"
        self._ui.pieChart.slice_colors = [QColor(229, 95,96), QColor(225, 229, 83), QColor(204, 229, 169)]

    @property
    def bar_char (self):
        """
        gibt den BarChart wieder.
        :return:
        """
        return self._ui.barChart

    @Slot(list)
    def on_load_statistic(self, data: List) -> None:
        """
        Lädt in das Barchart die Marken, die am häufigsten vermietet werden.
        :param data:
        :return:
        """
        brands: list = []
        values: list = []
        for t in data:
            if isinstance(t, tuple):
                brands.append(t[0])
                values.append(t[1])

        self.bar_char.set_categories(brands)
        self.bar_char.set_values(values)

    @Slot(list)
    def on_load_statistic_model(self, data: List) -> None:
        """
        Lädt in das BarChart die Modelle, die am häufigsten vermietet werden.
        :param data:
        :return:
        """
        models: list = []
        values: list = []
        for t in data:
            if isinstance(t, tuple):
                models.append(t[0])
                values.append(t[1])

        self._ui.barChart_2.set_categories(models)
        self._ui.barChart_2.set_values(values)


    @Slot(int, int, int)
    def on_status_count_changed(self, available: int, reserved: int, in_repair: int) -> None:
        """
        Aktualisiert den PieChart mit den hinzugefügten Werten.
        :param available:
        :param reserved:
        :param in_repair:
        :return:
        """
        self._ui.pieChart.set_entries({
            "verfügbar": available ,
            "vermietet": reserved ,
            "in Reparatur": in_repair
        })