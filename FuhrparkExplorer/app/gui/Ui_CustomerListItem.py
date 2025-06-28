# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomerListItem.ui'
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

class Ui_CustomerListItem(object):
    def setupUi(self, CustomerListItem):
        if not CustomerListItem.objectName():
            CustomerListItem.setObjectName(u"CustomerListItem")
        CustomerListItem.resize(570, 24)
        CustomerListItem.setMinimumSize(QSize(0, 24))
        CustomerListItem.setMaximumSize(QSize(16777215, 32))
        self.horizontalLayout = QHBoxLayout(CustomerListItem)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.lblFirstname = QLabel(CustomerListItem)
        self.lblFirstname.setObjectName(u"lblFirstname")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(False)
        self.lblFirstname.setFont(font)
        self.lblFirstname.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.lblFirstname)

        self.lblLastname = QLabel(CustomerListItem)
        self.lblLastname.setObjectName(u"lblLastname")
        self.lblLastname.setFont(font)
        self.lblLastname.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout.addWidget(self.lblLastname)

        self.lblPhone = QLabel(CustomerListItem)
        self.lblPhone.setObjectName(u"lblPhone")
        self.lblPhone.setMinimumSize(QSize(0, 24))
        self.lblPhone.setFont(font)
        self.lblPhone.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.horizontalLayout.addWidget(self.lblPhone)

        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(CustomerListItem)

        QMetaObject.connectSlotsByName(CustomerListItem)
    # setupUi

    def retranslateUi(self, CustomerListItem):
        CustomerListItem.setWindowTitle(QCoreApplication.translate("CustomerListItem", u"Form", None))
        self.lblFirstname.setText(QCoreApplication.translate("CustomerListItem", u"Vorname", None))
        self.lblLastname.setText(QCoreApplication.translate("CustomerListItem", u"Nachname", None))
        self.lblPhone.setText(QCoreApplication.translate("CustomerListItem", u"Telefon", None))
    # retranslateUi

