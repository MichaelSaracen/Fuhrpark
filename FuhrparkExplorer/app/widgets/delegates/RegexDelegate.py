from PySide6.QtWidgets import QStyledItemDelegate, QLineEdit, QWidget
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression, Qt


class RegexDelegate(QStyledItemDelegate):
    def __init__(self, validators: dict[int, QRegularExpression], parent: QWidget = None):
        super().__init__(parent)

        self._validators = validators

    def createEditor(self, parent, option, index, /):
        editor = QLineEdit(parent)
        regex = self._validators.get(index.column())
        if regex:
            validator = QRegularExpressionValidator(regex, parent)
            editor.setValidator(validator)
        return editor

    def setEditorData(self, editor: QLineEdit, index, /):
        editor.setText(index.model().data(index, Qt.ItemDataRole.EditRole))

    def setModelData(self, editor: QLineEdit, model, index, /):
        model.setData(index, editor.text(), Qt.ItemDataRole.EditRole)

    def updateEditorGeometry(self, editor: QLineEdit, option, index, /):
        editor.setGeometry(option.rect)