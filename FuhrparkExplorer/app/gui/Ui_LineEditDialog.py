# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LineEditDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)
import ressources_rc

class Ui_LineEditDialog(object):
    def setupUi(self, LineEditDialog):
        if not LineEditDialog.objectName():
            LineEditDialog.setObjectName(u"LineEditDialog")
        LineEditDialog.resize(665, 219)
        LineEditDialog.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(LineEditDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(LineEditDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(450, 201))
        self.widget.setMaximumSize(QSize(450, 201))
        self.widget.setStyleSheet(u"QWidget#widget {\n"
"	border: 1px solid rgba(0,0,0,100);\n"
"border-radius: 4px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QComboBox {\n"
" padding-left: 8px;\n"
"			background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"		border: 1px solid rgba(0,0,0,50);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QAbstractItemView::item {\n"
"    padding-left: 8px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"	padding-left: 8px;\n"
"			background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"	padding-left: 8px;\n"
"			background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding-left: 8px;\n"
"	background: rgba(0,0,0,10);\n"
"}\n"
"\n"
"QLabel{\n"
"		background-color: none;\n"
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
"	color: rgb(0, 0,"
                        " 0);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"	background-color: rgba(0, 0, 0, 20);\n"
"	color: rgb(0, 0, 0);\n"
"}")
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

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.aktuellLabel = QLabel(self.widget)
        self.aktuellLabel.setObjectName(u"aktuellLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.aktuellLabel)

        self.leOldValue = QLineEdit(self.widget)
        self.leOldValue.setObjectName(u"leOldValue")
        self.leOldValue.setMinimumSize(QSize(0, 32))
        self.leOldValue.setMaximumSize(QSize(16777215, 32))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(9)
        self.leOldValue.setFont(font1)
        self.leOldValue.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.leOldValue)

        self.neuLabel = QLabel(self.widget)
        self.neuLabel.setObjectName(u"neuLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.neuLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leNewValue = QLineEdit(self.widget)
        self.leNewValue.setObjectName(u"leNewValue")
        self.leNewValue.setMinimumSize(QSize(0, 32))
        self.leNewValue.setMaximumSize(QSize(16777215, 32))
        self.leNewValue.setFont(font1)

        self.horizontalLayout.addWidget(self.leNewValue)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 32))
        self.comboBox.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout.addWidget(self.comboBox)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 32))
        self.spinBox.setMaximumSize(QSize(16777215, 32))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(9999)

        self.horizontalLayout.addWidget(self.spinBox)

        self.doubleSpinBox = QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimumSize(QSize(0, 32))
        self.doubleSpinBox.setMaximumSize(QSize(16777215, 32))
        self.doubleSpinBox.setMinimum(1000.000000000000000)
        self.doubleSpinBox.setMaximum(9999999.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.btnLoadImage = QPushButton(self.widget)
        self.btnLoadImage.setObjectName(u"btnLoadImage")
        self.btnLoadImage.setMinimumSize(QSize(32, 32))
        self.btnLoadImage.setMaximumSize(QSize(32, 32))
        self.btnLoadImage.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/more.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLoadImage.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnLoadImage)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.btnSave = QPushButton(self.widget)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setEnabled(False)
        self.btnSave.setMinimumSize(QSize(0, 32))
        self.btnSave.setMaximumSize(QSize(16777215, 32))
        self.btnSave.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btnSave)

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


        self.retranslateUi(LineEditDialog)
        self.pushButton_2.clicked.connect(LineEditDialog.close)

        QMetaObject.connectSlotsByName(LineEditDialog)
    # setupUi

    def retranslateUi(self, LineEditDialog):
        LineEditDialog.setWindowTitle(QCoreApplication.translate("LineEditDialog", u"Form", None))
        self.lblTitle.setText(QCoreApplication.translate("LineEditDialog", u"Title", None))
        self.aktuellLabel.setText(QCoreApplication.translate("LineEditDialog", u"Aktuell", None))
        self.neuLabel.setText(QCoreApplication.translate("LineEditDialog", u"Neu", None))
        self.btnLoadImage.setText("")
        self.label_2.setText("")
        self.btnSave.setText(QCoreApplication.translate("LineEditDialog", u"Speichern", None))
        self.pushButton_2.setText(QCoreApplication.translate("LineEditDialog", u"Abbrechen", None))
    # retranslateUi

