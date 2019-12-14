from PyQt4 import QtCore, QtGui
from os import listdir
from os.path import isfile, join
from functools import partial
from classification2 import classifier
from report import Ui_MainWindow_Report
import pymongo
from pymongo import MongoClient
import cv2

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


collection = db.Invoice
class Ui_MainWindow_Win2(object):
    def setupUi(self, MainWindow,filePath,prev):
        self.prev = prev
        self.temp_window = MainWindow
        self.filePath=filePath
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        # self.label_photo = QtGui.QLabel(self.centralwidget)
        # # self.label_photo.setGeometry(QtCore.QRect(460, 20, 291, 391))
        # self.label_photo.setGeometry(QtCore.QRect(390, 20, 1000, 1333))
        # self.label_photo.setText(_fromUtf8(""))
        # self.label_photo.setObjectName(_fromUtf8("label_photo"))
        self.scrollArea_2 = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(430, 30, 800, 600))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 798, 598))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_photo = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_photo.setObjectName(_fromUtf8("label_photo"))
        self.gridLayout.addWidget(self.label_photo, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)


        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 250, 190))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 118, 189))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #mypath="F:\Tesseract\invoice_images"
       

        # print("printing files "+onlyfiles[1])

        
        # path = [join(self.filePath, f) for f in listdir(self.filePath) if isfile(join(self.filePath, f))]
        ob = classifier()
        self.d = ob.classifier_function(self.filePath)

        newpath = join(self.filePath, "imgs")
        self.filePath = newpath
        onlyfiles = [f for f in listdir(newpath) if isfile(join(newpath, f))]
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.buttons=[]
        num=len(onlyfiles)
        
        for i in range(num):
            self.buttons.append(QtGui.QPushButton(self.scrollAreaWidgetContents))
            self.gridLayout.addWidget(self.buttons[i], i, 0, 1, 1)
            self.buttons[i].setText(_translate("MainWindow", onlyfiles[i], None))
            #self.buttons[i].clicked.connect(partial(handleButton, data=str(self.buttons[i].objectName())))
            self.buttons[i].clicked.connect(partial(self.handleButton, data=onlyfiles[i]))
        
        self.label_type = QtGui.QLabel(self.centralwidget)
        self.label_type.setGeometry(QtCore.QRect(90, 230, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_type.setFont(font)
        self.label_type.setObjectName(_fromUtf8("label_type"))
        
        self.textEditType = QtGui.QTextEdit(self.centralwidget)
        self.textEditType.setGeometry(QtCore.QRect(170, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEditType.setFont(font)
        self.textEditType.setObjectName(_fromUtf8("textEditType"))
        
        self.label_InvoiceNumber = QtGui.QLabel(self.centralwidget)
        self.label_InvoiceNumber.setGeometry(QtCore.QRect(20, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_InvoiceNumber.setFont(font)
        self.label_InvoiceNumber.setObjectName(_fromUtf8("label_InvoiceNumber"))

        self.textEdit_InvoiceNumber = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_InvoiceNumber.setGeometry(QtCore.QRect(170, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_InvoiceNumber.setFont(font)
        self.textEdit_InvoiceNumber.setObjectName(_fromUtf8("textEdit_InvoiceNumber"))

        self.pushButtonUpdate = QtGui.QPushButton(self.centralwidget)
        # self.pushButtonUpdate.setGeometry(QtCore.QRect(620, 500, 75, 31))
        self.pushButtonUpdate.setGeometry(QtCore.QRect(100, 510, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonUpdate.setFont(font)
        self.pushButtonUpdate.setObjectName(_fromUtf8("pushButtonUpdate"))
        self.pushButtonUpdate.clicked.connect(self.fun_update)
        
        self.label_PurchaseNumber = QtGui.QLabel(self.centralwidget)
        self.label_PurchaseNumber.setGeometry(QtCore.QRect(15, 340, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_PurchaseNumber.setFont(font)
        self.label_PurchaseNumber.setObjectName(_fromUtf8("label_PurchaseNumber"))
        
        self.textEdit_PurchaseNumber = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_PurchaseNumber.setGeometry(QtCore.QRect(170, 330, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_PurchaseNumber.setFont(font)
        self.textEdit_PurchaseNumber.setObjectName(_fromUtf8("textEdit_PurchaseNumber"))
        
        self.pushButton_Next = QtGui.QPushButton(self.centralwidget)
        # self.pushButton_Next.setGeometry(QtCore.QRect(700, 500, 75, 31))
        self.pushButton_Next.setGeometry(QtCore.QRect(180, 510, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Next.setFont(font)
        self.pushButton_Next.setObjectName(_fromUtf8("pushButton_Next"))
        self.pushButton_Next.clicked.connect(self.fun_next)
        
        self.label_quantity = QtGui.QLabel(self.centralwidget)
        self.label_quantity.setGeometry(QtCore.QRect(70, 390, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_quantity.setFont(font)
        self.label_quantity.setObjectName(_fromUtf8("label_quantity"))
        
        self.label_amount = QtGui.QLabel(self.centralwidget)
        self.label_amount.setGeometry(QtCore.QRect(70, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_amount.setFont(font)
        self.label_amount.setObjectName(_fromUtf8("label_amount"))
        
        self.textEdit_quantity = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_quantity.setGeometry(QtCore.QRect(170, 390, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_quantity.setFont(font)
        self.textEdit_quantity.setObjectName(_fromUtf8("textEdit_quantity"))
        
        self.textEdit_amount = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_amount.setGeometry(QtCore.QRect(170, 450, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_amount.setFont(font)
        self.textEdit_amount.setObjectName(_fromUtf8("textEdit_amount"))

        self.pushButton_reset = QtGui.QPushButton(self.centralwidget)
        # self.pushButton_reset.setGeometry(QtCore.QRect(190, 510, 75, 31))
        self.pushButton_reset.setGeometry(QtCore.QRect(20, 510, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        self.pushButton_reset.clicked.connect(self.fun_reset)
        
        self.label_msg = QtGui.QLabel(self.centralwidget)
        self.label_msg.setGeometry(QtCore.QRect(60, 552, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName(_fromUtf8("label_msg"))

        self.pushButton_Back = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(270, 510, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setObjectName(_fromUtf8("pushButton_Back"))
        self.pushButton_Back.clicked.connect(self.fun_back)

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
        self.label_type.setText(_translate("MainWindow", "Type", None))
        self.label_InvoiceNumber.setText(_translate("MainWindow", "Invoice Number", None))
        self.pushButtonUpdate.setText(_translate("MainWindow", "Update", None))
        self.label_PurchaseNumber.setText(_translate("MainWindow", "Purchase Number", None))
        self.pushButton_Next.setText(_translate("MainWindow", "Next", None))
        self.label_quantity.setText(_translate("MainWindow", "Quantity", None))
        self.label_amount.setText(_translate("MainWindow", "Amount", None))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset", None))
        self.pushButton_Back.setText(_translate("MainWindow", "Back", None))

    def handleButton(self,data="\n"):
        self.fun_reset()
        f_path=join(self.filePath, data)
        self.index = data
        #print(data)
        # print("total file path "+f_path)
        self.label_photo.setPixmap(QtGui.QPixmap(f_path).scaled(1000,1333))
        temp = "Invoice"
        if self.d[data]['type'] == 'PO':
            temp = "Purchase Order"
        else:
            temp = "Invoice"
        self.textEditType.setText(temp)
        self.textEdit_PurchaseNumber.setText(self.d[data]['number'])
        self.textEdit_InvoiceNumber.setText(self.d[data]['invoice_number'])
        self.textEdit_amount.setText(self.d[data]['cost'])
    def fun_reset(self):
        self.textEditType.setText('')
        self.textEdit_InvoiceNumber.setText('')
        self.textEdit_PurchaseNumber.setText('')
        self.textEdit_quantity.setText('')
        self.textEdit_amount.setText('')

    def fun_update(self):
        self.label_msg.setText(_translate("MainWindow", "Updated . . .", None))
        cv2.waitKey(1000)
        self.label_msg.setText(_translate("MainWindow", "", None))
        type = self.textEditType.toPlainText()
        invoice = self.textEdit_InvoiceNumber.toPlainText()
        number = self.textEdit_PurchaseNumber.toPlainText()
        amount = self.textEdit_amount.toPlainText()
        self.d[self.index]["type"] = type
        self.d[self.index]["invoice"] = invoice
        self.d[self.index]["number"] = number
        self.d[self.index]["cost"] = amount
        collection.update({"_id": self.index},{"type": type, "invoice_number":invoice,"number": number, "cost": amount})
        # print(self.d)
        
    def fun_next(self):
        self.window=QtGui.QMainWindow()
        self.obj=Ui_MainWindow_Report()
        self.obj.setupUi(self.window, self.temp_window)
        self.window.show()
        self.temp_window.hide()
        
    def fun_back(self):
        self.prev.show()
        self.temp_window.close()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow_Win2()
    ui.setupUi(MainWindow,"")
    MainWindow.show()
    sys.exit(app.exec_())

