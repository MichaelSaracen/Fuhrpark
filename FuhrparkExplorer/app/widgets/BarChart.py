from PySide6.QtCharts import (QBarCategoryAxis, QBarSeries, QBarSet, QChart,
                              QChartView, QValueAxis)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QHBoxLayout


class BarChart(QWidget):
    def __init__(self, parent: QWidget=None):
        super().__init__(parent)
        self._set_0 = QBarSet("Cars")

        self._set_0.append([1, 2, 3, 4, 5, 6])

        self._series = QBarSeries()
        self._series.append(self._set_0)

        self._chart = QChart()
        self._chart.addSeries(self._series)
        self._chart.setTitle("Fahrzeug Buchungen")
        self._chart.setAnimationOptions(QChart.SeriesAnimations)

        self._categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        self._axis_x = QBarCategoryAxis()
        self._axis_x.append(self._categories)
        self._chart.addAxis(self._axis_x, Qt.AlignmentFlag.AlignBottom)
        self._series.attachAxis(self._axis_x)

        self._axis_y = QValueAxis()
        self._axis_y.setRange(0, 15)
        self._chart.addAxis(self._axis_y, Qt.AlignmentFlag.AlignLeft)
        self._series.attachAxis(self._axis_y)

        self._chart.legend().setVisible(False)
        self._chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        self._chart_view = QChartView(self._chart)
        self._chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        layout: QHBoxLayout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        layout.addWidget(self._chart_view)

    def set_categories(self, categories: list) -> None:
        self._axis_x.clear()
        self._axis_x.append(categories)

    def set_values(self, values: list) -> None:
        self._series.clear()

        new_set = QBarSet("Cars")
        new_set.append(values)

        self._series.append(new_set)

        self._axis_y.setRange(0, max(values))
