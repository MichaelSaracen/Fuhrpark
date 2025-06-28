from PySide6.QtWidgets import QWidget

from app.gui.Ui_CarStatus import Ui_CarStatus
from app.core import add_shadow


class CarStatus(QWidget):

    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_CarStatus = Ui_CarStatus()
        self._ui.setupUi(self)

        add_shadow(self._ui.widget)

    @property
    def tree(self):
        """
        Gibt die Baumansicht mit den Fahrzeug-Status wieder.
        :return:
        """
        return self._ui.carStatusTree


