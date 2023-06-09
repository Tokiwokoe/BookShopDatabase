# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queries.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1096, 418)
        Dialog.setStyleSheet("background-color: rgb(245, 245, 175)")
        self.queries = QtWidgets.QComboBox(Dialog)
        self.queries.setGeometry(QtCore.QRect(10, 10, 701, 21))
        self.queries.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.queries.setObjectName("queries")
        self.print = QtWidgets.QPushButton(Dialog)
        self.print.setGeometry(QtCore.QRect(940, 370, 151, 41))
        self.print.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.print.setObjectName("print")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 701, 371))
        self.tableWidget.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_combo = QtWidgets.QLabel(Dialog)
        self.label_combo.setGeometry(QtCore.QRect(720, 10, 371, 20))
        self.label_combo.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_combo.setText("")
        self.label_combo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_combo.setObjectName("label_combo")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(720, 40, 371, 21))
        self.comboBox.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(720, 100, 371, 21))
        self.textEdit.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.textEdit.setText("")
        self.textEdit.setObjectName("textEdit")
        self.label_text = QtWidgets.QLabel(Dialog)
        self.label_text.setGeometry(QtCore.QRect(720, 70, 371, 20))
        self.label_text.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_text.setText("")
        self.label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text.setObjectName("label_text")
        self.textEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(720, 160, 371, 21))
        self.textEdit_2.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.textEdit_2.setText("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_text_2 = QtWidgets.QLabel(Dialog)
        self.label_text_2.setGeometry(QtCore.QRect(720, 130, 371, 20))
        self.label_text_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_text_2.setText("")
        self.label_text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_2.setObjectName("label_text_2")
        self.error = QtWidgets.QLabel(Dialog)
        self.error.setGeometry(QtCore.QRect(720, 380, 211, 21))
        self.error.setStyleSheet("color: red;\n"
"font-size: 16px;\n"
"font: 16pt \"Franklin Gothic Demi\";")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.textEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(720, 220, 371, 21))
        self.textEdit_3.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.textEdit_3.setText("")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_text_3 = QtWidgets.QLabel(Dialog)
        self.label_text_3.setGeometry(QtCore.QRect(720, 190, 371, 20))
        self.label_text_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"font: \"Arial Black\";")
        self.label_text_3.setText("")
        self.label_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_3.setObjectName("label_text_3")
        self.excel_btn = QtWidgets.QPushButton(Dialog)
        self.excel_btn.setGeometry(QtCore.QRect(940, 270, 151, 41))
        self.excel_btn.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.excel_btn.setObjectName("excel_btn")
        self.graph_btn = QtWidgets.QPushButton(Dialog)
        self.graph_btn.setGeometry(QtCore.QRect(940, 320, 151, 41))
        self.graph_btn.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.graph_btn.setObjectName("graph_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.print.setText(_translate("Dialog", "Обновить"))
        self.excel_btn.setText(_translate("Dialog", "Экспорт в Excel"))
        self.graph_btn.setText(_translate("Dialog", "Гистограмма"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
