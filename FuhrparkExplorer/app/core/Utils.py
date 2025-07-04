import math
import os
from typing import Dict

from PySide6.QtCore import QPointF, QRect, QPoint
from PySide6.QtGui import QPainter, QFontMetrics, QLinearGradient, QColor
from PySide6.QtWidgets import QTreeWidgetItem, QWidget, QGraphicsDropShadowEffect
from cryptography.fernet import Fernet
from dotenv import load_dotenv

__all__ = [
    "populate_tree",
    "font_metrics_height",
    "font_metrics_width",
    "add_shadow",
    "longest_info",
    "find_parent_by_name",
    "get_db_config",
    "font_metrics",
    "sort_by_type",
    "longest_name",
    "percentages_from_values",
    "point_on_circle",
    "all_fields_has_text"
]


load_dotenv()  # Lädt Variablen aus .env

def get_db_config():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    name = os.getenv("DB_NAME")
    encrypted_password = os.getenv("DB_PASSWORD_ENC")

    # Lade Key sicher (z. B. aus Datei, Eingabe, Umgebung)
    with open("secret.key", "rb") as f:
        key = f.read()

    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()

    return {
        "host": host,
        "user": user,
        "password": decrypted_password,
        "database": name
    }

def all_fields_has_text(fields) -> bool:
    """
    Überprüft, ob die Textfelder Inhalt besitzen.
    :return:
    """
    return all([field.text() for field in fields])



def add_shadow(widget: QWidget):
    shadow: QGraphicsDropShadowEffect = QGraphicsDropShadowEffect(
        widget,
        offset=QPointF(0,0),
        blurRadius=20
    )
    widget.setGraphicsEffect(shadow)

def longest_info(painter: QPainter, d: Dict) -> int:
    return max([font_metrics_width(painter, key + ": " + val) for key, val in d.items() ])

def find_parent_by_name(start_widget: QWidget, object_name: str):
    ancestor: QWidget = start_widget.parent()
    while ancestor and ancestor.objectName() != object_name:
        ancestor = ancestor.parent()
    return ancestor

def font_metrics_width(painter: QPainter, text: str) -> int:
    metrics: QFontMetrics = painter.fontMetrics()
    return metrics.horizontalAdvance(text)

def font_metrics_height(painter: QPainter) -> int:
    metrics: QFontMetrics = painter.fontMetrics()
    return metrics.height()

def font_metrics(painter: QPainter, text: str):
    metrics: QFontMetrics = painter.fontMetrics()
    h: int = metrics.height()
    w: int = metrics.horizontalAdvance(text)
    return w, h

def linear_gradient(painter: QPainter, base_color: QColor, rect: QRect) -> None:
    lg: QLinearGradient = QLinearGradient(
        QPointF(rect.center().x(), rect.bottom()),
        QPointF(rect.center().x(), rect.top())
    )
    lg.setColorAt(0, base_color.lighter(200))
    lg.setColorAt(1, base_color.darker(200))
    painter.setBrush(lg)

def longest_name(entries: Dict[str, float]) -> str:
    return max(list(entries.keys()), key=len)

def percentages_from_values(values: Dict[str, float]) -> Dict[str, float]:
    """
    Rechnet die Werte aus der Liste in Prozente um, und gibt diese als neue Liste
    mit Fließkommazahlen wieder.
    Summiert ergibt das Resultat immer **100%**
    :param values:
    :return:
    """
    _total: int = sum(values.values())
    try:
        return {k: (v / _total) * 100 for k, v in values.items()}
    except ZeroDivisionError:
        pass

def point_on_circle(center: QPoint, angle: float, size: int, distance: float=0.5):
    radians = math.radians(-angle)
    radius = size / 2 * distance
    x = center.x() + math.cos(radians) * radius
    y = center.y() + math.sin(radians) * radius
    return QPoint(x, y)

def sort_by_type(entries: Dict[str, float], sort_type: "SortType", /) -> Dict[str, float]:
    """
    Filtert den **SortType**
    :param entries:
    :param sort_type:
    :return:
    """
    if not entries:
        return dict()

    match sort_type:
        case sort_type.LowestValue:
            return dict(sorted(entries.items(), key=lambda it: it[1], reverse=False))
        case sort_type.HighestValue:
            return dict(sorted(entries.items(), key=lambda it: it[1], reverse=True))
        case sort_type.NameAsc:
            return dict(sorted(entries.items(), key=lambda it: it[0], reverse=False))
        case sort_type.NameDesc:
            return dict(sorted(entries.items(), key=lambda it: it[0], reverse=True))
        case sort_type.NameLength:
            return dict(sorted(entries.items(), key=lambda it: (len(it[0]), it[0]), reverse=True))
    return dict()

def vertical_slice_span(center: QPoint, size: int, start_angle: float, span_angle: float) -> float:
    """
    Gibt den maximalen vertikalen Abstand zwischen den beiden Slice-Kanten (Start/Ende).
    """
    r = size / 2

    # Punkt auf dem äußeren Kreis für Start- und Endwinkel berechnen
    start_rad = math.radians(-start_angle)
    end_rad = math.radians(-(start_angle + span_angle))

    y1 = center.y() + math.sin(start_rad) * r
    y2 = center.y() + math.sin(end_rad) * r

    return abs(y2 - y1)

def populate_tree(parent_item: QTreeWidgetItem, data: Dict) -> None:
    """
    Fügt einem gegebenen QTreeWidgetItem rekursiv untergeordnete Elemente hinzu,
    basierend auf einer verschachtelten Dictionary- oder Listenstruktur.

    Diese Methode eignet sich für beliebig tiefe Datenstrukturen wie:\n
    "Marke":\n
    -- "Modell":\n
    ---- "Variante": ["A", "B"]\n

    :param parent_item: Das QTreeWidgetItem, dem untergeordnete Items hinzugefügt werden sollen.
    :param data: Ein Dictionary mit Strings als Schlüsseln und entweder weiteren Dictionaries oder Listen als Werten.
    :return: None
    """
    for key, value in data.items():
        item = QTreeWidgetItem([key])
        parent_item.addChild(item)

        if isinstance(value, dict):
            for subkey, subval in value.items():
                if isinstance(subval, dict):
                    subitem = QTreeWidgetItem([subkey])
                    item.addChild(subitem)
                    for dkey, dval in subval.items():
                        leaf = QTreeWidgetItem([dkey, dval])
                        subitem.addChild(leaf)
                else:
                    leaf = QTreeWidgetItem([subkey, subval])
                    item.addChild(leaf)


