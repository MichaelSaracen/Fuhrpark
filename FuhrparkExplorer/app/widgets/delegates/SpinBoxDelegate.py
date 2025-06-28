from PySide6.QtWidgets import QStyledItemDelegate, QSpinBox, QWidget
from PySide6.QtCore import Qt

class SpinBoxDelegate(QStyledItemDelegate):
    def createEditor(self, parent: QWidget, option, index):
        spin = QSpinBox(parent)
        spin.setRange(18, 99)
        return spin

    def setEditorData(self, editor: QSpinBox, index):
        value = int(index.model().data(index, Qt.ItemDataRole.EditRole))
        editor.setValue(value)

    def setModelData(self, editor: QSpinBox, model, index):
        model.setData(index, editor.value(), Qt.ItemDataRole.EditRole)

    def updateEditorGeometry(self, editor: QWidget, option, index):
        editor.setGeometry(option.rect)
