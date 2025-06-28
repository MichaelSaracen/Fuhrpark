from typing import List

from PySide6.QtCore import Signal, Slot, QRegularExpression
from PySide6.QtGui import Qt, QShortcut, QKeySequence, QRegularExpressionValidator
from PySide6.QtWidgets import QWidget, QLineEdit

from app.core.Utils import all_fields_has_text
from app.gui.Ui_AddCustomerDialog import Ui_AddCustomerDialog


class AddCustomerDialog(QWidget):
    inserted: Signal = Signal(list)
    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_AddCustomerDialog = Ui_AddCustomerDialog()
        self._ui.setupUi(self)

        # add_shadow(self._ui.widget)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.show()

        esc_shortcut: QShortcut = QShortcut(QKeySequence("ESC"), self)
        esc_shortcut.activated.connect(self.close)

        self._ui.leFirstName_2.setValidator(QRegularExpressionValidator(QRegularExpression(r"[A-Za-z]+(?:\-)?[A-Za-z]+")))

        self._fields: List[QLineEdit] = self.findChildren(QLineEdit)
        for field in self._fields:
            field.textChanged.connect(self.on_sender_text_changed)

        self._ui.btnSave.clicked.connect(self.on_saved_clicked)

    @Slot()
    def on_saved_clicked(self):
        texts = [field.text() for field in self._fields]
        f_name, name, age, tel, city, _zip, street, h_num, bank, iban = texts
        self.inserted.emit([f_name, name, age, tel, city, _zip, street, h_num, bank, iban])
        self.close()


    @Slot(str)
    def on_sender_text_changed(self, _text: str) -> None:
        sender = self.sender()
        if isinstance(sender, QLineEdit):
            self._ui.btnSave.setEnabled(all_fields_has_text(self._fields))


