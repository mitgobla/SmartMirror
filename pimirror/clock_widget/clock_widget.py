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
            self.current_time.emit(current_clock.strftime("%H:%M"))
        return 60-current.second

    @QtCore.pyqtSlot()
    def update_time(self):
        while True:
            sleep(self.get_time())

