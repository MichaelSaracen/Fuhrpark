from PySide6.QtWidgets import QWidget

from app.gui.Ui_CustomerListItem import Ui_CustomerListItem


class CustomerListItem(QWidget):

    def __init__(self, row: int, id_: int,  first_name: str, last_name: str, telephone: str, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_CustomerListItem = Ui_CustomerListItem()
        self._ui.setupUi(self)
        self.setFixedHeight(40)

        self._id = id_
        self._row = row

        self._ui.lblFirstname.setText(first_name)
        self._ui.lblLastname.setText(last_name)
        self._ui.lblPhone.setText(telephone)




