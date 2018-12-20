# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mitgobla\Documents\GitHub\SmartMirror\examples\clock\clock_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from itertools import cycle

class Clock(QtCore.QObject):
    """12/24 hour Updating Clock
    
    Arguments:
        timeformat {str} -- "24" or "12"

    Returns:
        str -- %H:%M or %I:%M %p format of time
    """


    current_time = QtCore.pyqtSignal(str)

    def __init__(self, timeformat="24"):
        super(QtCore.QObject, self).__init__()

        if timeformat == "24":
            self.timeformat_cycle = cycle(["24", "12"])
        else:
            self.timeformat_cycle = cycle(["12", "24"])
        self.timeformat = next(self.timeformat_cycle)

    def toggle_format(self):
        """Toggles between 12hr/24hr format.
        """

        self.timeformat = next(self.timeformat_cycle)

    def get_time(self):
        """Get the current time
        
        Returns:
            int -- Time left till next update
        """

        current = datetime.now()
        current_clock = datetime.strptime(str(current.hour)+":"+str(current.minute), "%H:%M")
        if self.timeformat == "12":
            self.current_time.emit(current_clock.strftime("%I:%M %p"))
        else:
            self.current_time.emit(current_clock.strftime("%H:%M"))
        return 60-current.second

    @QtCore.pyqtSlot()
    def update_time(self):
        while True:
            sleep(self.get_time())


class Ui_Dialog(object):

    def __init__(self):
        self.clock_update = Clock()
        self.thread = QtCore.QThread()
        self.clock_update.current_time.connect(self.update_label)
        self.clock_update.moveToThread(self.thread)
        self.thread.started.connect(self.clock_update.update_time)

    #@QtCore.pyqtSlot(str)
    def update_label(self, text: str):
        self.label_clock.setText(text)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(121, 31)
        self.label_clock = QtWidgets.QLabel(Dialog)
        self.label_clock.setGeometry(QtCore.QRect(0, 0, 121, 31))
        self.label_clock.setObjectName("label_clock")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.thread.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Clock"))
        self.label_clock.setText(_translate("Dialog", "Clock"))

