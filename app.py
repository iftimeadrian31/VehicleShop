from PyQt5 import QtCore, QtGui, QtWidgets
from shop import Ui_ShopWindow

class Ui_StartingWindow(object):
    def openShop(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_ShopWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.myWindow.hide()

    def setupUi(self, StartingWindow):
        StartingWindow.setObjectName("StartingWindow")
        StartingWindow.resize(829, 661)
        self.myWindow=StartingWindow
        self.centralwidget = QtWidgets.QWidget(StartingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, 5, 821, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background1.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(73, 26, 701, 111))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.openShop())
        self.pushButton.setGeometry(QtCore.QRect(250, 510, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        StartingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 26))
        self.menubar.setObjectName("menubar")
        self.menuLanguage = QtWidgets.QMenu(self.menubar)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuLanguages = QtWidgets.QMenu(self.menuLanguage)
        self.menuLanguages.setObjectName("menuLanguages")
        self.menuShop = QtWidgets.QMenu(self.menubar)
        self.menuShop.setObjectName("menuShop")
        self.menuPurchases = QtWidgets.QMenu(self.menubar)
        self.menuPurchases.setObjectName("menuPurchases")
        StartingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartingWindow)
        self.statusbar.setObjectName("statusbar")
        StartingWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(StartingWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionEnglish = QtWidgets.QAction(StartingWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionFrench = QtWidgets.QAction(StartingWindow)
        self.actionFrench.setObjectName("actionFrench")
        self.actionGerman = QtWidgets.QAction(StartingWindow)
        self.actionGerman.setObjectName("actionGerman")
        self.menuLanguages.addAction(self.actionEnglish)
        self.menuLanguages.addAction(self.actionFrench)
        self.menuLanguages.addAction(self.actionGerman)
        self.menuLanguage.addAction(self.menuLanguages.menuAction())
        self.menuLanguage.addAction(self.actionHelp)
        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menuShop.menuAction())
        self.menubar.addAction(self.menuPurchases.menuAction())

        self.retranslateUi(StartingWindow)
        QtCore.QMetaObject.connectSlotsByName(StartingWindow)

    def retranslateUi(self, StartingWindow):
        _translate = QtCore.QCoreApplication.translate
        StartingWindow.setWindowTitle(_translate("StartingWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("StartingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Welcome to the starting page of the car dealership</span></p></body></html>"))
        self.pushButton.setText(_translate("StartingWindow", "Begin transaction"))
        self.menuLanguage.setTitle(_translate("StartingWindow", "Menu"))
        self.menuLanguages.setTitle(_translate("StartingWindow", "Languages"))
        self.menuShop.setTitle(_translate("StartingWindow", "Shop"))
        self.menuPurchases.setTitle(_translate("StartingWindow", "Purchases"))
        self.actionHelp.setText(_translate("StartingWindow", "Help"))
        self.actionEnglish.setText(_translate("StartingWindow", "English"))
        self.actionFrench.setText(_translate("StartingWindow", "French"))
        self.actionGerman.setText(_translate("StartingWindow", "German"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartingWindow = QtWidgets.QMainWindow()
    ui = Ui_StartingWindow()
    ui.setupUi(StartingWindow)
    StartingWindow.show()
    sys.exit(app.exec_())
