# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SimpleDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SimpleDialog(object):
    def setupUi(self, SimpleDialog):
        if not SimpleDialog.objectName():
            SimpleDialog.setObjectName(u"SimpleDialog")
        SimpleDialog.resize(459, 203)
        SimpleDialog.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(SimpleDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(SimpleDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(441, 185))
        self.widget.setMaximumSize(QSize(441, 185))
        self.widget.setStyleSheet(u"QWidget#widget {\n"
"	border: 1px solid rgba(0,0,0,100);\n"
"border-radius: 4px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"		background-color: none;\n"
"}\n"
"QComboBox {\n"
"			background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"QSpinBox {\n"
"			background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"			background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"QPushButton {\n"
"		background-color: none;\n"
"	padding: 0 12px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgba(0, 0, 0, 10);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.lblTitle = QLabel(self.widget)
        self.lblTitle.setObjectName(u"lblTitle")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(14)
        font.setBold(True)
        self.lblTitle.setFont(font)

        self.verticalLayout.addWidget(self.lblTitle)

        self.lblDetails = QLabel(self.widget)
        self.lblDetails.setObjectName(u"lblDetails")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(9)
        self.lblDetails.setFont(font1)
        self.lblDetails.setTextFormat(Qt.TextFormat.MarkdownText)
        self.lblDetails.setWordWrap(True)

        self.verticalLayout.addWidget(self.lblDetails)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.btnOk = QPushButton(self.widget)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setEnabled(True)
        self.btnOk.setMinimumSize(QSize(0, 32))
        self.btnOk.setMaximumSize(QSize(16777215, 32))
        self.btnOk.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btnOk)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 32))
        self.pushButton_2.setMaximumSize(QSize(16777215, 32))
        self.pushButton_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(SimpleDialog)
        self.pushButton_2.clicked.connect(SimpleDialog.close)

        QMetaObject.connectSlotsByName(SimpleDialog)
    # setupUi

    def retranslateUi(self, SimpleDialog):
        SimpleDialog.setWindowTitle(QCoreApplication.translate("SimpleDialog", u"Form", None))
        self.lblTitle.setText(QCoreApplication.translate("SimpleDialog", u"Title", None))
        self.lblDetails.setText(QCoreApplication.translate("SimpleDialog", u"<html><head/><body><p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum</p></body></html>", None))
        self.label_2.setText("")
        self.btnOk.setText(QCoreApplication.translate("SimpleDialog", u"Ok", None))
        self.pushButton_2.setText(QCoreApplication.translate("SimpleDialog", u"Abbrechen", None))
    # retranslateUi

