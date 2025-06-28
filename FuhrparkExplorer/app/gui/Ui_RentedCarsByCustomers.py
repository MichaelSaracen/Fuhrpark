# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RentedCarsByCustomers.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from app.widgets.buttons.IconButton import IconButton
import ressources_rc

class Ui_RentedCarsByCustomers(object):
    def setupUi(self, RentedCarsByCustomers):
        if not RentedCarsByCustomers.objectName():
            RentedCarsByCustomers.setObjectName(u"RentedCarsByCustomers")
        RentedCarsByCustomers.resize(1111, 1053)
        self.verticalLayout_4 = QVBoxLayout(RentedCarsByCustomers)
        self.verticalLayout_4.setSpacing(32)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(64, 64, 64, 64)
        self.widget_2 = QWidget(RentedCarsByCustomers)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btnSearch = IconButton(self.widget_2)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setMinimumSize(QSize(60, 60))
        self.btnSearch.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.btnSearch.setFont(font)
        self.btnSearch.setIconSize(QSize(32, 32))
        self.btnSearch.setCheckable(True)
        self.btnSearch.setChecked(True)
        self.btnSearch.setProperty(u"pixmap", QPixmap(u":/icons/search.png"))

        self.verticalLayout_2.addWidget(self.btnSearch)


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
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_3 = QWidget(RentedCarsByCustomers)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.leSearch = QLineEdit(self.widget_3)
        self.leSearch.setObjectName(u"leSearch")
        self.leSearch.setMinimumSize(QSize(0, 60))
        self.leSearch.setMaximumSize(QSize(16777215, 32))
        font2 = QFont()
        font2.setPointSize(24)
        self.leSearch.setFont(font2)
        self.leSearch.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.leSearch.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.leSearch)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.radioButton = QRadioButton(self.widget_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.widget_3)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_2.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.widget_3)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_2.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.widget_3)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_2.addWidget(self.radioButton_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget = QWidget(RentedCarsByCustomers)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(16, 16, 16, 16)
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.widget)

        self.verticalLayout_4.setStretch(2, 1)

        self.retranslateUi(RentedCarsByCustomers)
        self.btnSearch.clicked["bool"].connect(self.widget_3.setVisible)

        QMetaObject.connectSlotsByName(RentedCarsByCustomers)
    # setupUi

    def retranslateUi(self, RentedCarsByCustomers):
        RentedCarsByCustomers.setWindowTitle(QCoreApplication.translate("RentedCarsByCustomers", u"Form", None))
        self.btnSearch.setText(QCoreApplication.translate("RentedCarsByCustomers", u"Suche", None))
        self.label_2.setText(QCoreApplication.translate("RentedCarsByCustomers", u"<html><head/><body><p><span style=\" font-size:8pt;\">Hier findest du eine Tabellarische Ansicht, \u00fcber </span><span style=\" font-size:8pt; font-weight:700;\">alle</span><span style=\" font-size:8pt;\"> Fahrzeuge, die zzt </span><span style=\" font-size:8pt; font-weight:700;\">vermietet</span><span style=\" font-size:8pt;\"> sind.</span></p><p><span style=\" font-size:8pt;\">Mit der </span><span style=\" font-size:8pt; font-weight:700;\">Suchfunktion</span><span style=\" font-size:8pt;\">, kannst du unter bestimmten Krierien, zu den gew\u00fcnschten Feldern navigieren.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("RentedCarsByCustomers", u"# Gebuchte Fahrzeuge", None))
        self.radioButton.setText(QCoreApplication.translate("RentedCarsByCustomers", u"Kundennummer", None))
        self.radioButton_2.setText(QCoreApplication.translate("RentedCarsByCustomers", u"Vorname", None))
        self.radioButton_3.setText(QCoreApplication.translate("RentedCarsByCustomers", u"Nachname", None))
        self.radioButton_4.setText(QCoreApplication.translate("RentedCarsByCustomers", u"Fahrzeugnummer", None))
        self.radioButton_5.setText(QCoreApplication.translate("RentedCarsByCustomers", u"von", None))
        self.radioButton_6.setText(QCoreApplication.translate("RentedCarsByCustomers", u"bis", None))
    # retranslateUi

