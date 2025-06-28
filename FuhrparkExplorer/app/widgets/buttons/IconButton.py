from PySide6.QtCore import Slot, QRect, QSize, Property, Signal, \
    QPropertyAnimation, QMargins
from PySide6.QtGui import QPainter, Qt, QPixmap, QColor, QPen
from PySide6.QtWidgets import QPushButton, QWidget

from app.core import font_metrics_height
from app.core.Theme import Theme


class IconButton(QPushButton):
    backgroundColorChanged: Signal = Signal(QColor)

    _background_color: QColor
    _pixmap: QPixmap | None
    _hovered: bool

    def __init__(self, parent: QWidget=None):
        super().__init__(parent=parent)

        self._pixmap = None
        self._hovered = False
        self._background_color = Theme.button_normal
        self._foreground_color = Theme.foreground

        self._background_color_anim: QPropertyAnimation = QPropertyAnimation(self, b"background_color")
        self._background_color_anim.setDuration(300)
        self._background_color_anim.setStartValue(self._background_color)
        self._background_color_anim.setEndValue(self._background_color)

        self._background_color_anim.valueChanged.connect(self._on_background_color)
        self.toggled.connect(self._update_color)

    def background_color(self) -> QColor:
        return self._background_color

    def set_background_color(self, color: QColor) -> None:
        if self._background_color != color:
            self._background_color = color
            self.backgroundColorChanged.emit(color)
            self.update()

    def paintEvent(self, event, /):
        painter: QPainter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        r: QRect = self.rect()
        painter.fillRect(r, self._background_color)
        painter.setPen(QPen(self._foreground_color, 1))
        painter.setFont(self.font())

        text_height = font_metrics_height(painter)

        text_rect = QRect(0, r.bottom() - text_height - 8, r.width(), text_height)
        painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, self.text())

        if self._pixmap:
            size: QSize = self.iconSize()
            w, h = size.width(), size.height()
            x, y = r.width() // 2 - w // 2, text_rect.top() - h
            icon_rect = QRect(x, y, w, h) if self.text() else self.rect().marginsRemoved(QMargins(4,4,4,4))
            scaled = self._pixmap.scaled(icon_rect.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                         Qt.TransformationMode.SmoothTransformation)
            colored = self.tint_pixmap(scaled, Theme.icon_color)
            painter.drawPixmap(icon_rect, colored)

    def mousePressEvent(self, e, /):
        # wird nicht mehr benötigt für Animation, aber falls du was anderes willst, kannst du erweitern
        super().mousePressEvent(e)

    def enterEvent(self, event, /):
        self._hovered = True
        self._update_color()
        super().enterEvent(event)

    def leaveEvent(self, event, /):
        self._hovered = False
        self._update_color()
        super().leaveEvent(event)

    @Slot(QColor)
    def _on_background_color(self, value: QColor):
        self._background_color = value
        self.update()

    @Slot(bool)
    def _on_toggled(self, _checked: bool) -> None:
        self._update_color()

    def _update_color(self):
        base = Theme.button_normal
        if self.isChecked() and self._hovered:
            target = Theme.button_checked
        elif self.isChecked():
            target = Theme.button_checked
        elif self._hovered:
            target = Theme.button_hover
        else:
            target = base

        self._background_color_anim.stop()
        self._background_color_anim.setStartValue(self._background_color)
        self._background_color_anim.setEndValue(target)
        self._background_color_anim.start()

    def pixmap(self) -> QPixmap:
        return self._pixmap

    def set_pixmap(self, pixmap: QPixmap) -> None:
        if not pixmap.isNull():
            self._pixmap = pixmap
            self.update()

    def tint_pixmap(self, pixmap: QPixmap, color: QColor) -> QPixmap:
        tinted = QPixmap(pixmap.size())
        tinted.fill(Qt.GlobalColor.transparent)
        painter = QPainter(tinted)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(tinted.rect(), color)
        painter.end()
        return tinted

    pixmap = Property(QPixmap, fget=pixmap, fset=set_pixmap)
    background_color = Property(QColor, fget=background_color, fset=set_background_color, notify=backgroundColorChanged)
