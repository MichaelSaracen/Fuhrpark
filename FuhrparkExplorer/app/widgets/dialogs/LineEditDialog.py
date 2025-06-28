from typing import Any

from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import Qt, QShortcut, QKeySequence
from PySide6.QtWidgets import QWidget, QFileDialog

from app.core import WidgetType, Database, DataMapper
from app.core.Utils import add_shadow
from app.gui.Ui_LineEditDialog import Ui_LineEditDialog


class LineEditDialog(QWidget):
    saved: Signal = Signal(str)
    _old_value: str

    def __init__(self, key: str, old_value: Any, widget_type: WidgetType = WidgetType.LineEdit, parent: QWidget=None):
        super().__init__(parent=parent)
        self._ui: Ui_LineEditDialog = Ui_LineEditDialog()
        self._ui.setupUi(self)

        self.show()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.resize(parent.width(), parent.height())
        add_shadow(self._ui.widget)

        esc_shortcut: QShortcut = QShortcut(QKeySequence("ESC"), self)
        esc_shortcut.activated.connect(self.close)

        self._ui.lblTitle.setText(f"{key} bearbeiten")
        self._old_value = old_value
        self._ui.leOldValue.setText(old_value)

        if widget_type == WidgetType.LineEdit:
            self.show_widgets(line_edit=True)
            self._ui.leNewValue.textChanged.connect(lambda t: self._ui.btnSave.setEnabled(len(t) > 0))
        elif widget_type == WidgetType.ComboBox:
            self.show_widgets(combo_box=True)
            self._ui.btnSave.setEnabled(True)
        elif widget_type == WidgetType.SpinBox:
            self.show_widgets(spin_box=True)
            self._ui.btnSave.setEnabled(True)
        else:
            self.show_widgets(dbl_spin_box=True)
            self._ui.btnSave.setEnabled(True)

        if key == "Getriebe":
            gearboxes = Database.call_procedure("p_get_gearbox")
            self._ui.comboBox.addItems(DataMapper.extract_first_rows(gearboxes[0]))
        if key == "Kraftstoff":
            fuels = Database.call_procedure("p_get_fuel")
            self._ui.comboBox.addItems(DataMapper.extract_first_rows(fuels[0]))

        self._ui.btnLoadImage.setVisible(key == "Bild")

        self._ui.btnSave.clicked.connect(self.on_saved)


        if self._ui.btnLoadImage.isVisible():
            self._ui.btnLoadImage.clicked.connect(self.on_open_file_dialog)

    def show_widgets(
            self, line_edit: bool = False,
            combo_box: bool = False,
            spin_box: bool = False,
            dbl_spin_box: bool = False
    ):
        self._ui.leNewValue.setVisible(line_edit)
        self._ui.comboBox.setVisible(combo_box)
        self._ui.spinBox.setVisible(spin_box)
        self._ui.doubleSpinBox.setVisible(dbl_spin_box)

    @Slot()
    def on_saved(self):
        if self._ui.comboBox.isVisible():
            self.saved.emit(self._ui.comboBox.currentText())
        elif self._ui.spinBox.isVisible():
            self.saved.emit(str(self._ui.spinBox.value()))
        elif self._ui.doubleSpinBox.isVisible():
            self.saved.emit(str(self._ui.doubleSpinBox.value()))
        else:
            self.saved.emit(self._ui.leNewValue.text())
        self.close()

    @Slot()
    def on_open_file_dialog(self):
        path = QFileDialog.getOpenFileName(self, "Bild ersetzen", "", "PNG(*.png)")[0]
        if path:
            self._ui.leNewValue.setText(path)



















