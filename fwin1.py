from PyQt4 import QtCore, QtGui
from fwin2 import Ui_MainWindow_Win2
import pytesseract

#import cv2

import os
import re
from pdf2image import convert_from_path

import pymongo
from pymongo import MongoClient

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

client = MongoClient("mongodb://localhost:27017")

db = client.get_database('test')
print(db)

collection = db.Invoice


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 90, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        
        self.pushButton_browse = QtGui.QPushButton(self.centralwidget)
        self.pushButton_browse.setGeometry(QtCore.QRect(480, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_browse.setFont(font)
        self.pushButton_browse.setObjectName(_fromUtf8("pushButton_browse"))
        self.pushButton_browse.clicked.connect(self.browse_fun)
        
        self.pushButton_next = QtGui.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(310, 280, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName(_fromUtf8("pushButton_next"))
        self.pushButton_next.clicked.connect(self.next_fun)
        
        self.label_wt = QtGui.QLabel(self.centralwidget)
        self.label_wt.setGeometry(QtCore.QRect(250, 390, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_wt.setFont(font)
        self.label_wt.setObjectName(_fromUtf8("label_wt"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse", None))
        self.pushButton_next.setText(_translate("MainWindow", "Next", None))

    def browse_fun(self):
        #self.filepath=QtGui.QFileDialog.getOpenFileName(None,'Single File',"~/Desktop\Project\PyQt",'*')
        self.filepath = str(QtGui.QFileDialog.getExistingDirectory(None,'Single File',"~/Desktop\Project\PyQt",QtGui.QFileDialog.ShowDirsOnly))
        self.textBrowser.setText(_translate("MainWindow", str(self.filepath), None))

    def next_fun(self):
        self.label_wt.setText(_translate("MainWindow", "Processing . . .", None))
        self.window=QtGui.QMainWindow()
        self.obj=Ui_MainWindow_Win2()
        self.obj.setupUi(self.window,self.filepath, MainWindow)
        
        self.window.show()
        MainWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

