# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TreePriceWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)
import ressources_rc

class Ui_TreePriceWidget(object):
    def setupUi(self, TreePriceWidget):
        if not TreePriceWidget.objectName():
            TreePriceWidget.setObjectName(u"TreePriceWidget")
        TreePriceWidget.resize(692, 24)
        TreePriceWidget.setMinimumSize(QSize(0, 24))
        TreePriceWidget.setMaximumSize(QSize(16777215, 26))
        TreePriceWidget.setStyleSheet(u"background: none;\n"
"border: 0px;")
        self.horizontalLayout_2 = QHBoxLayout(TreePriceWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.lblModel = QLabel(TreePriceWidget)
        self.lblModel.setObjectName(u"lblModel")
        self.lblModel.setMinimumSize(QSize(1, 0))
        self.lblModel.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        self.lblModel.setFont(font)

        self.horizontalLayout_2.addWidget(self.lblModel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblPrice = QLabel(TreePriceWidget)
        self.lblPrice.setObjectName(u"lblPrice")
        font1 = QFont()
        font1.setFamilies([u"Roboto Mono"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.lblPrice.setFont(font1)
        self.lblPrice.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lblPrice)

        self.lblEuro = QLabel(TreePriceWidget)
        self.lblEuro.setObjectName(u"lblEuro")
        self.lblEuro.setFont(font1)
        self.lblEuro.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lblEuro, 0, Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2.setStretch(0, 1)

        self.retranslateUi(TreePriceWidget)

        QMetaObject.connectSlotsByName(TreePriceWidget)
    # setupUi

    def retranslateUi(self, TreePriceWidget):
        TreePriceWidget.setWindowTitle(QCoreApplication.translate("TreePriceWidget", u"Form", None))
        self.lblModel.setText(QCoreApplication.translate("TreePriceWidget", u"A3", None))
        self.lblPrice.setText(QCoreApplication.translate("TreePriceWidget", u"20.00", None))
        self.lblEuro.setText(QCoreApplication.translate("TreePriceWidget", u"\u20ac", None))
    # retranslateUi

