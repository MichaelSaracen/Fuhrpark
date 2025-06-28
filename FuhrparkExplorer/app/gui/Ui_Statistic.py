# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Statistic.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from app.widgets.BarChart import BarChart
from app.widgets.DonutCharts.PieChart import PieChart
import ressources_rc

class Ui_Statistic(object):
    def setupUi(self, Statistic):
        if not Statistic.objectName():
            Statistic.setObjectName(u"Statistic")
        Statistic.resize(1214, 993)
        self.verticalLayout_4 = QVBoxLayout(Statistic)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Statistic)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1212, 991))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(32)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(64, 64, 64, 64)
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(False)

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.barChart = BarChart(self.widget)
        self.barChart.setObjectName(u"barChart")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barChart.sizePolicy().hasHeightForWidth())
        self.barChart.setSizePolicy(sizePolicy)
        self.barChart.setMinimumSize(QSize(300, 300))

        self.horizontalLayout.addWidget(self.barChart)

        self.pieChart = PieChart(self.widget)
        self.pieChart.setObjectName(u"pieChart")
        self.pieChart.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.horizontalLayout.addWidget(self.pieChart)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.barChart_2 = BarChart(self.widget)
        self.barChart_2.setObjectName(u"barChart_2")
        self.barChart_2.setMinimumSize(QSize(0, 300))

        self.verticalLayout.addWidget(self.barChart_2)


        self.verticalLayout_3.addWidget(self.widget)

        self.verticalLayout_3.setStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.retranslateUi(Statistic)

        QMetaObject.connectSlotsByName(Statistic)
    # setupUi

    def retranslateUi(self, Statistic):
        Statistic.setWindowTitle(QCoreApplication.translate("Statistic", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Statistic", u"<html><head/><body><p><span style=\" font-size:8pt;\">\u00dcbersicht \u00fcber die Vermietungungen.</span></p><p><span style=\" font-size:8pt;\">- Welche Marke wird am h\u00e4ufigsten vermietet?</span></p><p>- Welches Modell ist gefragtesten?</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Statistic", u"# Statistiken", None))
    # retranslateUi

