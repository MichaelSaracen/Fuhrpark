from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QListWidgetItem

from app.core import add_shadow
from app.gui.Ui_History import Ui_History
from app.widgets.delegates import HistoryListItem


class History(QWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_History = Ui_History()
        self._ui.setupUi(self)
        add_shadow(self._ui.widget)

    @Slot(list)
    def on_load_history(self, history_data: list) -> None:
        """
        Empfängt die Historie aus der Datenbank und bindet diese in das ListWidget ein.
        :param history_data:
        """
        if not history_data:
            return

        for index, data in enumerate(history_data):
            # (1, 'Honda', 'Civic', Decimal('225.00'), datetime.date(2025, 6, 15), datetime.date(2025, 6, 19))
            (id_, brand, model, price, d_from, d_to) = data
            item: QListWidgetItem = QListWidgetItem()
            widget: HistoryListItem = HistoryListItem(index, id_, brand, model, price, d_from, d_to)
            item.setSizeHint(widget.sizeHint())
            self._ui.listWidget.addItem(item)
            self._ui.listWidget.setItemWidget(item, widget)