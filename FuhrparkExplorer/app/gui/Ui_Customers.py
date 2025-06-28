# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Customers.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QTableWidgetItem, QVBoxLayout, QWidget)

from app.widgets.buttons.IconButton import IconButton
from app.widgets.table_widgets.CustomerTable import CustomerTable
import ressources_rc

class Ui_Customers(object):
    def setupUi(self, Customers):
        if not Customers.objectName():
            Customers.setObjectName(u"Customers")
        Customers.resize(844, 768)
        self.verticalLayout_3 = QVBoxLayout(Customers)
        self.verticalLayout_3.setSpacing(32)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(64, 64, 64, 64)
        self.widget_2 = QWidget(Customers)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setContentsMargins(16, 16, 16, 16)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnSearch = IconButton(self.widget_2)
        self.btnSearch.setObjectName(u"btnSearch")
        self.btnSearch.setMinimumSize(QSize(60, 60))
        self.btnSearch.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(7)
        self.btnSearch.setFont(font1)
        self.btnSearch.setIconSize(QSize(32, 32))
        self.btnSearch.setCheckable(True)
        self.btnSearch.setChecked(True)
        self.btnSearch.setProperty(u"pixmap", QPixmap(u":/icons/search.png"))

        self.verticalLayout_2.addWidget(self.btnSearch)

        self.btnEdit = IconButton(self.widget_2)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(60, 60))
        self.btnEdit.setMaximumSize(QSize(60, 60))
        self.btnEdit.setFont(font1)
        self.btnEdit.setIconSize(QSize(32, 32))
        self.btnEdit.setCheckable(True)
        self.btnEdit.setChecked(True)
        self.btnEdit.setProperty(u"pixmap", QPixmap(u":/icons/edit.png"))

        self.verticalLayout_2.addWidget(self.btnEdit)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(False)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget = QWidget(Customers)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.leSearch = QLineEdit(self.widget)
        self.leSearch.setObjectName(u"leSearch")
        self.leSearch.setMinimumSize(QSize(0, 60))
        self.leSearch.setMaximumSize(QSize(16777215, 60))
        font2 = QFont()
        font2.setPointSize(24)
        self.leSearch.setFont(font2)
        self.leSearch.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.leSearch.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.leSearch)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.widget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout.addWidget(self.radioButton_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_3 = QWidget(Customers)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(16, 16, 16, 16)
        self.tableWidget = CustomerTable(self.widget_3)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet(u"QAbstractItemView::item:selected {\n"
"	background: rgb(188, 188, 188);\n"
"	color: black;\n"
"}")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.retranslateUi(Customers)
        self.btnSearch.clicked["bool"].connect(self.widget.setVisible)

        QMetaObject.connectSlotsByName(Customers)
    # setupUi

    def retranslateUi(self, Customers):
        Customers.setWindowTitle(QCoreApplication.translate("Customers", u"Form", None))
        self.label.setText(QCoreApplication.translate("Customers", u"# Kunden\u00fcbersicht", None))
        self.btnSearch.setText(QCoreApplication.translate("Customers", u"Suche", None))
        self.btnEdit.setText(QCoreApplication.translate("Customers", u"Edit Mode", None))
        self.label_2.setText(QCoreApplication.translate("Customers", u"<html><head/><body><p><span style=\" font-size:8pt;\">Tabellarische Kunden\u00fcbersicht.</span></p><p><span style=\" font-size:8pt;\">Der Edit - Button erlaubt es, wenn aktiviert, einzelne Spalten der Kunden zu ver\u00e4ndern.</span></p><p><span style=\" font-size:8pt;\">Der Such - Button setzt die Suchleiste auf Sichtbar/Unsichtbar.</span></p><p><span style=\" font-size:8pt;\">In der Suchleiste kannst du nach Kriterien Filtern und somit gezielter nach bestimmten Kunden Suchen.</span></p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate("Customers", u"Kundennummer", None))
        self.radioButton_2.setText(QCoreApplication.translate("Customers", u"Vorname", None))
        self.radioButton_3.setText(QCoreApplication.translate("Customers", u"Nachname", None))
        self.radioButton_4.setText(QCoreApplication.translate("Customers", u"IBAN", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Customers", u"Kundennummer", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Customers", u"Vorname", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Customers", u"Nachname", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Customers", u"Alter", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Customers", u"Telefon", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Customers", u"Stadt", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Customers", u"PLZ", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Customers", u"Strasse", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Customers", u"Hausnummer", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Customers", u"IBAN", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Customers", u"Kreditinstitut", None));
    # retranslateUi

