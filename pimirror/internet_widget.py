import http.client as httplib
from PyQt5 import QtCore, QtGui
from time import sleep

class Connection(QtCore.QObject):
    """Connection Related Functions
    """

    connection_signal = QtCore.pyqtSignal(bool)

    @QtCore.pyqtSlot()
    def check_connection(self):
        """Check internet connection
        """

        conn = httplib.HTTPConnection("www.google.com", timeout=5)
        try:
            conn.request("HEAD", "/")
            conn.close()
            self.connection_signal.emit(True)
        except:
            conn.close()
            self.connection_signal.emit(False)
        sleep(5)

