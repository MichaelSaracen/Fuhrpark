# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddCustomerDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_AddCustomerDialog(object):
    def setupUi(self, AddCustomerDialog):
        if not AddCustomerDialog.objectName():
            AddCustomerDialog.setObjectName(u"AddCustomerDialog")
        AddCustomerDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        AddCustomerDialog.resize(629, 497)
        AddCustomerDialog.setMinimumSize(QSize(629, 497))
        AddCustomerDialog.setMaximumSize(QSize(629, 497))
        AddCustomerDialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(AddCustomerDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(AddCustomerDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_10.setFont(font)

        self.verticalLayout_2.addWidget(self.label_10)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.vornameLabel_3 = QLabel(self.widget)
        self.vornameLabel_3.setObjectName(u"vornameLabel_3")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setBold(True)
        self.vornameLabel_3.setFont(font1)
        self.vornameLabel_3.setStyleSheet(u"padding-top: 16px;")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.vornameLabel_3)

        self.vornameLabel_4 = QLabel(self.widget)
        self.vornameLabel_4.setObjectName(u"vornameLabel_4")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        self.vornameLabel_4.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.vornameLabel_4)

        self.leFirstName_2 = QLineEdit(self.widget)
        self.leFirstName_2.setObjectName(u"leFirstName_2")
        self.leFirstName_2.setMinimumSize(QSize(520, 32))
        self.leFirstName_2.setMaximumSize(QSize(16777215, 32))
        self.leFirstName_2.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.leFirstName_2)

        self.nachnameLabel_3 = QLabel(self.widget)
        self.nachnameLabel_3.setObjectName(u"nachnameLabel_3")
        self.nachnameLabel_3.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.nachnameLabel_3)

        self.leLastName_2 = QLineEdit(self.widget)
        self.leLastName_2.setObjectName(u"leLastName_2")
        self.leLastName_2.setMinimumSize(QSize(0, 32))
        self.leLastName_2.setMaximumSize(QSize(16777215, 32))
        self.leLastName_2.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.leLastName_2)

        self.alterLabel_2 = QLabel(self.widget)
        self.alterLabel_2.setObjectName(u"alterLabel_2")
        self.alterLabel_2.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.alterLabel_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sbAge_2 = QSpinBox(self.widget)
        self.sbAge_2.setObjectName(u"sbAge_2")
        self.sbAge_2.setMinimumSize(QSize(80, 32))
        self.sbAge_2.setMaximumSize(QSize(80, 32))
        self.sbAge_2.setFont(font2)
        self.sbAge_2.setMinimum(18)
        self.sbAge_2.setMaximum(90)

        self.horizontalLayout_3.addWidget(self.sbAge_2)

        self.nachnameLabel_4 = QLabel(self.widget)
        self.nachnameLabel_4.setObjectName(u"nachnameLabel_4")
        self.nachnameLabel_4.setFont(font2)

        self.horizontalLayout_3.addWidget(self.nachnameLabel_4)

        self.leTelefon_2 = QLineEdit(self.widget)
        self.leTelefon_2.setObjectName(u"leTelefon_2")
        self.leTelefon_2.setMinimumSize(QSize(0, 32))
        self.leTelefon_2.setMaximumSize(QSize(16777215, 32))
        self.leTelefon_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.leTelefon_2)


        self.formLayout_2.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_3)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"padding-top: 16px;")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.wohnortLabel_2 = QLabel(self.widget)
        self.wohnortLabel_2.setObjectName(u"wohnortLabel_2")
        self.wohnortLabel_2.setFont(font2)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.wohnortLabel_2)

        self.leCity_2 = QLineEdit(self.widget)
        self.leCity_2.setObjectName(u"leCity_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leCity_2.sizePolicy().hasHeightForWidth())
        self.leCity_2.setSizePolicy(sizePolicy)
        self.leCity_2.setMinimumSize(QSize(0, 32))
        self.leCity_2.setMaximumSize(QSize(16777215, 32))
        self.leCity_2.setFont(font2)

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.leCity_2)

        self.pLZLabel_2 = QLabel(self.widget)
        self.pLZLabel_2.setObjectName(u"pLZLabel_2")
        self.pLZLabel_2.setFont(font2)

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.pLZLabel_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leZip_2 = QLineEdit(self.widget)
        self.leZip_2.setObjectName(u"leZip_2")
        self.leZip_2.setMinimumSize(QSize(80, 32))
        self.leZip_2.setMaximumSize(QSize(80, 32))
        self.leZip_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.leZip_2)

        self.strasseLabel_2 = QLabel(self.widget)
        self.strasseLabel_2.setObjectName(u"strasseLabel_2")
        self.strasseLabel_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.strasseLabel_2)

        self.leStreet_2 = QLineEdit(self.widget)
        self.leStreet_2.setObjectName(u"leStreet_2")
        self.leStreet_2.setMinimumSize(QSize(0, 32))
        self.leStreet_2.setMaximumSize(QSize(16777215, 32))
        self.leStreet_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.leStreet_2)

        self.hausnummerLabel_2 = QLabel(self.widget)
        self.hausnummerLabel_2.setObjectName(u"hausnummerLabel_2")
        self.hausnummerLabel_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.hausnummerLabel_2)

        self.leHouseNr_2 = QLineEdit(self.widget)
        self.leHouseNr_2.setObjectName(u"leHouseNr_2")
        self.leHouseNr_2.setMinimumSize(QSize(0, 32))
        self.leHouseNr_2.setMaximumSize(QSize(80, 32))
        self.leHouseNr_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.leHouseNr_2)


        self.formLayout_2.setLayout(6, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_4)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"padding-top: 16px;")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.institutLabel_2 = QLabel(self.widget)
        self.institutLabel_2.setObjectName(u"institutLabel_2")
        self.institutLabel_2.setFont(font2)

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.LabelRole, self.institutLabel_2)

        self.institutLineEdit_2 = QLineEdit(self.widget)
        self.institutLineEdit_2.setObjectName(u"institutLineEdit_2")
        self.institutLineEdit_2.setMinimumSize(QSize(0, 32))
        self.institutLineEdit_2.setMaximumSize(QSize(16777215, 32))
        self.institutLineEdit_2.setFont(font2)

        self.formLayout_2.setWidget(8, QFormLayout.ItemRole.FieldRole, self.institutLineEdit_2)

        self.iBANLabel_2 = QLabel(self.widget)
        self.iBANLabel_2.setObjectName(u"iBANLabel_2")
        self.iBANLabel_2.setFont(font2)

        self.formLayout_2.setWidget(9, QFormLayout.ItemRole.LabelRole, self.iBANLabel_2)

        self.iBANLineEdit_2 = QLineEdit(self.widget)
        self.iBANLineEdit_2.setObjectName(u"iBANLineEdit_2")
        self.iBANLineEdit_2.setMinimumSize(QSize(0, 32))
        self.iBANLineEdit_2.setMaximumSize(QSize(16777215, 32))
        self.iBANLineEdit_2.setFont(font2)

        self.formLayout_2.setWidget(9, QFormLayout.ItemRole.FieldRole, self.iBANLineEdit_2)


        self.verticalLayout_2.addLayout(self.formLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(9)
        self.label_13.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.btnSave = QPushButton(self.widget)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setEnabled(False)
        self.btnSave.setMinimumSize(QSize(0, 32))
        self.btnSave.setMaximumSize(QSize(16777215, 32))
        self.btnSave.setFont(font3)

        self.horizontalLayout_7.addWidget(self.btnSave)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 32))
        self.pushButton_2.setMaximumSize(QSize(16777215, 32))
        self.pushButton_2.setFont(font3)

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.horizontalLayout_7.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(AddCustomerDialog)
        self.pushButton_2.clicked.connect(AddCustomerDialog.close)

        QMetaObject.connectSlotsByName(AddCustomerDialog)
    # setupUi

    def retranslateUi(self, AddCustomerDialog):
        AddCustomerDialog.setWindowTitle(QCoreApplication.translate("AddCustomerDialog", u"Kunden hinzuf\u00fcgen", None))
        self.label_10.setText(QCoreApplication.translate("AddCustomerDialog", u"Kunden hinzuf\u00fcgen", None))
        self.vornameLabel_3.setText(QCoreApplication.translate("AddCustomerDialog", u"Allgemein", None))
        self.vornameLabel_4.setText(QCoreApplication.translate("AddCustomerDialog", u"Vorname", None))
        self.nachnameLabel_3.setText(QCoreApplication.translate("AddCustomerDialog", u"Nachname", None))
        self.alterLabel_2.setText(QCoreApplication.translate("AddCustomerDialog", u"Alter", None))
        self.nachnameLabel_4.setText(QCoreApplication.translate("AddCustomerDialog", u"Telefon", None))
        self.label_11.setText(QCoreApplication.translate("AddCustomerDialog", u"Wohnhaft", None))
        self.wohnortLabel_2.setText(QCoreApplication.translate("AddCustomerDialog", u"Wohnort", None))
        self.pLZLabel_2.setText(QCoreApplication.translate("AddCustomerDialog", u"PLZ", None))
        self.strasseLabel_2.setText(QCoreApplication.translate("AddCustomerDialog", u"Strasse", None))
        self.hausnummerLabel_2.setText(QCoreApplication.translate("AddCustomerDialog", u"Hnr", None))
        self.label_12.setText(QCoreApplication.translate("AddCustomerDialog", u"Kontodaten", None))
        self.institutLabel_2.setText(QCoreApplication.translate("AddCustomerDialog", u"Institut", None))
        self.iBANLabel_2.setText(QCoreApplication.translate("AddCustomerDialog", u"IBAN", None))
        self.label_13.setText("")
        self.btnSave.setText(QCoreApplication.translate("AddCustomerDialog", u"Speichern", None))
        self.pushButton_2.setText(QCoreApplication.translate("AddCustomerDialog", u"Abbrechen", None))
    # retranslateUi

