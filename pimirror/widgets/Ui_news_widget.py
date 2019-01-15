# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\mitgobla\Documents\GitHub\SmartMirror\pimirror\widgets\news_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_news_widget(object):
    def setupUi(self, news_widget):
        news_widget.setObjectName("news_widget")
        news_widget.resize(320, 600)
        news_widget.setMinimumSize(QtCore.QSize(320, 600))
        news_widget.setMaximumSize(QtCore.QSize(320, 600))
        news_widget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_articletitle_1 = QtWidgets.QLabel(news_widget)
        self.label_articletitle_1.setGeometry(QtCore.QRect(0, 0, 320, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_articletitle_1.setFont(font)
        self.label_articletitle_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_articletitle_1.setWordWrap(True)
        self.label_articletitle_1.setObjectName("label_articletitle_1")
        self.label_articlebody_1 = QtWidgets.QLabel(news_widget)
        self.label_articlebody_1.setGeometry(QtCore.QRect(0, 50, 320, 121))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_articlebody_1.setFont(font)
        self.label_articlebody_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_articlebody_1.setWordWrap(True)
        self.label_articlebody_1.setObjectName("label_articlebody_1")
        self.line = QtWidgets.QFrame(news_widget)
        self.line.setGeometry(QtCore.QRect(9, 180, 301, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_articlebody_2 = QtWidgets.QLabel(news_widget)
        self.label_articlebody_2.setGeometry(QtCore.QRect(0, 250, 320, 121))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_articlebody_2.setFont(font)
        self.label_articlebody_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_articlebody_2.setWordWrap(True)
        self.label_articlebody_2.setObjectName("label_articlebody_2")
        self.line_2 = QtWidgets.QFrame(news_widget)
        self.line_2.setGeometry(QtCore.QRect(9, 380, 301, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_articletitle_2 = QtWidgets.QLabel(news_widget)
        self.label_articletitle_2.setGeometry(QtCore.QRect(0, 200, 320, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_articletitle_2.setFont(font)
        self.label_articletitle_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_articletitle_2.setWordWrap(True)
        self.label_articletitle_2.setObjectName("label_articletitle_2")
        self.line_3 = QtWidgets.QFrame(news_widget)
        self.line_3.setGeometry(QtCore.QRect(9, 580, 301, 20))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.label_articletitle_3 = QtWidgets.QLabel(news_widget)
        self.label_articletitle_3.setGeometry(QtCore.QRect(0, 400, 320, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_articletitle_3.setFont(font)
        self.label_articletitle_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_articletitle_3.setWordWrap(True)
        self.label_articletitle_3.setObjectName("label_articletitle_3")
        self.label_articlebody_3 = QtWidgets.QLabel(news_widget)
        self.label_articlebody_3.setGeometry(QtCore.QRect(0, 450, 320, 121))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_articlebody_3.setFont(font)
        self.label_articlebody_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_articlebody_3.setWordWrap(True)
        self.label_articlebody_3.setObjectName("label_articlebody_3")

        self.retranslateUi(news_widget)
        QtCore.QMetaObject.connectSlotsByName(news_widget)

    def retranslateUi(self, news_widget):
        _translate = QtCore.QCoreApplication.translate
        self.label_articletitle_1.setText(_translate("news_widget", "<html><head/><body><p><span style=\" font-size:14pt;\">Article 1 Name ABCDEFGHIJKLMNOP1234567890</span></p></body></html>"))
        self.label_articlebody_1.setText(_translate("news_widget", "<html><head/><body><p><span style=\" font-size:10pt;\">Article 1 Text: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et rhoncus diam. Etiam ipsum nibh, mollis ac aliquam sed, euismod non ligula. In nulla justo, finibus vel arcu vitae, condimentum posuere erat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Curabitur a porta leo.</span></p></body></html>"))
        self.label_articlebody_2.setText(_translate("news_widget", "<html><head/><body><p><span style=\" font-size:10pt;\">Article 2 Text: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et rhoncus diam. Etiam ipsum nibh, mollis ac aliquam sed, euismod non ligula. In nulla justo, finibus vel arcu vitae, condimentum posuere erat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Curabitur a porta leo.</span></p></body></html>"))
        self.label_articletitle_2.setText(_translate("news_widget", "<html><head/><body><p><span style=\" font-size:14pt;\">Article 2 Name ABCDEFGHIJKLMNOP1234567890</span></p></body></html>"))
        self.label_articletitle_3.setText(_translate("news_widget", "<html><head/><body><p><span style=\" font-size:14pt;\">Article 3 Name ABCDEFGHIJKLMNOP1234567890</span></p></body></html>"))
        self.label_articlebody_3.setText(_translate("news_widget", "<html><head/><body><p><span style=\" font-size:10pt;\">Article 3 Text: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et rhoncus diam. Etiam ipsum nibh, mollis ac aliquam sed, euismod non ligula. In nulla justo, finibus vel arcu vitae, condimentum posuere erat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Curabitur a porta leo.</span></p></body></html>"))

