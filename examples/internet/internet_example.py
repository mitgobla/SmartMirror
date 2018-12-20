from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_internet_dialog
import sys

APP = QtWidgets.QApplication([])
DIALOG = QtWidgets.QDialog()
UI = Ui_internet_dialog.Ui_Dialog()
UI.setupUi(DIALOG)

# Check Ui_internet_dialog.py to see how the class is used.

DIALOG.show()

if __name__ == "__main__":
    sys.exit(APP.exec_())
