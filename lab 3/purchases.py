# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchases.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_PurchasesWindow(object):
    def setupUi(self, PurchasesWindow):
        theme_file=open("theme.json")
        theme=json.load(theme_file)
        PurchasesWindow.setObjectName("PurchasesWindow")
        PurchasesWindow.resize(829, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PurchasesWindow.sizePolicy().hasHeightForWidth())
        PurchasesWindow.setSizePolicy(sizePolicy)
        PurchasesWindow.setStyleSheet("background-color:"+theme["on_primary_color"]+"")
        self.centralwidget = QtWidgets.QWidget(PurchasesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, 80, 831, 491))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.tableWidget = QtWidgets.QTableWidget(self.stackedWidgetPage1)
        self.tableWidget.setGeometry(QtCore.QRect(40, 60, 771, 501))
        self.tableWidget.setStyleSheet("")
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
        self.textBrowser = QtWidgets.QTextBrowser(self.stackedWidgetPage1)
        self.textBrowser.setGeometry(QtCore.QRect(180, -40, 451, 91))
        self.textBrowser.setStyleSheet("border-style: hidden;\n"
"background-color:"+theme["primary_color"]+";\n"
"border-radius: 40px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color:"+theme["on_primary_color"]+"")
        self.textBrowser.setObjectName("textBrowser")
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.widget_5 = QtWidgets.QWidget(self.page)
        self.widget_5.setGeometry(QtCore.QRect(70, 60, 711, 411))
        self.widget_5.setStyleSheet("background-color:"+theme["secondary_variant_color"]+";\n"
"color:"+theme["on_primary_color"]+";\n"
"border-radius:10px;")
        self.widget_5.setObjectName("widget_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(340, 130, 211, 31))
        self.lineEdit_4.setStyleSheet("color:"+theme["on_primary_color"]+";\n"
"border-style:solid;\n"
"border-color:"+theme["on_primary_color"]+";\n"
"border-width:1px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(340, 180, 211, 31))
        self.lineEdit_5.setStyleSheet("border-style:solid;\n"
"border-color:"+theme["on_primary_color"]+";\n"
"border-width:1px;\n"
"color:"+theme["on_primary_color"]+";")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(340, 230, 211, 31))
        self.lineEdit_6.setStyleSheet("color:"+theme["on_primary_color"]+";\n"
"border-style:solid;\n"
"border-color:"+theme["on_primary_color"]+";\n"
"border-width:1px")
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
        self.textEdit_2.setStyleSheet("border-style:solid;\n"
"border-color:"+theme["on_primary_color"]+";\n"
"border-width:1px")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_19 = QtWidgets.QLabel(self.widget_5)
        self.label_19.setGeometry(QtCore.QRect(220, 20, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page)
        self.textBrowser_4.setGeometry(QtCore.QRect(190, -40, 451, 91))
        self.textBrowser_4.setStyleSheet("border-style: hidden;\n"
"background-color:"+theme["primary_color"]+";\n"
"border-radius: 40px;\n"
"border-style: outset;\n"
"padding: 5px;\n"
"color:"+theme["on_primary_color"]+"")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.stackedWidget.addWidget(self.page)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 570, 841, 81))
        self.widget_4.setStyleSheet("background-color:"+theme["primary_color"]+"")
        self.widget_4.setObjectName("widget_4")
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setGeometry(QtCore.QRect(20, 350, 811, 80))
        self.widget_2.setStyleSheet("opacity:0")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 831, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("background-color:"+theme["primary_color"]+"")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(660, -20, 181, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:"+theme["secondary_color"]+";\n"
"color:"+theme["on_primary_color"]+";\n"
"border: 2px solid #555;\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"padding: 5px;")
        self.pushButton_5.setObjectName("pushButton_5")
        PurchasesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PurchasesWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PurchasesWindow)

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
        item.setText(_translate("PurchasesWindow", "Color"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("PurchasesWindow", "Buyer id"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("PurchasesWindow", "Car price"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("PurchasesWindow", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("PurchasesWindow", "BMW"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("PurchasesWindow", "SUV"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("PurchasesWindow", "Green"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("PurchasesWindow", "2990317018184"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("PurchasesWindow", "30000$"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.textBrowser.setHtml(_translate("PurchasesWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Recent Purchases</span></p></body></html>"))
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
        self.pushButton_5.setText(_translate("PurchasesWindow", "Main Menu"))


