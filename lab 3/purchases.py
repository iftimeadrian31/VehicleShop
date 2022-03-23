# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchases.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import json
import os
from playsound import playsound

class Ui_PurchasesWindow(object):

    def display(self,i):
        playsound('sounds\\03 Primary System Sounds\\ui_tap-variant-03.wav')
        self.stackedWidget.setCurrentIndex(i)

    def openMainMenu(self):
        playsound('sounds\\03 Primary System Sounds\\ui_tap-variant-03.wav')
        self.mainMenuCallback()
        
    def loadTable(self):
        path="purchases.json"
        theme_file=open(path,"r")
        if os.stat(path).st_size == 0:
            self.theme=[]
        else:
            self.theme=json.load(theme_file)
        theme_file.close()
        self.tableWidget.setRowCount(0);
        for i in range(len(self.theme)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i,0,QTableWidgetItem(str(i+1)))
            self.tableWidget.setItem(i,1,QTableWidgetItem(self.theme[i]["company"]))
            self.tableWidget.setItem(i,2,QTableWidgetItem(self.theme[i]["type"]))
            self.tableWidget.setItem(i,3,QTableWidgetItem(self.theme[i]["time"]))
            self.tableWidget.setItem(i,4,QTableWidgetItem(str(i+1)))
            self.tableWidget.setItem(i,5,QTableWidgetItem(str((i+1)*12345)))
            
    def selectData(self):
        playsound('sounds\\03 Primary System Sounds\\ui_tap-variant-03.wav')
        self.display(1)
        info=self.theme[self.tableWidget.currentRow()]["personal_information"]
        firstname=info["firstname"]
        lastname=info["lastname"]
        personalId=info["personalId"]
        adress=info["adress"]
        self.lineEdit_4.setText(firstname)
        self.lineEdit_5.setText(lastname)
        self.lineEdit_6.setText(personalId)
        self.textEdit_2.setText(adress)

    def setupUi(self, PurchasesWindow,mainMenuCallback):
        
        self.mainMenuCallback=mainMenuCallback
        theme_file=open("theme.json")
        theme=json.load(theme_file)
        PurchasesWindow.setObjectName("PurchasesWindow")
        PurchasesWindow.resize(829, 650)
        self.myWindow=PurchasesWindow
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PurchasesWindow.sizePolicy().hasHeightForWidth())
        PurchasesWindow.setSizePolicy(sizePolicy)
        PurchasesWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(PurchasesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 0, 841, 651))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.tableWidget = QtWidgets.QTableWidget(self.page_0)
        self.tableWidget.setGeometry(QtCore.QRect(40, 220, 771, 341))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(227, 131, 246))
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(227, 131, 246))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(227, 131, 246))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(227, 131, 246))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(227, 131, 246))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(227, 131, 246))
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(227, 131, 246))
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        self.textBrowser = QtWidgets.QTextBrowser(self.page_0)
        self.textBrowser.setGeometry(QtCore.QRect(210, 40, 451, 91))
        self.textBrowser.setStyleSheet("border-style: hidden;\n"
"background-color:rgb(137, 83, 243);\n"
"border-radius: 40px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color:rgb(255, 255, 255)")
        self.textBrowser.setObjectName("textBrowser")
        self.widget_4 = QtWidgets.QWidget(self.page_0)
        self.widget_4.setGeometry(QtCore.QRect(10, 570, 841, 81))
        self.widget_4.setStyleSheet("background-color:rgb(137, 83, 243)")
        self.widget_4.setObjectName("widget_4")
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.pushButton_23 = QtWidgets.QPushButton(self.widget_4,clicked = lambda:self.selectData())
        self.pushButton_23.setGeometry(QtCore.QRect(230, 20, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("QPushButton{background-color:rgb(177, 15, 210);\n"
"color:rgb(255, 255, 255);\n"
"border: 2px solid #555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"padding: 5px;}\n"
"QPushButton:hover {\n"
"    background-color: rgb(227, 131, 246);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(96, 9, 114);\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.widget_2.setGeometry(QtCore.QRect(20, 350, 811, 80))
        self.widget_2.setStyleSheet("opacity:0")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.page_0)
        self.widget_3.setGeometry(QtCore.QRect(10, 0, 831, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color:rgb(137, 83, 243)")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(660, -20, 181, 111))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3,clicked = lambda:self.openMainMenu())
        self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{background-color:rgb(177, 15, 210);\n"
"color:rgb(255, 255, 255);\n"
"border: 2px solid #555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"padding: 5px;}\n"
"QPushButton:hover {\n"
"    background-color: rgb(227, 131, 246);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(96, 9, 114);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page")
        self.widget_5 = QtWidgets.QWidget(self.page_1)
        self.widget_5.setGeometry(QtCore.QRect(70, 150, 711, 411))
        self.widget_5.setStyleSheet("background-color:rgb(227, 131, 246);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.widget_5.setObjectName("widget_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 130, 211, 31))
        self.lineEdit_4.setStyleSheet("QLineEdit{color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-color:rgb(0, 0, 0);\n"
"border-width:1px\n"
"}\n"
"QLineEdit:focus{color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width:1px\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 180, 211, 31))
        self.lineEdit_5.setStyleSheet("QLineEdit{color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-color:rgb(0, 0, 0);\n"
"border-width:1px\n"
"}\n"
"QLineEdit:focus{color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width:1px\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(340, 230, 211, 31))
        self.lineEdit_6.setStyleSheet("QLineEdit{color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-color:rgb(0, 0, 0);\n"
"border-width:1px\n"
"}\n"
"QLineEdit:focus{color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width:1px\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        self.label_3.setGeometry(QtCore.QRect(200, 130, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setGeometry(QtCore.QRect(200, 180, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_17 = QtWidgets.QLabel(self.widget_5)
        self.label_17.setGeometry(QtCore.QRect(200, 230, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget_5)
        self.label_18.setGeometry(QtCore.QRect(200, 300, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_5)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 280, 211, 101))
        self.textEdit_2.setStyleSheet("QTextEdit{color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-color:rgb(0, 0, 0);\n"
"border-width:1px\n"
"}\n"
"QTextEdit:focus{color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width:1px\n"
"}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_19 = QtWidgets.QLabel(self.widget_5)
        self.label_19.setGeometry(QtCore.QRect(220, 20, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_1)
        self.textBrowser_4.setGeometry(QtCore.QRect(210, 40, 451, 91))
        self.textBrowser_4.setStyleSheet("border-style: hidden;\n"
"background-color:rgb(137, 83, 243);\n"
"border-radius: 40px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color:rgb(255, 255, 255)")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.widget_6 = QtWidgets.QWidget(self.page_1)
        self.widget_6.setGeometry(QtCore.QRect(830, 580, 841, 81))
        self.widget_6.setStyleSheet("background-color:rgb(137, 83, 243)")
        self.widget_6.setObjectName("widget_6")
        self.widget_8 = QtWidgets.QWidget(self.widget_6)
        self.widget_8.setGeometry(QtCore.QRect(20, 350, 811, 80))
        self.widget_8.setStyleSheet("opacity:0")
        self.widget_8.setObjectName("widget_8")
        self.widget_10 = QtWidgets.QWidget(self.page_1)
        self.widget_10.setGeometry(QtCore.QRect(10, 0, 831, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy)
        self.widget_10.setStyleSheet("background-color:rgb(137, 83, 243)")
        self.widget_10.setObjectName("widget_10")
        self.label_6 = QtWidgets.QLabel(self.widget_10)
        self.label_6.setGeometry(QtCore.QRect(660, -20, 181, 111))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("logo2.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_10,clicked = lambda:self.display(0))
        self.pushButton_8.setGeometry(QtCore.QRect(10, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{background-color:rgb(177, 15, 210);\n"
"color:rgb(255, 255, 255);\n"
"border: 2px solid #555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"padding: 5px;}\n"
"QPushButton:hover {\n"
"    background-color: rgb(227, 131, 246);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(96, 9, 114);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_10,clicked = lambda:self.openMainMenu())
        self.pushButton_9.setGeometry(QtCore.QRect(170, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{background-color:rgb(177, 15, 210);\n"
"color:rgb(255, 255, 255);\n"
"border: 2px solid #555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"padding: 5px;}\n"
"QPushButton:hover {\n"
"    background-color: rgb(227, 131, 246);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(96, 9, 114);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget_11 = QtWidgets.QWidget(self.page_1)
        self.widget_11.setGeometry(QtCore.QRect(10, 570, 841, 81))
        self.widget_11.setStyleSheet("background-color:rgb(137, 83, 243)")
        self.widget_11.setObjectName("widget_11")
        self.widget_12 = QtWidgets.QWidget(self.widget_11)
        self.widget_12.setGeometry(QtCore.QRect(20, 350, 811, 80))
        self.widget_12.setStyleSheet("opacity:0")
        self.widget_12.setObjectName("widget_12")
        self.stackedWidget.addWidget(self.page_1)
        PurchasesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PurchasesWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PurchasesWindow)
        self.loadTable()

    def retranslateUi(self, PurchasesWindow):
        _translate = QtCore.QCoreApplication.translate
        PurchasesWindow.setWindowTitle(_translate("PurchasesWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PurchasesWindow", "Car id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PurchasesWindow", "Company"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("PurchasesWindow", "Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("PurchasesWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PurchasesWindow", "Buyer id"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("PurchasesWindow", "Car price"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.textBrowser.setHtml(_translate("PurchasesWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Recent Purchases</span></p></body></html>"))
        self.pushButton_5.setText(_translate("PurchasesWindow", "Main Menu"))
        self.label_3.setText(_translate("PurchasesWindow", "Firstname"))
        self.label_9.setText(_translate("PurchasesWindow", "Lastname"))
        self.label_17.setText(_translate("PurchasesWindow", "Personal ID"))
        self.label_18.setText(_translate("PurchasesWindow", "Adress"))
        self.label_19.setText(_translate("PurchasesWindow", "Personal information"))
        self.textBrowser_4.setHtml(_translate("PurchasesWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">ID:</span></p></body></html>"))
        self.pushButton_8.setText(_translate("PurchasesWindow", "Back"))
        self.pushButton_9.setText(_translate("PurchasesWindow", "Main Menu"))
        self.pushButton_23.setText(_translate("PurchaseWindow", "Show Buyer info"))
        
