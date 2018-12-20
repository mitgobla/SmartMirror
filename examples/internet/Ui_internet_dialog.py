# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mitgobla\Documents\GitHub\SmartMirror\examples\internet\internet_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import http.client as httplib
from time import sleep

class Connection(QtCore.QObject):
    """Connection Related Functions
    """

    connection_signal = QtCore.pyqtSignal(bool)

    @QtCore.pyqtSlot()
    def check_connection(self):
        """Check internet connection
        """

        while True:
            conn = httplib.HTTPConnection("www.google.com", timeout=5)
            try:
                conn.request("HEAD", "/")
                conn.close()
                self.connection_signal.emit(True)
            except:
                conn.close()
                self.connection_signal.emit(False)
            sleep(1)

class Ui_Dialog(object):

    def __init__(self):
        self.connection = Connection()
        self.thread = QtCore.QThread()
        self.connection.connection_signal.connect(self.update_label)
        self.connection.moveToThread(self.thread)
        self.thread.started.connect(self.connection.check_connection)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(121, 31)
        self.label_internet = QtWidgets.QLabel(Dialog)
        self.label_internet.setGeometry(QtCore.QRect(0, 0, 121, 31))
        self.label_internet.setObjectName("label_internet")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.thread.start()

    def update_label(self, status: bool):
        if status:
            self.label_internet.setText("Connected")
            self.label_internet.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.label_internet.setText("Not Connected")
            self.label_internet.setStyleSheet("color: rgb(255, 0, 0);")
            
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Internet"))
        self.label_internet.setText(_translate("Dialog", "Internet"))

