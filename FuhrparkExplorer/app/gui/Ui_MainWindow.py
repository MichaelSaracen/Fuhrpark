# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)

from app.core.Theme import Theme
from app.widgets.CarDisplayWidget import CarDisplayWidget
from app.widgets.CarStatus import CarStatus
from app.widgets.Customers import Customers
from app.widgets.History import History
from app.widgets.NavigationTree import NavigationTree
from app.widgets.RentFormular import RentFormular
from app.widgets.RentedCarsByCustomers import RentedCarsByCustomers
from app.widgets.Statistic import Statistic
from app.widgets.bars.NavBar import NavBar
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1171, 721)
        MainWindow.setStyleSheet(u"")
#         MainWindow.setStyleSheet(f"""
# QWidget {{
#     background: {Theme.background.name()}
# }}
# """)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        self.actNavigationOnOff = QAction(MainWindow)
        self.actNavigationOnOff.setObjectName(u"actNavigationOnOff")
        self.actNavigationOnOff.setCheckable(True)
        self.actNavigationOnOff.setChecked(True)
        self.actAddNewCar = QAction(MainWindow)
        self.actAddNewCar.setObjectName(u"actAddNewCar")
        self.actCustomer = QAction(MainWindow)
        self.actCustomer.setObjectName(u"actCustomer")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.navBar = NavBar(self.centralwidget)
        self.navBar.setObjectName(u"navBar")
        self.navBar.setMinimumSize(QSize(61, 0))
        self.navBar.setMaximumSize(QSize(61, 16777215))

        self.horizontalLayout.addWidget(self.navBar)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1108, 665))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.widgetLogo = QWidget(self.page)
        self.widgetLogo.setObjectName(u"widgetLogo")
        self.verticalLayout_3 = QVBoxLayout(self.widgetLogo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widgetLogo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.widgetLogo)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.widgetLogo, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.logo = QLabel(self.page)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u":/cars/audi v13 tuning sportwage.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.page)
        self.rentFormular = RentFormular()
        self.rentFormular.setObjectName(u"rentFormular")
        self.stackedWidget.addWidget(self.rentFormular)
        self.wg_Fahrzeug = QWidget()
        self.wg_Fahrzeug.setObjectName(u"wg_Fahrzeug")
        self.verticalLayout = QVBoxLayout(self.wg_Fahrzeug)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.splitterCarDisplay = QSplitter(self.wg_Fahrzeug)
        self.splitterCarDisplay.setObjectName(u"splitterCarDisplay")
        self.splitterCarDisplay.setOrientation(Qt.Orientation.Horizontal)
        self.splitterCarDisplay.setHandleWidth(1)
        self.navigationTree = NavigationTree(self.splitterCarDisplay)
        self.navigationTree.setObjectName(u"navigationTree")
        self.splitterCarDisplay.addWidget(self.navigationTree)
        self.carDisplay = CarDisplayWidget(self.splitterCarDisplay)
        self.carDisplay.setObjectName(u"carDisplay")
        self.carDisplay.setStyleSheet(u"border-left: 1px solid rgba(0,0,0,50);")
        self.splitterCarDisplay.addWidget(self.carDisplay)

        self.verticalLayout.addWidget(self.splitterCarDisplay)

        self.stackedWidget.addWidget(self.wg_Fahrzeug)
        self.carStatus = CarStatus()
        self.carStatus.setObjectName(u"carStatus")
        self.stackedWidget.addWidget(self.carStatus)
        self.rentedCardsByCustomers = RentedCarsByCustomers()
        self.rentedCardsByCustomers.setObjectName(u"rentedCardsByCustomers")
        self.stackedWidget.addWidget(self.rentedCardsByCustomers)
        self.history = History()
        self.history.setObjectName(u"history")
        self.stackedWidget.addWidget(self.history)
        self.statistic = Statistic()
        self.statistic.setObjectName(u"statistic")
        self.stackedWidget.addWidget(self.statistic)
        self.customers = Customers()
        self.customers.setObjectName(u"customers")
        self.stackedWidget.addWidget(self.customers)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1171, 33))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuAnsicht = QMenu(self.menubar)
        self.menuAnsicht.setObjectName(u"menuAnsicht")
        self.menuHinzuf_gen = QMenu(self.menubar)
        self.menuHinzuf_gen.setObjectName(u"menuHinzuf_gen")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuAnsicht.menuAction())
        self.menubar.addAction(self.menuHinzuf_gen.menuAction())
        self.menuDatei.addAction(self.actQuit)
        self.menuAnsicht.addAction(self.actNavigationOnOff)
        self.menuHinzuf_gen.addAction(self.actAddNewCar)
        self.menuHinzuf_gen.addSeparator()
        self.menuHinzuf_gen.addAction(self.actCustomer)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"Beenden", None))
#if QT_CONFIG(shortcut)
        self.actQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.actNavigationOnOff.setText(QCoreApplication.translate("MainWindow", u"Navigation an/aus", None))
        self.actAddNewCar.setText(QCoreApplication.translate("MainWindow", u"Fahrzeug", None))
        self.actCustomer.setText(QCoreApplication.translate("MainWindow", u"Kunde", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"# Fuhrpark Explorer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"#### acht Tage die Woche Fullsupport!", None))
        self.logo.setText("")
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menuAnsicht.setTitle(QCoreApplication.translate("MainWindow", u"Ansicht", None))
        self.menuHinzuf_gen.setTitle(QCoreApplication.translate("MainWindow", u"Hinzuf\u00fcgen", None))
    # retranslateUi

