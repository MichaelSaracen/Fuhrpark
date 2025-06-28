# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NavBar.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from app.widgets.buttons.IconButton import IconButton
import ressources_rc

class Ui_NavBar(object):
    def setupUi(self, NavBar):
        if not NavBar.objectName():
            NavBar.setObjectName(u"NavBar")
        NavBar.resize(94, 738)
        NavBar.setMinimumSize(QSize(60, 0))
        NavBar.setMaximumSize(QSize(94, 16777215))
        NavBar.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(NavBar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = IconButton(NavBar)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(60, 60))
        self.pushButton.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(7)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.setCheckable(True)
        self.pushButton.setProperty(u"pixmap", QPixmap(u":/icons/home.png"))

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_2 = IconButton(NavBar)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(60, 60))
        self.pushButton_2.setMaximumSize(QSize(60, 60))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIconSize(QSize(32, 32))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setProperty(u"pixmap", QPixmap(u":/icons/rent.png"))

        self.verticalLayout.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_3 = IconButton(NavBar)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(60, 60))
        self.pushButton_3.setMaximumSize(QSize(60, 60))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIconSize(QSize(32, 32))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setProperty(u"pixmap", QPixmap(u":/icons/car_prev.png"))

        self.verticalLayout.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_6 = IconButton(NavBar)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(60, 60))
        self.pushButton_6.setMaximumSize(QSize(60, 60))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setIconSize(QSize(32, 32))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setProperty(u"pixmap", QPixmap(u":/icons/status.png"))

        self.verticalLayout.addWidget(self.pushButton_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_5 = IconButton(NavBar)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(60, 60))
        self.pushButton_5.setMaximumSize(QSize(60, 60))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setIconSize(QSize(32, 32))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setProperty(u"pixmap", QPixmap(u":/icons/hist.png"))

        self.verticalLayout.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_4 = IconButton(NavBar)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(60, 60))
        self.pushButton_4.setMaximumSize(QSize(60, 60))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setIconSize(QSize(32, 32))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setProperty(u"pixmap", QPixmap(u":/icons/history.png"))

        self.verticalLayout.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_7 = IconButton(NavBar)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(60, 60))
        self.pushButton_7.setMaximumSize(QSize(60, 60))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setIconSize(QSize(32, 32))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setProperty(u"pixmap", QPixmap(u":/icons/statistic.png"))

        self.verticalLayout.addWidget(self.pushButton_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_8 = IconButton(NavBar)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(60, 60))
        self.pushButton_8.setMaximumSize(QSize(60, 60))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setIconSize(QSize(32, 32))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setProperty(u"pixmap", QPixmap(u":/icons/customers.png"))

        self.verticalLayout.addWidget(self.pushButton_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 255, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(NavBar)

        QMetaObject.connectSlotsByName(NavBar)
    # setupUi

    def retranslateUi(self, NavBar):
        NavBar.setWindowTitle(QCoreApplication.translate("NavBar", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("NavBar", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("NavBar", u"Vermietung", None))
        self.pushButton_3.setText(QCoreApplication.translate("NavBar", u"Vorschau", None))
        self.pushButton_6.setText(QCoreApplication.translate("NavBar", u"Status", None))
        self.pushButton_5.setText(QCoreApplication.translate("NavBar", u"Gebucht", None))
        self.pushButton_4.setText(QCoreApplication.translate("NavBar", u"Historie", None))
        self.pushButton_7.setText(QCoreApplication.translate("NavBar", u"Statistik", None))
        self.pushButton_8.setText(QCoreApplication.translate("NavBar", u"Kunden", None))
    # retranslateUi

