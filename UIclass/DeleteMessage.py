# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteMessage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(560, 150)
        Dialog.setStyleSheet("background-color: rgb(245, 245, 175)")
        self.OKbutton = QtWidgets.QPushButton(Dialog)
        self.OKbutton.setGeometry(QtCore.QRect(220, 100, 161, 41))
        self.OKbutton.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.OKbutton.setObjectName("OKbutton")
        self.text = QtWidgets.QTextBrowser(Dialog)
        self.text.setGeometry(QtCore.QRect(10, 11, 541, 81))
        self.text.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.text.setObjectName("text")
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(390, 100, 161, 41))
        self.CancelButton.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.CancelButton.setObjectName("CancelButton")
        self.error = QtWidgets.QLabel(Dialog)
        self.error.setGeometry(QtCore.QRect(10, 110, 201, 21))
        self.error.setStyleSheet("color: red;\n"
"font-size: 16px;\n"
"font: 16pt \"Franklin Gothic Demi\";")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OKbutton.setText(_translate("Dialog", "Да"))
        self.text.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CancelButton.setText(_translate("Dialog", "Нет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
