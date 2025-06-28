from PySide6.QtGui import QColor


class Theme:
    background: QColor = QColor(30,34,39)
    button_normal: QColor = QColor(240, 240, 240)
    button_hover: QColor = button_normal.darker(110)
    button_checked: QColor = button_hover.darker(110)
    foreground: QColor = QColor(30,34,39)
    icon_color: QColor = QColor(30,34,39)

