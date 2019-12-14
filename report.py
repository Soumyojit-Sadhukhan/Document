# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")

db = client.get_database('test')
print(db)

collection = db.Invoice
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

class Ui_MainWindow_Report(object):
    def setupUi(self, MainWindow, prev):
        self.prev = prev
        self.cur = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.textEdit_purchase = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_purchase.setGeometry(QtCore.QRect(290, 100, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_purchase.setFont(font)
        self.textEdit_purchase.setObjectName(_fromUtf8("textEdit_purchase"))
        
        self.pushButton_search = QtGui.QPushButton(self.centralwidget)
        self.pushButton_search.setGeometry(QtCore.QRect(560, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName(_fromUtf8("pushButton_search"))
        self.pushButton_search.clicked.connect(self.btn_fun)
        
        self.pushButton_back = QtGui.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(600, 500, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName(_fromUtf8("pushButton_back"))
        self.pushButton_back.clicked.connect(self.fun_back)

        self.label_invoice = QtGui.QLabel(self.centralwidget)
        self.label_invoice.setGeometry(QtCore.QRect(160, 210, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoice.setFont(font)
        self.label_invoice.setObjectName(_fromUtf8("label_invoice"))
        
        self.label_purchaseOrder = QtGui.QLabel(self.centralwidget)
        self.label_purchaseOrder.setGeometry(QtCore.QRect(520, 210, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_purchaseOrder.setFont(font)
        self.label_purchaseOrder.setObjectName(_fromUtf8("label_purchaseOrder"))
        
        self.label_invoiceNum = QtGui.QLabel(self.centralwidget)
        self.label_invoiceNum.setGeometry(QtCore.QRect(70, 270, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoiceNum.setFont(font)
        self.label_invoiceNum.setObjectName(_fromUtf8("label_invoiceNum"))
        
        self.label_invoice_value = QtGui.QLabel(self.centralwidget)
        self.label_invoice_value.setGeometry(QtCore.QRect(210, 270, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoice_value.setFont(font)
        self.label_invoice_value.setText(_fromUtf8(""))
        self.label_invoice_value.setObjectName(_fromUtf8("label_invoice_value"))
        
        self.label_invoice_value_purchase = QtGui.QLabel(self.centralwidget)
        self.label_invoice_value_purchase.setGeometry(QtCore.QRect(210, 320, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoice_value_purchase.setFont(font)
        self.label_invoice_value_purchase.setText(_fromUtf8(""))
        self.label_invoice_value_purchase.setObjectName(_fromUtf8("label_invoice_value_purchase"))
        
        self.label_invoicePurchaseNum = QtGui.QLabel(self.centralwidget)
        self.label_invoicePurchaseNum.setGeometry(QtCore.QRect(60, 320, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoicePurchaseNum.setFont(font)
        self.label_invoicePurchaseNum.setObjectName(_fromUtf8("label_invoicePurchaseNum"))
        
        self.label_invoice_value_amount = QtGui.QLabel(self.centralwidget)
        self.label_invoice_value_amount.setGeometry(QtCore.QRect(210, 370, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoice_value_amount.setFont(font)
        self.label_invoice_value_amount.setText(_fromUtf8(""))
        self.label_invoice_value_amount.setObjectName(_fromUtf8("label_invoice_value_amount"))
        
        self.label_invoiceAmount = QtGui.QLabel(self.centralwidget)
        self.label_invoiceAmount.setGeometry(QtCore.QRect(130, 370, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoiceAmount.setFont(font)
        self.label_invoiceAmount.setObjectName(_fromUtf8("label_invoiceAmount"))
        
        self.label_invoice_value_img = QtGui.QLabel(self.centralwidget)
        self.label_invoice_value_img.setGeometry(QtCore.QRect(210, 420, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoice_value_img.setFont(font)
        self.label_invoice_value_img.setText(_fromUtf8(""))
        self.label_invoice_value_img.setObjectName(_fromUtf8("label_invoice_value_img"))
        
        self.label_invoice_img = QtGui.QLabel(self.centralwidget)
        self.label_invoice_img.setGeometry(QtCore.QRect(130, 420, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_invoice_img.setFont(font)
        self.label_invoice_img.setObjectName(_fromUtf8("label_invoice_img"))
        
        self.label_purchase_img = QtGui.QLabel(self.centralwidget)
        self.label_purchase_img.setGeometry(QtCore.QRect(500, 370, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_purchase_img.setFont(font)
        self.label_purchase_img.setObjectName(_fromUtf8("label_purchase_img"))
        
        self.label_purchase_value_img = QtGui.QLabel(self.centralwidget)
        self.label_purchase_value_img.setGeometry(QtCore.QRect(580, 370, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_purchase_value_img.setFont(font)
        self.label_purchase_value_img.setText(_fromUtf8(""))
        self.label_purchase_value_img.setObjectName(_fromUtf8("label_purchase_value_img"))
        
        self.label_value_purchase = QtGui.QLabel(self.centralwidget)
        self.label_value_purchase.setGeometry(QtCore.QRect(580, 270, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_value_purchase.setFont(font)
        self.label_value_purchase.setText(_fromUtf8(""))
        self.label_value_purchase.setObjectName(_fromUtf8("label_value_purchase"))
        
        self.label_purchase_value_amount = QtGui.QLabel(self.centralwidget)
        self.label_purchase_value_amount.setGeometry(QtCore.QRect(580, 320, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_purchase_value_amount.setFont(font)
        self.label_purchase_value_amount.setText(_fromUtf8(""))
        self.label_purchase_value_amount.setObjectName(_fromUtf8("label_purchase_value_amount"))
        
        self.label_purchaseAmount = QtGui.QLabel(self.centralwidget)
        self.label_purchaseAmount.setGeometry(QtCore.QRect(500, 320, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_purchaseAmount.setFont(font)
        self.label_purchaseAmount.setObjectName(_fromUtf8("label_purchaseAmount"))
        
        self.label_PurchaseNum = QtGui.QLabel(self.centralwidget)
        self.label_PurchaseNum.setGeometry(QtCore.QRect(430, 270, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_PurchaseNum.setFont(font)
        self.label_PurchaseNum.setObjectName(_fromUtf8("label_PurchaseNum"))
        
        self.label_msg = QtGui.QLabel(self.centralwidget)
        self.label_msg.setGeometry(QtCore.QRect(320, 500, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName(_fromUtf8("label_msg"))
        
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
        self.label.setText(_translate("MainWindow", "Purchase Order", None))
        self.pushButton_search.setText(_translate("MainWindow", "Search", None))
        self.pushButton_back.setText(_translate("MainWindow", "Back", None))

    def btn_fun(self):
        self.label_invoice.setText(_translate("MainWindow", "Invoice", None))
        self.label_purchaseOrder.setText(_translate("MainWindow", "Purchase Order", None))
        self.label_invoiceNum.setText(_translate("MainWindow", "Invoice Number", None))
        self.label_invoicePurchaseNum.setText(_translate("MainWindow", "Purchase Number", None))
        self.label_invoiceAmount.setText(_translate("MainWindow", "Amount", None))
        self.label_invoice_img.setText(_translate("MainWindow", "Images", None))
        self.label_purchase_img.setText(_translate("MainWindow", "Images", None))
        self.label_purchaseAmount.setText(_translate("MainWindow", "Amount", None))
        self.label_PurchaseNum.setText(_translate("MainWindow", "Purchase Number", None))
        invoice_cost = 0
        po_cost = 0
        # print(self.textEdit_purchase.toPlainText())
        results = collection.find({"number": self.textEdit_purchase.toPlainText()})
        #a=list(results)
        #print(a)
        for i in results:
            #print(i)
            #print(type(i))
            #print("printin i type " +i["type"])
            if i["type"].lower() == "invoice":
                
                self.label_invoice_value.setText(_translate("MainWindow", i["invoice_number"], None))
                self.label_invoice_value_purchase.setText(_translate("MainWindow", i["number"] , None))
                self.label_invoice_value_amount.setText(_translate("MainWindow", i["cost"], None))
                self.label_invoice_value_img.setText(_translate("MainWindow", i["_id"], None))   
                invoice_cost =  i["cost"] 
            if i["type"].lower() == "po":
                self.label_purchase_value_img.setText(_translate("MainWindow", i["_id"], None))
                self.label_purchase_value_amount.setText(_translate("MainWindow", i["cost"], None))
                self.label_value_purchase.setText(_translate("MainWindow",i["number"] , None))
                po_cost =  i["cost"] 
        if invoice_cost == po_cost:
            self.label_msg.setText(_translate("MainWindow", "Valid", None))
        else:
            self.label_msg.setText(_translate("MainWindow", "inValid", None))

    def fun_back(self):
        self.prev.show()
        self.cur.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow_Report()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

