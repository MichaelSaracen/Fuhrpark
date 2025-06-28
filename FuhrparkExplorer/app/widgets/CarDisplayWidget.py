from typing import Dict, Any

from PySide6.QtCore import QRect, QLine, Signal, Property, QPropertyAnimation, Slot, QAbstractAnimation
from PySide6.QtGui import QPixmap, QPainter, Qt, QFont, QColor, QPen
from PySide6.QtWidgets import QWidget

from app.core import DataMapper
from app.core.Utils import font_metrics_width, font_metrics_height, longest_info
from app.widgets.NavigationTree import NavigationTree


class CarDisplayWidget(QWidget):
    dataChanged: Signal = Signal(dict)
    _brand: str
    _details: dict[Any, Any]
    _detail_scale_anim: QPropertyAnimation
    _detail_scale: float
    _model: str
    _navigation_tree: None
    _opacity_anim: QPropertyAnimation
    _pixmap: QPixmap
    _text_color: QColor

    def __init__(self, parent: QWidget = None):
        """
        Initialisiert das Widget zur Anzeige von Fahrzeugbild und Details.
        Setzt Animationen für Detail-Einblendung und Opazität auf.
        """
        super().__init__(parent=parent)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        self._navigation_tree = None
        self._brand = "Audi"
        self._details = {}
        self._model = "A3"
        self._pixmap = QPixmap()
        self._detail_scale = 0.0
        self._opacity = 0.0
        self._text_color = QColor(208,208,208)

        self._detail_scale_anim = QPropertyAnimation(self, b"detail_scale")
        self._detail_scale_anim.setStartValue(0.0)
        self._detail_scale_anim.setEndValue(1.0)
        self._detail_scale_anim.setDuration(300)

        self._opacity_anim = QPropertyAnimation(self, b"opacity")
        self._opacity_anim.setStartValue(0.0)
        self._opacity_anim.setEndValue(1.0)
        self._opacity_anim.setDuration(500)

        self.dataChanged.connect(self.on_data_changed)

    @Slot()
    def on_data_changed(self) -> None:
        """
         Startet Animationen neu, wenn sich die angezeigten Fahrzeugdaten ändern.
         Stoppt laufende Animationen vor Neustart.
         """
        if self._detail_scale_anim.state() == QAbstractAnimation.State.Running:
            self._detail_scale_anim.stop()
            self._opacity_anim.stop()

        self._detail_scale_anim.start()
        self._opacity_anim.start()

    def paintEvent(self, event, /) -> None:
        """
        Überschreibt das Paint-Event, um Marke, Modell, Detail-Infos und Bild zu zeichnen.
        Zeichnet Text, Linien und skaliertes Pixmap gemäß aktuellem Animationsstatus.
        """
        painter: QPainter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setOpacity(self._opacity)

        brand_rect: QRect = self._draw_brand_text(painter)
        brand_text_width: int = font_metrics_width(painter, self._brand)
        model_rect: QRect = self._draw_model_text(painter, brand_rect)
        model_text_width: int = font_metrics_width(painter, f"Modell: {self._model}")
        self._draw_spacer_line(painter, model_rect, brand_text_width, model_text_width)

        content_rect: QRect = self.rect().adjusted(0, model_rect.bottom(), 0, 0)

        info_rect = self._draw_info(painter, model_rect, content_rect)

        car_rect: QRect = self._draw_pixmap(painter, content_rect, info_rect)

    def detail_scale(self) -> float:
        """
        Getter für die Property detail_scale, zurückgegeben wird der aktuelle Skalierungsfaktor.
        """
        return self._detail_scale

    def set_details_scale(self, scale: float) -> None:
        """
        Setter für die Property detail_scale, aktualisiert Wert und löst Neuzeichnen aus.
        :param scale: Neuer Skalierungsfaktor (0.0–1.0)
        """
        if self._detail_scale != scale:
            self._detail_scale = scale
            self.update()
    
    def set_navigation_tree(self, navigation_tree: NavigationTree) -> None:
        self._navigation_tree: NavigationTree = navigation_tree
        self._navigation_tree.car_tree.carInformationChanged.connect(self.set_car_details)
    
    def set_car_details(self, details: Dict[str, Any]) -> None:
        """
        Verknüpft das Navigationsbaum-Widget, um auf Auswahl-Änderungen zu reagieren.
        """
        self._brand = details.get("Marke")
        self._model = details.get("Modell")
        path = details.get("Bild")

        self._details = DataMapper.sort_dict_by_longest_name(details.get("Details"))
        self.set_image(QPixmap(path))
        self.dataChanged.emit(details)
        self.update()

    def set_image(self, image: QPixmap) -> None:
        """
        Setzt das anzuzeigende Fahrzeugbild, sofern gültig, und löst Neuzeichnen aus.
        """
        if image.isNull():
            return
        self._pixmap = image
        self.update()

    def opacity(self) -> float:
        """
        Getter für die Property opacity, liefert aktuellen Opazitätswert.
        """
        return self._opacity

    def set_opacity(self, opacity: float) -> None:
        """
        Setter für die Property opacity, setzt Wert und aktualisiert Ansicht.
        :param opacity: Neuer Opacity-Wert (0.0–1.0)
        """
        if self._opacity != opacity:
            self._opacity = opacity
            self.update()

    def _draw_brand_text(self, painter: QPainter) -> QRect:
        """
        Zeichnet den Markennamen oben zentriert und gibt das Text-Rechteck zurück.
        """
        brand_rect: QRect = QRect(0,0, self.width(), int(self.height() * 0.125))
        painter.setFont(QFont("Roboto", int(brand_rect.height() * 0.5), 600))
        painter.setPen(QPen(QColor(208,208,208, 220)))
        painter.drawText(brand_rect, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom, self._brand)
        return brand_rect

    def _draw_info(self, painter: QPainter, model_rect: QRect, content_rect: QRect) -> QRect:
        """
        Zeichnet die Detail-Box mit Hintergrund und Text für Fahrzeugattribute.
        Nutzt Detail-Scale-Animation zum Einblenden.
        :return: QRect der gezeichneten Info-Box
        """
        painter.save()
        painter.setFont(QFont("Consolas", int(model_rect.height() * 0.35), 400))
        info_height = 0

        for i in range(len(self._details)):
            text_height = font_metrics_height(painter)
            info_height += text_height + 16

        _longest_info = 0
        if self._details:
            _longest_info: int = longest_info(painter, self._details) + 16

        info_rect: QRect = QRect(8, content_rect.center().y() - (info_height - 4) // 2, _longest_info, info_height + 8 )

        info_center_x: int = info_rect.center().x()
        info_center_y: int = info_rect.center().y()
        painter.translate(info_center_x, info_center_y)
        painter.scale(self._detail_scale, self._detail_scale)
        painter.translate(-info_center_x, -info_center_y)

        painter.setBrush(QColor(30, 34, 39, 140))
        painter.drawRoundedRect(info_rect, 4,4)

        start_pos = info_rect.top() + 8
        painter.setPen(QPen(QColor(255, 255, 255)))
        for key, val in self._details.items():
            text = f"{key}: {val}"
            text_width = font_metrics_width(painter, text)
            text_height = font_metrics_height(painter)

            text_rect: QRect = QRect (
                8,
                start_pos,
                text_width + 12,
                text_height + 12
            )
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, text)
            start_pos += text_height + 16
        painter.restore()
        return info_rect

    def _draw_model_text(self, painter: QPainter, brand_rect: QRect) -> QRect:
        """
        Zeichnet den Modellnamen direkt unter der Marke.
        :param brand_rect: QRect des Markentextes
        :return: QRect des Modelltextes
        """
        model_rect: QRect = QRect(0, brand_rect.bottom(), self.width(), int(brand_rect.height() * 0.35))
        painter.setFont(QFont("Consolas", int(model_rect.height() * 0.45), 400))
        painter.setPen(QPen(QColor(208,208,208, 150)))
        painter.drawText(model_rect, Qt.AlignmentFlag.AlignCenter, f"Modell: {self._model}" )
        return model_rect

    def _draw_pixmap(self, painter: QPainter, content_rect, info_rect) -> QRect:
        """
        Zeichnet das Fahrzeugbild neben der Detail-Box, skaliert proportional.
        :return: QRect des Bildbereichs
        """
        if self._pixmap.isNull():
            return QRect(0,0,0,0)

        painter.setPen(QPen(QColor(30, 34, 39, 220)))
        #painter.fillRect(content_rect, Qt.GlobalColor.red)

        car_rect: QRect = QRect(
            info_rect.right(),
            content_rect.top(),
            content_rect.width() - info_rect.width(),
            content_rect.height()
        )
        #painter.fillRect(car_rect, Qt.GlobalColor.green)
        scaled_pixmap = self._pixmap.scaled(
            car_rect.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )

        # Zielrechteck zum Zentrieren im car_rect berechnen
        target_rect = QRect(
            car_rect.center().x() - scaled_pixmap.width() // 2,
            car_rect.center().y() - scaled_pixmap.height() // 2,
            scaled_pixmap.width(),
            scaled_pixmap.height()
        )

        painter.drawPixmap(target_rect, scaled_pixmap)
        return car_rect

    # noinspection PyMethodMayBeStatic
    def _draw_spacer_line(self, painter: QPainter, model_rect: QRect, brand_text_width: int, model_text_width: int):
        max_text_width: int = max(model_text_width, brand_text_width)
        line: QLine = QLine(
            model_rect.center().x() - (max_text_width // 2) - 10,
            model_rect.top() - 2,
            model_rect.center().x()  + (max_text_width // 2) + 10 ,
            model_rect.top() - 2
        )
        painter.setPen(QPen(QColor(30, 34, 39, 100)))
        painter.drawLine(line)

    detail_scale = Property(float, fget=detail_scale, fset=set_details_scale)
    opacity = Property(float, fget=opacity, fset=set_opacity)


















