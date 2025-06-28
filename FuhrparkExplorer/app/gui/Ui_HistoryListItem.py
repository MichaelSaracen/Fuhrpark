# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HistoryListItem.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_HistoryListItem(object):
    def setupUi(self, HistoryListItem):
        if not HistoryListItem.objectName():
            HistoryListItem.setObjectName(u"HistoryListItem")
        HistoryListItem.resize(1102, 43)
        HistoryListItem.setStyleSheet(u"border: 0px;\n"
"background: none;")
        self.gridLayout = QGridLayout(HistoryListItem)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.lblBrand = QLabel(HistoryListItem)
        self.lblBrand.setObjectName(u"lblBrand")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        self.lblBrand.setFont(font)
        self.lblBrand.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.gridLayout.addWidget(self.lblBrand, 0, 0, 1, 1)

        self.lblModel = QLabel(HistoryListItem)
        self.lblModel.setObjectName(u"lblModel")
        self.lblModel.setFont(font)
        self.lblModel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.lblModel, 0, 1, 1, 1)

        self.lblPrice = QLabel(HistoryListItem)
        self.lblPrice.setObjectName(u"lblPrice")
        self.lblPrice.setFont(font)
        self.lblPrice.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.lblPrice, 0, 2, 1, 1)

        self.lblDateFrom = QLabel(HistoryListItem)
        self.lblDateFrom.setObjectName(u"lblDateFrom")
        self.lblDateFrom.setMinimumSize(QSize(0, 0))
        self.lblDateFrom.setFont(font)
        self.lblDateFrom.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.lblDateFrom, 0, 3, 1, 1)

        self.lblDateTo = QLabel(HistoryListItem)
        self.lblDateTo.setObjectName(u"lblDateTo")
        self.lblDateTo.setFont(font)
        self.lblDateTo.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout.addWidget(self.lblDateTo, 0, 4, 1, 1)

        self.label_4 = QLabel(HistoryListItem)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(7)
        font1.setBold(False)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(HistoryListItem)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_6 = QLabel(HistoryListItem)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_7 = QLabel(HistoryListItem)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)

        self.label_8 = QLabel(HistoryListItem)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(0, 20))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout.addWidget(self.label_8, 1, 4, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowMinimumHeight(1, 1)

        self.retranslateUi(HistoryListItem)

        QMetaObject.connectSlotsByName(HistoryListItem)
    # setupUi

    def retranslateUi(self, HistoryListItem):
        HistoryListItem.setWindowTitle(QCoreApplication.translate("HistoryListItem", u"Form", None))
        self.lblBrand.setText(QCoreApplication.translate("HistoryListItem", u"Brand", None))
        self.lblModel.setText(QCoreApplication.translate("HistoryListItem", u"Model", None))
        self.lblPrice.setText(QCoreApplication.translate("HistoryListItem", u"Price", None))
        self.lblDateFrom.setText(QCoreApplication.translate("HistoryListItem", u"Datum", None))
        self.lblDateTo.setText(QCoreApplication.translate("HistoryListItem", u"Datum", None))
        self.label_4.setText(QCoreApplication.translate("HistoryListItem", u"Marke", None))
        self.label_5.setText(QCoreApplication.translate("HistoryListItem", u"Modell", None))
        self.label_6.setText(QCoreApplication.translate("HistoryListItem", u"Preis", None))
        self.label_7.setText(QCoreApplication.translate("HistoryListItem", u"Ausleihdatum", None))
        self.label_8.setText(QCoreApplication.translate("HistoryListItem", u"R\u00fcckgabedatum", None))
    # retranslateUi

