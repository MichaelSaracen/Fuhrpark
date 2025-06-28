# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import ressources_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(367, 563)
        Login.setMinimumSize(QSize(367, 563))
        Login.setMaximumSize(QSize(367, 563))
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(300, 300))
        self.widget.setMaximumSize(QSize(300, 300))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 200))
        self.label_3.setMaximumSize(QSize(200, 200))
        self.label_3.setStyleSheet(u"border: 1px solid rgba(0,0,0,30);\n"
"border-radius: 100px;\n"
"padding: 74px;")
        self.label_3.setPixmap(QPixmap(u":/icons/customers.png"))
        self.label_3.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.leUser = QLineEdit(Login)
        self.leUser.setObjectName(u"leUser")
        self.leUser.setMinimumSize(QSize(0, 32))
        self.leUser.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout.addWidget(self.leUser)

        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.lePassword = QLineEdit(Login)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setMinimumSize(QSize(0, 32))
        self.lePassword.setMaximumSize(QSize(16777215, 32))
        self.lePassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lePassword)

        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lblError = QLabel(Login)
        self.lblError.setObjectName(u"lblError")
        font1 = QFont()
        font1.setPointSize(8)
        self.lblError.setFont(font1)
        self.lblError.setStyleSheet(u"padding-top:16px;\n"
"color: rgb(255, 43, 43);")
        self.lblError.setWordWrap(True)

        self.verticalLayout.addWidget(self.lblError)

        self.verticalSpacer_2 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btnSubmit = QPushButton(Login)
        self.btnSubmit.setObjectName(u"btnSubmit")
        self.btnSubmit.setEnabled(False)
        self.btnSubmit.setMinimumSize(QSize(0, 32))
        self.btnSubmit.setMaximumSize(QSize(16777215, 32))

        self.verticalLayout.addWidget(self.btnSubmit)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("Login", u"Benutzername", None))
        self.label.setText(QCoreApplication.translate("Login", u"Passwort", None))
        self.lblError.setText("")
        self.btnSubmit.setText(QCoreApplication.translate("Login", u"abschicken", None))
    # retranslateUi

