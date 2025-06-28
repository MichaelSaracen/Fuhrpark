# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RentFormular.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QSplitter,
    QVBoxLayout, QWidget)

from app.widgets.DayPrice import DayPrice
from app.widgets.RentCustomerWidget import RentCustomerWidget
from app.widgets.buttons.IconButton import IconButton
import ressources_rc

class Ui_RentFormular(object):
    def setupUi(self, RentFormular):
        if not RentFormular.objectName():
            RentFormular.setObjectName(u"RentFormular")
        RentFormular.resize(1160, 632)
        RentFormular.setStyleSheet(u"#widget_5 {\n"
"	border-left: 1px solid rgb(42, 46, 54);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(RentFormular)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(RentFormular)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -201, 1178, 831))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setMinimumSize(QSize(300, 0))
        self.splitter.setMaximumSize(QSize(16777215, 16777215))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.splitter.setHandleWidth(1)
        self.dayPrice = DayPrice(self.splitter)
        self.dayPrice.setObjectName(u"dayPrice")
        self.dayPrice.setMinimumSize(QSize(0, 0))
        self.dayPrice.setMaximumSize(QSize(16777215, 16777215))
        self.dayPrice.setStyleSheet(u"")
        self.splitter.addWidget(self.dayPrice)
        self.rentCustomerWidget = RentCustomerWidget(self.splitter)
        self.rentCustomerWidget.setObjectName(u"rentCustomerWidget")
        self.rentCustomerWidget.setMaximumSize(QSize(16777215, 16777215))
        self.rentCustomerWidget.setStyleSheet(u"")
        self.splitter.addWidget(self.rentCustomerWidget)

        self.horizontalLayout_4.addWidget(self.splitter)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setSpacing(32)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(64, 64, 64, 64)
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(16)
        self.gridLayout_4.setContentsMargins(16, 16, 16, 16)
        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnRent_4 = IconButton(self.widget_4)
        self.btnRent_4.setObjectName(u"btnRent_4")
        self.btnRent_4.setMinimumSize(QSize(60, 60))
        self.btnRent_4.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(7)
        self.btnRent_4.setFont(font1)
        self.btnRent_4.setIconSize(QSize(32, 32))
        self.btnRent_4.setCheckable(True)
        self.btnRent_4.setChecked(True)
        self.btnRent_4.setProperty(u"pixmap", QPixmap(u":/icons/euro.png"))

        self.horizontalLayout_2.addWidget(self.btnRent_4)

        self.btnRent_2 = IconButton(self.widget_4)
        self.btnRent_2.setObjectName(u"btnRent_2")
        self.btnRent_2.setMinimumSize(QSize(60, 60))
        self.btnRent_2.setMaximumSize(QSize(16777215, 60))
        self.btnRent_2.setFont(font1)
        self.btnRent_2.setIconSize(QSize(32, 32))
        self.btnRent_2.setCheckable(True)
        self.btnRent_2.setChecked(True)
        self.btnRent_2.setProperty(u"pixmap", QPixmap(u":/icons/auswahl.png"))

        self.horizontalLayout_2.addWidget(self.btnRent_2)

        self.btnRent_3 = IconButton(self.widget_4)
        self.btnRent_3.setObjectName(u"btnRent_3")
        self.btnRent_3.setMinimumSize(QSize(60, 60))
        self.btnRent_3.setMaximumSize(QSize(16777215, 60))
        self.btnRent_3.setFont(font1)
        self.btnRent_3.setIconSize(QSize(32, 32))
        self.btnRent_3.setCheckable(True)
        self.btnRent_3.setChecked(True)
        self.btnRent_3.setProperty(u"pixmap", QPixmap(u":/icons/calendar.png"))

        self.horizontalLayout_2.addWidget(self.btnRent_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(16)
        self.gridLayout_3.setContentsMargins(16, 16, 16, 16)
        self.cwFrom = QCalendarWidget(self.widget_3)
        self.cwFrom.setObjectName(u"cwFrom")
        self.cwFrom.setMinimumSize(QSize(351, 0))
        self.cwFrom.setStyleSheet(u"QToolButton::menu-indicator{\n"
"	border: none;\n"
"	qproperty-image: none;\n"
"	image: none;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"	border: none;\n"
"qproperty-icon: none;\n"
"	image: url(:/icons/chev_l.png);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth::hover {\n"
"	background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth {\n"
"	border: none;\n"
"qproperty-icon: none;\n"
"	image: url(:/icons/chev_r.png);\n"
"}\n"
"\n"
"#qt_calendar_yearbutton {\n"
"	border: none;\n"
"	qproperty-image: none;\n"
"	image: none;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton {\n"
"	border: none;\n"
"	qproperty-image: none;\n"
"	image: none;\n"
"}\n"
"\n"
"\n"
"/* Kalender-Hauptbereich */\n"
"QCalendarWidget {\n"
"    background-color: white;\n"
"    border: 1px solid rgba(0, 0, 0, 30);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* Navigation (Monat/Jahr oben) */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 20);\n"
"}\n"
"\n"
"/* Mon"
                        "at und Jahr Label */\n"
"QCalendarWidget QToolButton {\n"
"    background: transparent;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    margin: 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 20);\n"
"}\n"
"\n"
"/* Pfeil-Buttons links/rechts */\n"
"QCalendarWidget QAbstractButton {\n"
"    border: none;\n"
"}\n"
"\n"
"/* Wochentage (Mo, Di, ...) */\n"
"QCalendarWidget QHeaderView {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    selection-background-color: rgba(0, 0, 0, 20);\n"
"    selection-color: black;\n"
"    gridline-color: rgba(0, 0, 0, 10);\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Tage im Kalender */\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: white;\n"
"    alternate-background-color: #f9f9f9;\n"
"    color: black;\n"
"    selection-bac"
                        "kground-color: rgba(0, 0, 0, 20);\n"
"    selection-color: black;\n"
"}\n"
"\n"
"/* Heute-Markierung */\n"
"QCalendarWidget QAbstractItemView::item {\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:enabled:selected {\n"
"    background-color: rgba(0, 0, 0, 20);\n"
"    color: black;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.cwFrom, 0, 0, 1, 1)

        self.markeLabel_5 = QLabel(self.widget_3)
        self.markeLabel_5.setObjectName(u"markeLabel_5")
        font2 = QFont()
        font2.setPointSize(7)
        self.markeLabel_5.setFont(font2)
        self.markeLabel_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.markeLabel_5, 3, 1, 1, 1)

        self.cwTo = QCalendarWidget(self.widget_3)
        self.cwTo.setObjectName(u"cwTo")
        self.cwTo.setMinimumSize(QSize(351, 0))
        self.cwTo.setStyleSheet(u"QToolButton::menu-indicator{\n"
"	border: none;\n"
"	qproperty-image: none;\n"
"	image: none;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"	border: none;\n"
"qproperty-icon: none;\n"
"	image: url(:/icons/chev_l.png);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth::hover {\n"
"	background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth {\n"
"	border: none;\n"
"qproperty-icon: none;\n"
"	image: url(:/icons/chev_r.png);\n"
"}\n"
"\n"
"#qt_calendar_yearbutton {\n"
"	border: none;\n"
"	qproperty-image: none;\n"
"	image: none;\n"
"}\n"
"\n"
"#qt_calendar_monthbutton {\n"
"	border: none;\n"
"	qproperty-image: none;\n"
"	image: none;\n"
"}\n"
"\n"
"\n"
"/* Kalender-Hauptbereich */\n"
"QCalendarWidget {\n"
"    background-color: white;\n"
"    border: 1px solid rgba(0, 0, 0, 30);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* Navigation (Monat/Jahr oben) */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 20);\n"
"}\n"
"\n"
"/* Mon"
                        "at und Jahr Label */\n"
"QCalendarWidget QToolButton {\n"
"    background: transparent;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    padding: 4px;\n"
"    margin: 2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 20);\n"
"}\n"
"\n"
"/* Pfeil-Buttons links/rechts */\n"
"QCalendarWidget QAbstractButton {\n"
"    border: none;\n"
"}\n"
"\n"
"/* Wochentage (Mo, Di, ...) */\n"
"QCalendarWidget QHeaderView {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    selection-background-color: rgba(0, 0, 0, 20);\n"
"    selection-color: black;\n"
"    gridline-color: rgba(0, 0, 0, 10);\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Tage im Kalender */\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: white;\n"
"    alternate-background-color: #f9f9f9;\n"
"    color: black;\n"
"    selection-bac"
                        "kground-color: rgba(0, 0, 0, 20);\n"
"    selection-color: black;\n"
"}\n"
"\n"
"/* Heute-Markierung */\n"
"QCalendarWidget QAbstractItemView::item {\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:enabled:selected {\n"
"    background-color: rgba(0, 0, 0, 20);\n"
"    color: black;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView::item:hover {\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"}\n"
"")
        self.cwTo.setGridVisible(False)
        self.cwTo.setNavigationBarVisible(True)
        self.cwTo.setDateEditEnabled(True)

        self.gridLayout_3.addWidget(self.cwTo, 0, 1, 1, 1)

        self.markeLabel_4 = QLabel(self.widget_3)
        self.markeLabel_4.setObjectName(u"markeLabel_4")
        self.markeLabel_4.setFont(font2)

        self.gridLayout_3.addWidget(self.markeLabel_4, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget = QWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 110))
        self.widget.setMaximumSize(QSize(16777215, 110))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.cbBrand = QComboBox(self.widget)
        self.cbBrand.setObjectName(u"cbBrand")
        self.cbBrand.setMinimumSize(QSize(0, 60))
        self.cbBrand.setMaximumSize(QSize(16777215, 60))
        font3 = QFont()
        font3.setPointSize(14)
        self.cbBrand.setFont(font3)

        self.gridLayout.addWidget(self.cbBrand, 0, 0, 1, 1)

        self.cbModel = QComboBox(self.widget)
        self.cbModel.setObjectName(u"cbModel")
        self.cbModel.setMinimumSize(QSize(0, 60))
        self.cbModel.setMaximumSize(QSize(16777215, 60))
        self.cbModel.setFont(font3)
        self.cbModel.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cbModel, 0, 1, 1, 1)

        self.lePricePerDay = QLineEdit(self.widget)
        self.lePricePerDay.setObjectName(u"lePricePerDay")
        self.lePricePerDay.setMinimumSize(QSize(0, 60))
        self.lePricePerDay.setMaximumSize(QSize(16777215, 60))
        self.lePricePerDay.setFont(font3)
        self.lePricePerDay.setMaxLength(16)
        self.lePricePerDay.setReadOnly(True)

        self.gridLayout.addWidget(self.lePricePerDay, 0, 2, 1, 1)

        self.sbDays = QSpinBox(self.widget)
        self.sbDays.setObjectName(u"sbDays")
        self.sbDays.setMinimumSize(QSize(0, 60))
        self.sbDays.setMaximumSize(QSize(16777215, 60))
        self.sbDays.setFont(font3)
        self.sbDays.setReadOnly(True)
        self.sbDays.setMinimum(1)
        self.sbDays.setMaximum(100)

        self.gridLayout.addWidget(self.sbDays, 0, 3, 1, 1)

        self.markeLabel = QLabel(self.widget)
        self.markeLabel.setObjectName(u"markeLabel")
        self.markeLabel.setFont(font2)

        self.gridLayout.addWidget(self.markeLabel, 1, 0, 1, 1)

        self.modellLabel = QLabel(self.widget)
        self.modellLabel.setObjectName(u"modellLabel")
        self.modellLabel.setFont(font2)
        self.modellLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.modellLabel, 1, 1, 1, 1)

        self.tagespreisLabel = QLabel(self.widget)
        self.tagespreisLabel.setObjectName(u"tagespreisLabel")
        self.tagespreisLabel.setFont(font2)
        self.tagespreisLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.tagespreisLabel, 1, 2, 1, 1)

        self.tageLabel = QLabel(self.widget)
        self.tageLabel.setObjectName(u"tageLabel")
        self.tageLabel.setFont(font2)
        self.tageLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.tageLabel, 1, 3, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 110))
        self.widget_2.setMaximumSize(QSize(16777215, 110))
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(16)
        self.gridLayout_2.setContentsMargins(-1, 16, 16, 16)
        self.leCustomerID = QLineEdit(self.widget_2)
        self.leCustomerID.setObjectName(u"leCustomerID")
        self.leCustomerID.setMinimumSize(QSize(0, 60))
        self.leCustomerID.setMaximumSize(QSize(16777215, 60))
        font4 = QFont()
        font4.setPointSize(24)
        self.leCustomerID.setFont(font4)
        self.leCustomerID.setReadOnly(True)

        self.gridLayout_2.addWidget(self.leCustomerID, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblTotalPrice = QLabel(self.widget_2)
        self.lblTotalPrice.setObjectName(u"lblTotalPrice")
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(24)
        self.lblTotalPrice.setFont(font5)
        self.lblTotalPrice.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lblTotalPrice)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(16)
        self.label_5.setFont(font6)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalLayout.setStretch(1, 2)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.markeLabel_2 = QLabel(self.widget_2)
        self.markeLabel_2.setObjectName(u"markeLabel_2")
        self.markeLabel_2.setFont(font2)

        self.gridLayout_2.addWidget(self.markeLabel_2, 1, 0, 1, 1)

        self.markeLabel_6 = QLabel(self.widget_2)
        self.markeLabel_6.setObjectName(u"markeLabel_6")
        self.markeLabel_6.setFont(font2)
        self.markeLabel_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.markeLabel_6, 1, 1, 1, 1)

        self.btnRent = IconButton(self.widget_2)
        self.btnRent.setObjectName(u"btnRent")
        self.btnRent.setMinimumSize(QSize(60, 60))
        self.btnRent.setMaximumSize(QSize(16777215, 111))
        self.btnRent.setFont(font1)
        self.btnRent.setIconSize(QSize(32, 32))
        self.btnRent.setCheckable(False)
        self.btnRent.setProperty(u"pixmap", QPixmap(u":/icons/buy.png"))

        self.gridLayout_2.addWidget(self.btnRent, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout_4.addWidget(self.widget_5)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)


        self.retranslateUi(RentFormular)
        self.btnRent_4.clicked["bool"].connect(self.dayPrice.setVisible)
        self.btnRent_2.clicked["bool"].connect(self.widget.setVisible)
        self.btnRent_3.clicked["bool"].connect(self.widget_3.setVisible)

        QMetaObject.connectSlotsByName(RentFormular)
    # setupUi

    def retranslateUi(self, RentFormular):
        RentFormular.setWindowTitle(QCoreApplication.translate("RentFormular", u"Form", None))
        self.label.setText(QCoreApplication.translate("RentFormular", u"# Fahrzeug Vermietung", None))
        self.btnRent_4.setText(QCoreApplication.translate("RentFormular", u"Preise", None))
        self.btnRent_2.setText(QCoreApplication.translate("RentFormular", u"Auswahl", None))
        self.btnRent_3.setText(QCoreApplication.translate("RentFormular", u"Datum", None))
        self.markeLabel_5.setText(QCoreApplication.translate("RentFormular", u"Abgabe Datum", None))
        self.markeLabel_4.setText(QCoreApplication.translate("RentFormular", u"Abhol Datum", None))
        self.markeLabel.setText(QCoreApplication.translate("RentFormular", u"Marke", None))
        self.modellLabel.setText(QCoreApplication.translate("RentFormular", u"Modell", None))
        self.tagespreisLabel.setText(QCoreApplication.translate("RentFormular", u"Tagespreis", None))
        self.tageLabel.setText(QCoreApplication.translate("RentFormular", u"Tage", None))
        self.lblTotalPrice.setText(QCoreApplication.translate("RentFormular", u"0.00", None))
        self.label_5.setText(QCoreApplication.translate("RentFormular", u"\u20ac", None))
        self.markeLabel_2.setText(QCoreApplication.translate("RentFormular", u"Kundennummer", None))
        self.markeLabel_6.setText(QCoreApplication.translate("RentFormular", u"Gesamtpreis", None))
        self.btnRent.setText(QCoreApplication.translate("RentFormular", u"An den Kunden Vermieten", None))
    # retranslateUi

