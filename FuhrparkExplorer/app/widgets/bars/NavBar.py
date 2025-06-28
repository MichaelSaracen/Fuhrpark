from typing import List

from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QButtonGroup, QPushButton

from app.gui.Ui_NavBar import Ui_NavBar


class NavBar(QWidget):
    currentIndexChanged: Signal = Signal(int)
    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_NavBar = Ui_NavBar()
        self._ui.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        self._current_index: int = 0
        self._buttons: List[QPushButton] = self.findChildren(QPushButton)

        self._button_group: QButtonGroup = QButtonGroup(self)

        for i, btn in enumerate(self._buttons):
            self._button_group.addButton(btn, i)

        self._button_group.idClicked.connect(self.set_current_index)
        self.currentIndexChanged.connect(self._on_index_changed)

        self.set_current_index(0)
        self._on_index_changed(0)

    def set_current_index(self, index: int) -> None:
        if self._current_index != index:
            self._current_index = index
            self.currentIndexChanged.emit(index)

    @Slot(int)
    def _on_index_changed(self, index: int):
        sender = self._button_group.button(index)
        sender.click()





