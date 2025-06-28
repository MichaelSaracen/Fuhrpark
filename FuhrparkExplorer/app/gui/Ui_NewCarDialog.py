# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewCarDialog.ui'
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
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

from app.widgets.buttons.IconButton import IconButton
import ressources_rc

class Ui_NewCarDialog(object):
    def setupUi(self, NewCarDialog):
        if not NewCarDialog.objectName():
            NewCarDialog.setObjectName(u"NewCarDialog")
        NewCarDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        NewCarDialog.resize(680, 550)
        NewCarDialog.setMinimumSize(QSize(680, 550))
        NewCarDialog.setMaximumSize(QSize(680, 550))
        NewCarDialog.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(NewCarDialog)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(NewCarDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(680, 550))
        self.widget.setMaximumSize(QSize(680, 550))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(16, 16, 16, 16)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 1))
        self.line_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 15);")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.markeLabel = QLabel(self.widget)
        self.markeLabel.setObjectName(u"markeLabel")
        self.markeLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.markeLabel)

        self.cbBrand = QComboBox(self.widget)
        self.cbBrand.setObjectName(u"cbBrand")
        self.cbBrand.setMinimumSize(QSize(0, 32))
        self.cbBrand.setMaximumSize(QSize(16777215, 32))
        self.cbBrand.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.cbBrand)

        self.modellLabel = QLabel(self.widget)
        self.modellLabel.setObjectName(u"modellLabel")
        self.modellLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.modellLabel)

        self.leModel = QLineEdit(self.widget)
        self.leModel.setObjectName(u"leModel")
        self.leModel.setMinimumSize(QSize(0, 32))
        self.leModel.setMaximumSize(QSize(16777215, 32))
        self.leModel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.leModel)

        self.getriebeLabel = QLabel(self.widget)
        self.getriebeLabel.setObjectName(u"getriebeLabel")
        self.getriebeLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.getriebeLabel)

        self.cbGearbox = QComboBox(self.widget)
        self.cbGearbox.setObjectName(u"cbGearbox")
        self.cbGearbox.setMinimumSize(QSize(0, 32))
        self.cbGearbox.setMaximumSize(QSize(16777215, 32))
        self.cbGearbox.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cbGearbox)

        self.kraftstoffLabel = QLabel(self.widget)
        self.kraftstoffLabel.setObjectName(u"kraftstoffLabel")
        self.kraftstoffLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.kraftstoffLabel)

        self.cbFuel = QComboBox(self.widget)
        self.cbFuel.setObjectName(u"cbFuel")
        self.cbFuel.setMinimumSize(QSize(0, 32))
        self.cbFuel.setMaximumSize(QSize(16777215, 32))
        self.cbFuel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cbFuel)

        self.leistungLabel = QLabel(self.widget)
        self.leistungLabel.setObjectName(u"leistungLabel")
        self.leistungLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.leistungLabel)

        self.sbPower = QSpinBox(self.widget)
        self.sbPower.setObjectName(u"sbPower")
        self.sbPower.setMinimumSize(QSize(0, 32))
        self.sbPower.setMaximumSize(QSize(16777215, 32))
        self.sbPower.setFont(font)
        self.sbPower.setMinimum(30)
        self.sbPower.setMaximum(2000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.sbPower)

        self.verbrauchgLabel = QLabel(self.widget)
        self.verbrauchgLabel.setObjectName(u"verbrauchgLabel")
        self.verbrauchgLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.verbrauchgLabel)

        self.sbConsum = QSpinBox(self.widget)
        self.sbConsum.setObjectName(u"sbConsum")
        self.sbConsum.setMinimumSize(QSize(0, 32))
        self.sbConsum.setMaximumSize(QSize(16777215, 32))
        self.sbConsum.setFont(font)
        self.sbConsum.setMinimum(1)
        self.sbConsum.setMaximum(100)
        self.sbConsum.setValue(10)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.sbConsum)

        self.tRenLabel = QLabel(self.widget)
        self.tRenLabel.setObjectName(u"tRenLabel")
        self.tRenLabel.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.tRenLabel)

        self.sbDoors = QSpinBox(self.widget)
        self.sbDoors.setObjectName(u"sbDoors")
        self.sbDoors.setMinimumSize(QSize(0, 32))
        self.sbDoors.setMaximumSize(QSize(16777215, 32))
        self.sbDoors.setFont(font)
        self.sbDoors.setMinimum(1)
        self.sbDoors.setMaximum(10)
        self.sbDoors.setValue(4)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.sbDoors)

        self.sitzeLabel = QLabel(self.widget)
        self.sitzeLabel.setObjectName(u"sitzeLabel")
        self.sitzeLabel.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.sitzeLabel)

        self.sbSeats = QSpinBox(self.widget)
        self.sbSeats.setObjectName(u"sbSeats")
        self.sbSeats.setMinimumSize(QSize(0, 32))
        self.sbSeats.setMaximumSize(QSize(16777215, 32))
        self.sbSeats.setFont(font)
        self.sbSeats.setMinimum(1)
        self.sbSeats.setMaximum(20)
        self.sbSeats.setValue(4)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.sbSeats)

        self.farbeLabel = QLabel(self.widget)
        self.farbeLabel.setObjectName(u"farbeLabel")
        self.farbeLabel.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.farbeLabel)

        self.leColor = QLineEdit(self.widget)
        self.leColor.setObjectName(u"leColor")
        self.leColor.setMinimumSize(QSize(0, 32))
        self.leColor.setMaximumSize(QSize(16777215, 32))
        self.leColor.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.leColor)

        self.grundpreisLabel = QLabel(self.widget)
        self.grundpreisLabel.setObjectName(u"grundpreisLabel")
        self.grundpreisLabel.setFont(font)

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.grundpreisLabel)

        self.sbPrice = QDoubleSpinBox(self.widget)
        self.sbPrice.setObjectName(u"sbPrice")
        self.sbPrice.setMinimumSize(QSize(0, 32))
        self.sbPrice.setMaximumSize(QSize(16777215, 32))
        self.sbPrice.setFont(font)
        self.sbPrice.setMaximum(9999999.990000000223517)
        self.sbPrice.setValue(10000.000000000000000)

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.sbPrice)


        self.horizontalLayout_3.addLayout(self.formLayout)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setFont(font)
        self.line.setStyleSheet(u"background-color: rgba(0, 0, 0, 15);\n"
"width: 1px;")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.btnLoadImage = IconButton(self.widget)
        self.btnLoadImage.setObjectName(u"btnLoadImage")
        self.btnLoadImage.setMinimumSize(QSize(32, 32))
        self.btnLoadImage.setMaximumSize(QSize(32, 32))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(7)
        self.btnLoadImage.setFont(font3)
        self.btnLoadImage.setIconSize(QSize(24, 24))
        self.btnLoadImage.setCheckable(False)
        self.btnLoadImage.setChecked(False)
        self.btnLoadImage.setProperty(u"pixmap", QPixmap(u":/icons/more.png"))

        self.horizontalLayout.addWidget(self.btnLoadImage)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lblImage = QLabel(self.widget)
        self.lblImage.setObjectName(u"lblImage")
        self.lblImage.setMinimumSize(QSize(340, 340))
        self.lblImage.setMaximumSize(QSize(340, 340))
        self.lblImage.setFont(font)
        self.lblImage.setScaledContents(False)

        self.verticalLayout.addWidget(self.lblImage)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setFont(font)
        self.line_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 15);")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.btnSave = IconButton(self.widget)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setEnabled(False)
        self.btnSave.setMinimumSize(QSize(0, 32))
        self.btnSave.setMaximumSize(QSize(16777215, 32))
        self.btnSave.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnSave)

        self.pushButton_2 = IconButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 32))
        self.pushButton_2.setMaximumSize(QSize(16777215, 32))
        self.pushButton_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(NewCarDialog)
        self.pushButton_2.clicked.connect(NewCarDialog.close)

        QMetaObject.connectSlotsByName(NewCarDialog)
    # setupUi

    def retranslateUi(self, NewCarDialog):
        NewCarDialog.setWindowTitle(QCoreApplication.translate("NewCarDialog", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("NewCarDialog", u"Fahrzeug hinzuf\u00fcgen", None))
        self.markeLabel.setText(QCoreApplication.translate("NewCarDialog", u"Marke", None))
        self.modellLabel.setText(QCoreApplication.translate("NewCarDialog", u"Modell", None))
        self.getriebeLabel.setText(QCoreApplication.translate("NewCarDialog", u"Getriebe", None))
        self.kraftstoffLabel.setText(QCoreApplication.translate("NewCarDialog", u"Kraftstoff", None))
        self.leistungLabel.setText(QCoreApplication.translate("NewCarDialog", u"Leistung (PS)", None))
        self.verbrauchgLabel.setText(QCoreApplication.translate("NewCarDialog", u"Verbrauch", None))
        self.tRenLabel.setText(QCoreApplication.translate("NewCarDialog", u"T\u00fcren", None))
        self.sitzeLabel.setText(QCoreApplication.translate("NewCarDialog", u"Sitze", None))
        self.farbeLabel.setText(QCoreApplication.translate("NewCarDialog", u"Farbe", None))
        self.grundpreisLabel.setText(QCoreApplication.translate("NewCarDialog", u"Grundpreis (\u20ac)", None))
        self.label.setText(QCoreApplication.translate("NewCarDialog", u"Bild ausw\u00e4hlen", None))
        self.btnLoadImage.setText("")
        self.lblImage.setText("")
        self.label_2.setText("")
        self.btnSave.setText(QCoreApplication.translate("NewCarDialog", u"Speichern", None))
        self.pushButton_2.setText(QCoreApplication.translate("NewCarDialog", u"Abbrechen", None))
    # retranslateUi

