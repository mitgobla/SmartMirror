# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mitgobla\Documents\GitHub\SmartMirror\pimirror\widgets\clock_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_clock_widget(object):
    def setupUi(self, clock_widget):
        clock_widget.setObjectName("clock_widget")
        clock_widget.resize(320, 100)
        clock_widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_date = QtWidgets.QLabel(clock_widget)
        self.label_date.setGeometry(QtCore.QRect(0, 60, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.label_time = QtWidgets.QLabel(clock_widget)
        self.label_time.setGeometry(QtCore.QRect(0, 0, 320, 60))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(35)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")

        self.retranslateUi(clock_widget)
        QtCore.QMetaObject.connectSlotsByName(clock_widget)

    def retranslateUi(self, clock_widget):
        _translate = QtCore.QCoreApplication.translate
        self.label_date.setText(_translate("clock_widget", "<html><head/><body><p><span style=\" font-size:14pt;\">Wednesday 31</span><span style=\" font-size:14pt; vertical-align:super;\">st</span><span style=\" font-size:14pt;\">, September, 2019</span></p></body></html>"))
        self.label_time.setText(_translate("clock_widget", "<html><head/><body><p><span style=\" font-size:32pt;\">00:00</span><span style=\" font-size:22pt;\"> am</span></p></body></html>"))

