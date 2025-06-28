# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DayPrice.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from app.widgets.tree_widgets.DayPriceTree import DayPriceTree
import ressources_rc

class Ui_DayPrice(object):
    def setupUi(self, DayPrice):
        if not DayPrice.objectName():
            DayPrice.setObjectName(u"DayPrice")
        DayPrice.resize(811, 684)
        self.verticalLayout = QVBoxLayout(DayPrice)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(DayPrice)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCollapse = QPushButton(DayPrice)
        self.btnCollapse.setObjectName(u"btnCollapse")
        self.btnCollapse.setMinimumSize(QSize(32, 32))
        self.btnCollapse.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/icons/collapse_all.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCollapse.setIcon(icon)
        self.btnCollapse.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btnCollapse)

        self.btnExpand = QPushButton(DayPrice)
        self.btnExpand.setObjectName(u"btnExpand")
        self.btnExpand.setMinimumSize(QSize(32, 32))
        self.btnExpand.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/icons/unfold_all.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnExpand.setIcon(icon1)
        self.btnExpand.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btnExpand)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.dayPriceTree = DayPriceTree(DayPrice)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.dayPriceTree.setHeaderItem(__qtreewidgetitem)
        self.dayPriceTree.setObjectName(u"dayPriceTree")
        self.dayPriceTree.setStyleSheet(u"")
        self.dayPriceTree.header().setVisible(False)

        self.verticalLayout.addWidget(self.dayPriceTree)


        self.retranslateUi(DayPrice)
        self.btnExpand.clicked.connect(self.dayPriceTree.expandAll)
        self.btnCollapse.clicked.connect(self.dayPriceTree.collapseAll)

        QMetaObject.connectSlotsByName(DayPrice)
    # setupUi

    def retranslateUi(self, DayPrice):
        DayPrice.setWindowTitle(QCoreApplication.translate("DayPrice", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("DayPrice", u"Tagespreise", None))
        self.btnCollapse.setText("")
        self.btnExpand.setText("")
    # retranslateUi

