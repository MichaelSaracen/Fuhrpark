from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from app.gui.Ui_TreePriceWidget import Ui_TreePriceWidget


class TreePriceWidget(QWidget):

    priceChanged: Signal = Signal(float)
    def __init__(self, model: str, price: float, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_TreePriceWidget = Ui_TreePriceWidget()
        self._ui.setupUi(self)
        self.setFixedHeight(32)
        self._ui.lblModel.setText(model)
        self._ui.lblPrice.setText(f"{price:.2f}")

    @property
    def price(self) -> float:
        """
        Gibt den Tagespreis wieder.
        :return: float
        """
        return float(self._ui.lblPrice.text())

    @price.setter
    def price(self, price: float) -> None:
        """
        Setzt den Tagespreis für den Verleih des Fahrzeugs.
        :param price:
        :return:
        """
        if float(self._ui.lblPrice.text()) != price:
            self._ui.lblPrice.setText(f"{price:.2f}")

