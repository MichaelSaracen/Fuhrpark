# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TreeStatusWidget.ui'
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
    QSpacerItem, QWidget)

class Ui_TreeStatusWidget(object):
    def setupUi(self, TreeStatusWidget):
        if not TreeStatusWidget.objectName():
            TreeStatusWidget.setObjectName(u"TreeStatusWidget")
        TreeStatusWidget.resize(711, 40)
        TreeStatusWidget.setStyleSheet(u"\n"
"background-color: none;\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(TreeStatusWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.widgetStatus = QWidget(TreeStatusWidget)
        self.widgetStatus.setObjectName(u"widgetStatus")
        self.widgetStatus.setMinimumSize(QSize(16, 16))
        self.widgetStatus.setMaximumSize(QSize(16, 16))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        self.widgetStatus.setFont(font)
        self.widgetStatus.setStyleSheet(u"border: 1px solid rgba(0,0,0,50);\n"
"border-radius: 8px;\n"
"")

        self.horizontalLayout_3.addWidget(self.widgetStatus)

        self.horizontalSpacer = QSpacerItem(8, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblBrand = QLabel(TreeStatusWidget)
        self.lblBrand.setObjectName(u"lblBrand")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.lblBrand.setFont(font1)

        self.horizontalLayout.addWidget(self.lblBrand)

        self.lblModel = QLabel(TreeStatusWidget)
        self.lblModel.setObjectName(u"lblModel")
        self.lblModel.setFont(font1)

        self.horizontalLayout.addWidget(self.lblModel)

        self.horizontalLayout.setStretch(1, 1)

        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(TreeStatusWidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(7)
        font2.setBold(False)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lblCarNum = QLabel(TreeStatusWidget)
        self.lblCarNum.setObjectName(u"lblCarNum")
        self.lblCarNum.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lblCarNum)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.lblPic = QLabel(TreeStatusWidget)
        self.lblPic.setObjectName(u"lblPic")
        self.lblPic.setMinimumSize(QSize(32, 32))
        self.lblPic.setMaximumSize(QSize(32, 32))
        self.lblPic.setFont(font)

        self.horizontalLayout_3.addWidget(self.lblPic)


        self.retranslateUi(TreeStatusWidget)

        QMetaObject.connectSlotsByName(TreeStatusWidget)
    # setupUi

    def retranslateUi(self, TreeStatusWidget):
        TreeStatusWidget.setWindowTitle(QCoreApplication.translate("TreeStatusWidget", u"Form", None))
        self.lblBrand.setText(QCoreApplication.translate("TreeStatusWidget", u"Brand", None))
        self.lblModel.setText(QCoreApplication.translate("TreeStatusWidget", u"Model", None))
        self.label_3.setText(QCoreApplication.translate("TreeStatusWidget", u"Fahrzeugnummer", None))
        self.lblCarNum.setText(QCoreApplication.translate("TreeStatusWidget", u"00000000", None))
        self.lblPic.setText("")
    # retranslateUi

