from PySide6.QtWidgets import QWidget

from app.gui.Ui_DayPrice import Ui_DayPrice


class DayPrice(QWidget):

    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_DayPrice = Ui_DayPrice()
        self._ui.setupUi(self)


    @property
    def tree(self):
        """
        Gibt den DayPriceTree, für die Auflistung der Tagespreise wieder.
        :return: Tagespreis Baumansicht
        """
        return self._ui.dayPriceTree
