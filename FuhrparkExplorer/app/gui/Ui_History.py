# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'History.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_History(object):
    def setupUi(self, History):
        if not History.objectName():
            History.setObjectName(u"History")
        History.resize(1225, 926)
        self.verticalLayout_3 = QVBoxLayout(History)
        self.verticalLayout_3.setSpacing(32)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(64, 64, 64, 64)
        self.widget_2 = QWidget(History)
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

        self.widget = QWidget(History)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.verticalLayout_3.addWidget(self.widget)

        self.verticalLayout_3.setStretch(1, 1)

        self.retranslateUi(History)

        QMetaObject.connectSlotsByName(History)
    # setupUi

    def retranslateUi(self, History):
        History.setWindowTitle(QCoreApplication.translate("History", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("History", u"<html><head/><body><p><span style=\" font-size:8pt;\">Historien\u00fcbersicht.</span></p><p><span style=\" font-size:8pt;\">Darstellung von </span><span style=\" font-size:8pt; font-weight:700;\">Marke</span><span style=\" font-size:8pt;\">, </span><span style=\" font-size:8pt; font-weight:700;\">Modell</span><span style=\" font-size:8pt;\">, </span><span style=\" font-size:8pt; font-weight:700;\">Preis</span><span style=\" font-size:8pt;\">, </span><span style=\" font-size:8pt; font-weight:700;\">Annahme</span><span style=\" font-size:8pt;\"> und </span><span style=\" font-size:8pt; font-weight:700;\">Abgabedatum</span><span style=\" font-size:8pt;\">.</span></p><p><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("History", u"# Historie", None))
    # retranslateUi

