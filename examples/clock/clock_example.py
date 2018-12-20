from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_clock_dialog
import sys
APP = QtWidgets.QApplication([])
DIALOG = QtWidgets.QDialog()
UI = Ui_clock_dialog.Ui_Dialog()
UI.setupUi(DIALOG)

DIALOG.show()

if __name__ == "__main__":
    sys.exit(APP.exec_())
