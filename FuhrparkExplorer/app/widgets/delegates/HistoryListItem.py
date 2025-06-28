import datetime

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from app.gui.Ui_HistoryListItem import Ui_HistoryListItem


class HistoryListItem(QWidget):
    removed: Signal = Signal(int, int)
    def __init__(
            self,
            row: int,
            id_: int,
            brand: str,
            model: str,
            price: float,
            from_date: datetime.date,
            to_date: datetime.date,
            parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_HistoryListItem = Ui_HistoryListItem()
        self._ui.setupUi(self)

        self._row = row
        self._id_ = id_
        self._brand = brand
        self._model = model
        self._price = price
        self._from_date = from_date
        self._to_date = to_date

        self._ui.lblBrand.setText(brand)
        self._ui.lblModel.setText(model)
        self._ui.lblDateFrom.setText(f"von: {from_date}")
        self._ui.lblDateTo.setText(f"bis: {to_date}")
        self._ui.lblPrice.setText(f"{price:.2f}€")

