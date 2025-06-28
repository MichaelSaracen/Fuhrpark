# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RentCustomerWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_RentCustomerWidget(object):
    def setupUi(self, RentCustomerWidget):
        if not RentCustomerWidget.objectName():
            RentCustomerWidget.setObjectName(u"RentCustomerWidget")
        RentCustomerWidget.resize(485, 616)
        self.verticalLayout = QVBoxLayout(RentCustomerWidget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.lineEdit = QLineEdit(RentCustomerWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 32))
        self.lineEdit.setMaximumSize(QSize(16777215, 32))
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(RentCustomerWidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(RentCustomerWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(RentCustomerWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.listWidget = QListWidget(RentCustomerWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(RentCustomerWidget)

        QMetaObject.connectSlotsByName(RentCustomerWidget)
    # setupUi

    def retranslateUi(self, RentCustomerWidget):
        RentCustomerWidget.setWindowTitle(QCoreApplication.translate("RentCustomerWidget", u"Form", None))
        self.radioButton.setText(QCoreApplication.translate("RentCustomerWidget", u"Vorname", None))
        self.radioButton_2.setText(QCoreApplication.translate("RentCustomerWidget", u"Nachname", None))
        self.radioButton_3.setText(QCoreApplication.translate("RentCustomerWidget", u"Telefon", None))
    # retranslateUi

