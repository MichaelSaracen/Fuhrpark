from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import Qt, QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget

from app.core.Utils import add_shadow
from app.gui.Ui_SimpleDialog import Ui_SimpleDialog


class SimpleDialog(QWidget):
    ok: Signal = Signal()

    def __init__(self, title: str, details: str, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_SimpleDialog = Ui_SimpleDialog()
        self._ui.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.resize(parent.width(), parent.height())
        add_shadow(self._ui.widget)
        self.show()

        esc_shortcut: QShortcut = QShortcut(QKeySequence("ESC"), self)
        esc_shortcut.activated.connect(self.close)

        self._ui.lblTitle.setText(title)
        self._ui.lblDetails.setText(details)

        self._ui.btnOk.clicked.connect(self.on_ok)

    def show_buttons(self, show: bool=True) -> None:
        self._ui.btnOk.setVisible(show)
        self._ui.pushButton_2.setVisible(show)

    @Slot()
    def on_ok(self):
        self.ok.emit()