# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mitgobla\Documents\GitHub\SmartMirror\pimirror\widgets\internet_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

CWD = os.path.dirname(os.path.realpath(__file__))

class Ui_internet_widget(object):
    def setupUi(self, internet_widget):
        internet_widget.setObjectName("internet_widget")
        internet_widget.resize(320, 110)
        internet_widget.setMinimumSize(QtCore.QSize(320, 110))
        internet_widget.setMaximumSize(QtCore.QSize(320, 110))
        internet_widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_mirroricon = QtWidgets.QLabel(internet_widget)
        self.label_mirroricon.setGeometry(QtCore.QRect(0, 10, 61, 61))
        self.label_mirroricon.setText("")
        self.label_mirroricon.setPixmap(QtGui.QPixmap(os.path.join(CWD, "..", "resources", "icons", "mirror.png")))
        self.label_mirroricon.setScaledContents(True)
        self.label_mirroricon.setObjectName("label_mirroricon")
        self.label_arrow_1 = QtWidgets.QLabel(internet_widget)
        self.label_arrow_1.setGeometry(QtCore.QRect(70, 10, 51, 61))
        self.label_arrow_1.setText("")
        self.label_arrow_1.setPixmap(QtGui.QPixmap(os.path.join(CWD, "..", "resources", "icons", "arrows/right.png")))
        self.label_arrow_1.setScaledContents(True)
        self.label_arrow_1.setObjectName("label_arrow_1")
        self.label_statusicon = QtWidgets.QLabel(internet_widget)
        self.label_statusicon.setGeometry(QtCore.QRect(130, 10, 51, 51))
        self.label_statusicon.setText("")
        self.label_statusicon.setPixmap(QtGui.QPixmap(os.path.join(CWD, "..", "resources", "icons", "check/yes.png")))
        self.label_statusicon.setScaledContents(True)
        self.label_statusicon.setObjectName("label_statusicon")
        self.label_arrow_2 = QtWidgets.QLabel(internet_widget)
        self.label_arrow_2.setGeometry(QtCore.QRect(190, 10, 51, 61))
        self.label_arrow_2.setText("")
        self.label_arrow_2.setPixmap(QtGui.QPixmap(os.path.join(CWD, "..", "resources", "icons", "arrows/right.png")))
        self.label_arrow_2.setScaledContents(True)
        self.label_arrow_2.setObjectName("label_arrow_2")
        self.label_interneticon = QtWidgets.QLabel(internet_widget)
        self.label_interneticon.setGeometry(QtCore.QRect(250, 10, 61, 61))
        self.label_interneticon.setText("")
        self.label_interneticon.setPixmap(QtGui.QPixmap(os.path.join(CWD, "..", "resources", "icons", "internet.png")))
        self.label_interneticon.setScaledContents(True)
        self.label_interneticon.setObjectName("label_interneticon")
        self.label_status = QtWidgets.QLabel(internet_widget)
        self.label_status.setGeometry(QtCore.QRect(0, 69, 320, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_status.setObjectName("label_status")
        self.label_mirroricon.raise_()
        self.label_statusicon.raise_()
        self.label_arrow_2.raise_()
        self.label_interneticon.raise_()
        self.label_status.raise_()
        self.label_arrow_1.raise_()

        self.retranslateUi(internet_widget)
        QtCore.QMetaObject.connectSlotsByName(internet_widget)

    def retranslateUi(self, internet_widget):
        _translate = QtCore.QCoreApplication.translate
        self.label_status.setText(_translate("internet_widget", "<html><head/><body><p><span style=\" font-size:14pt;\">Connected</span></p></body></html>"))

