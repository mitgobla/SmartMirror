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
        super().__init__()

        if timeformat == "24":
            self.timeformat_cycle = cycle(["24", "12"])
        else:
            self.timeformat_cycle = cycle(["12", "24"])
        self.timeformat = next(self.timeformat_cycle)

    def toggle_format(self):
        """Toggles between 12hr/24hr format.
        """

        self.timeformat = next(self.timeformat_cycle)
        self.get_time()

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
            self.current_time.emit(current_clock.strftime("%H:%M %p"))
        return 60-current.second

    @QtCore.pyqtSlot()
    def update_time(self):
        while True:
            sleep(self.get_time())

class Date(QtCore.QObject):
    """12/24 hour Updating Clock

    Arguments:
        timeformat {str} -- "24" or "12"

    Returns:
        str -- %H:%M or %I:%M %p format of time
    """


    current_date = QtCore.pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def get_date(self):
        """Get the current date

        Returns:
            int -- Time left till next update
        """

        current = datetime.now()
        date_list = current.strftime("%A %d %B %Y").split(" ")
        if date_list[1][-1] == '1':
            date_list.append('st')
        elif date_list[1][-1] == '2':
            date_list.append('nd')
        elif date_list[1][-1] == '3':
            date_list.append('rd')
        else:
            date_list.append('th')
        self.current_date.emit(date_list)
        return ((24 - current.hour - 1) * 60 * 60) + ((60 - current.minute - 1) * 60) + (60 - current.second)

    @QtCore.pyqtSlot()
    def update_date(self):
        while True:
            sleep(self.get_date())
