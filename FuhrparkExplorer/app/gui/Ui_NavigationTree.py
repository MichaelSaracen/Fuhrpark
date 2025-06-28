# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NavigationTree.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from app.widgets.tree_widgets.CarTree import CarTree
import ressources_rc

class Ui_NavigationTree(object):
    def setupUi(self, NavigationTree):
        if not NavigationTree.objectName():
            NavigationTree.setObjectName(u"NavigationTree")
        NavigationTree.resize(368, 149)
        NavigationTree.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(NavigationTree)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(NavigationTree)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"padding-left: 8px;")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_3 = QPushButton(NavigationTree)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(32, 32))
        self.pushButton_3.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(NavigationTree)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(32, 32))
        self.pushButton_2.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u":/icons/collapse_all.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(NavigationTree)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(32, 32))
        self.pushButton.setMaximumSize(QSize(32, 32))
        icon2 = QIcon()
        icon2.addFile(u":/icons/unfold_all.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.leSearch = QLineEdit(NavigationTree)
        self.leSearch.setObjectName(u"leSearch")
        self.leSearch.setMinimumSize(QSize(0, 32))
        self.leSearch.setMaximumSize(QSize(16777215, 32))
        self.leSearch.setStyleSheet(u"padding-left: 8px;")
        self.leSearch.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.leSearch)

        self.carTree = CarTree(NavigationTree)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.carTree.setHeaderItem(__qtreewidgetitem)
        self.carTree.setObjectName(u"carTree")
        self.carTree.setHeaderHidden(True)

        self.verticalLayout.addWidget(self.carTree)


        self.retranslateUi(NavigationTree)
        self.pushButton_3.clicked["bool"].connect(self.leSearch.setVisible)
        self.pushButton_2.clicked.connect(self.carTree.collapseAll)
        self.pushButton.clicked.connect(self.carTree.expandAll)

        QMetaObject.connectSlotsByName(NavigationTree)
    # setupUi

    def retranslateUi(self, NavigationTree):
        NavigationTree.setWindowTitle(QCoreApplication.translate("NavigationTree", u"Form", None))
        self.label.setText(QCoreApplication.translate("NavigationTree", u"Fahrzeu\u00fcbersicht", None))
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi

