# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hraiNaDnx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(640, 490, 141, 61))
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.pushButton.setPalette(palette)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 490, 141, 61))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.pushButton_2.setPalette(palette1)
        self.pushButton_2.setFont(font)
        self.labelOtazka = QLabel(self.centralwidget)
        self.labelOtazka.setObjectName(u"labelOtazka")
        self.labelOtazka.setGeometry(QRect(10, 130, 781, 191))
        font1 = QFont()
        font1.setPointSize(14)
        self.labelOtazka.setFont(font1)
        self.labelOtazka.setFrameShape(QFrame.WinPanel)
        self.labelOdpoved = QLabel(self.centralwidget)
        self.labelOdpoved.setObjectName(u"labelOdpoved")
        self.labelOdpoved.setGeometry(QRect(10, 340, 781, 131))
        self.labelOdpoved.setFont(font1)
        self.labelOdpoved.setFrameShape(QFrame.WinPanel)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 21))
        font2 = QFont()
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 91, 21))
        self.label_2.setFont(font2)
        self.label_T1Body = QLabel(self.centralwidget)
        self.label_T1Body.setObjectName(u"label_T1Body")
        self.label_T1Body.setGeometry(QRect(90, 10, 91, 21))
        self.label_T1Body.setFont(font2)
        self.label_T2Body = QLabel(self.centralwidget)
        self.label_T2Body.setObjectName(u"label_T2Body")
        self.label_T2Body.setGeometry(QRect(90, 30, 80, 21))
        self.label_T2Body.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 90, 211, 21))
        self.label_3.setFont(font2)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 490, 141, 61))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.pushButton_3.setPalette(palette2)
        self.pushButton_3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Dal\u0161\u00ed ot\u00e1zka", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Konec", None))
        self.labelOtazka.setText("")
        self.labelOdpoved.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"T\u00fdm 1 : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T\u00fdm 2 : ", None))
        self.label_T1Body.setText(QCoreApplication.translate("MainWindow", u"0b.", None))
        self.label_T2Body.setText(QCoreApplication.translate("MainWindow", u"0b.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u010cEK\u00c1N\u00cd NA ODPOV\u011a\u010e", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"+1", None))
    # retranslateUi

