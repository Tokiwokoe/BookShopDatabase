# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(656, 150)
        Dialog.setStyleSheet("background-color: rgb(245, 245, 175)")
        self.OKbutton = QtWidgets.QPushButton(Dialog)
        self.OKbutton.setGeometry(QtCore.QRect(490, 100, 150, 41))
        self.OKbutton.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.OKbutton.setObjectName("OKbutton")
        self.id = QtWidgets.QLineEdit(Dialog)
        self.id.setGeometry(QtCore.QRect(290, 50, 351, 31))
        self.id.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.id.setText("")
        self.id.setObjectName("id")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(290, 20, 351, 20))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.table = QtWidgets.QComboBox(Dialog)
        self.table.setGeometry(QtCore.QRect(20, 50, 250, 30))
        self.table.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.table.setObjectName("table")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 250, 20))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.error = QtWidgets.QLabel(Dialog)
        self.error.setGeometry(QtCore.QRect(0, 110, 481, 21))
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
        self.OKbutton.setText(_translate("Dialog", "Добавить"))
        self.label_4.setText(_translate("Dialog", "Название"))
        self.label_5.setText(_translate("Dialog", "Выберите, куда добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
