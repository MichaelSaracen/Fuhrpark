# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CarStatus.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from app.widgets.buttons.IconButton import IconButton
from app.widgets.tree_widgets.CarStatusTree import CarStatusTree
import ressources_rc

class Ui_CarStatus(object):
    def setupUi(self, CarStatus):
        if not CarStatus.objectName():
            CarStatus.setObjectName(u"CarStatus")
        CarStatus.resize(1030, 754)
        self.verticalLayout_3 = QVBoxLayout(CarStatus)
        self.verticalLayout_3.setSpacing(32)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(64, 64, 64, 64)
        self.widget_2 = QWidget(CarStatus)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(False)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget = QWidget(CarStatus)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSearch_2 = IconButton(self.widget)
        self.btnSearch_2.setObjectName(u"btnSearch_2")
        self.btnSearch_2.setMinimumSize(QSize(60, 60))
        self.btnSearch_2.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(7)
        self.btnSearch_2.setFont(font1)
        self.btnSearch_2.setIconSize(QSize(32, 32))
        self.btnSearch_2.setCheckable(False)
        self.btnSearch_2.setChecked(False)
        self.btnSearch_2.setProperty(u"pixmap", QPixmap(u":/icons/collapse_all.png"))

        self.horizontalLayout.addWidget(self.btnSearch_2)

        self.btnSearch = IconButton(self.widget)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setMinimumSize(QSize(60, 60))
        self.btnSearch.setMaximumSize(QSize(60, 60))
        self.btnSearch.setFont(font1)
        self.btnSearch.setIconSize(QSize(32, 32))
        self.btnSearch.setCheckable(False)
        self.btnSearch.setChecked(False)
        self.btnSearch.setProperty(u"pixmap", QPixmap(u":/icons/unfold_all.png"))

        self.horizontalLayout.addWidget(self.btnSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.carStatusTree = CarStatusTree(self.widget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.carStatusTree.setHeaderItem(__qtreewidgetitem)
        self.carStatusTree.setObjectName(u"carStatusTree")
        self.carStatusTree.header().setVisible(False)

        self.verticalLayout.addWidget(self.carStatusTree)


        self.verticalLayout_3.addWidget(self.widget)

        self.verticalLayout_3.setStretch(1, 1)

        self.retranslateUi(CarStatus)
        self.btnSearch.clicked.connect(self.carStatusTree.expandAll)
        self.btnSearch_2.clicked.connect(self.carStatusTree.collapseAll)

        QMetaObject.connectSlotsByName(CarStatus)
    # setupUi

    def retranslateUi(self, CarStatus):
        CarStatus.setWindowTitle(QCoreApplication.translate("CarStatus", u"Form", None))
        self.label.setText(QCoreApplication.translate("CarStatus", u"# Fahrzeugstatus", None))
        self.label_2.setText(QCoreApplication.translate("CarStatus", u"<html><head/><body><p>Zeigt die Fahrzeuge, die <span style=\" font-weight:700;\">vermietet</span>, <span style=\" font-weight:700;\">verf\u00fcgbar</span> oder in der <span style=\" font-weight:700;\">Reparatur</span> sind, in einer Baumansicht an.</p></body></html>", None))
        self.btnSearch_2.setText(QCoreApplication.translate("CarStatus", u"einklappen", None))
        self.btnSearch.setText(QCoreApplication.translate("CarStatus", u"aufklappen", None))
    # retranslateUi

