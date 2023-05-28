# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 640)
        MainWindow.setStyleSheet("background-color: rgb(245, 245, 175)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Print_prop = QtWidgets.QPushButton(self.centralwidget)
        self.Print_prop.setGeometry(QtCore.QRect(250, 530, 151, 23))
        self.Print_prop.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_prop.setObjectName("Print_prop")
        self.Print_shop = QtWidgets.QPushButton(self.centralwidget)
        self.Print_shop.setGeometry(QtCore.QRect(50, 440, 151, 23))
        self.Print_shop.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_shop.setObjectName("Print_shop")
        self.Print_city = QtWidgets.QPushButton(self.centralwidget)
        self.Print_city.setGeometry(QtCore.QRect(250, 470, 151, 23))
        self.Print_city.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_city.setObjectName("Print_city")
        self.Print_country = QtWidgets.QPushButton(self.centralwidget)
        self.Print_country.setGeometry(QtCore.QRect(250, 500, 151, 23))
        self.Print_country.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_country.setObjectName("Print_country")
        self.Print_book = QtWidgets.QPushButton(self.centralwidget)
        self.Print_book.setGeometry(QtCore.QRect(50, 470, 151, 23))
        self.Print_book.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_book.setObjectName("Print_book")
        self.Print_author = QtWidgets.QPushButton(self.centralwidget)
        self.Print_author.setGeometry(QtCore.QRect(50, 560, 151, 23))
        self.Print_author.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_author.setObjectName("Print_author")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 861, 371))
        self.tableWidget.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Print_dist = QtWidgets.QPushButton(self.centralwidget)
        self.Print_dist.setGeometry(QtCore.QRect(250, 440, 151, 23))
        self.Print_dist.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_dist.setObjectName("Print_dist")
        self.Print_lang = QtWidgets.QPushButton(self.centralwidget)
        self.Print_lang.setGeometry(QtCore.QRect(250, 560, 151, 23))
        self.Print_lang.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_lang.setObjectName("Print_lang")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 379, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 32px;\n"
"font: \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Print_publish = QtWidgets.QPushButton(self.centralwidget)
        self.Print_publish.setGeometry(QtCore.QRect(50, 530, 151, 23))
        self.Print_publish.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_publish.setObjectName("Print_publish")
        self.Change_button = QtWidgets.QPushButton(self.centralwidget)
        self.Change_button.setGeometry(QtCore.QRect(470, 440, 171, 40))
        self.Change_button.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Change_button.setObjectName("Change_button")
        self.Print_book_in_shop = QtWidgets.QPushButton(self.centralwidget)
        self.Print_book_in_shop.setGeometry(QtCore.QRect(50, 500, 151, 23))
        self.Print_book_in_shop.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Print_book_in_shop.setObjectName("Print_book_in_shop")
        self.Workers_button = QtWidgets.QPushButton(self.centralwidget)
        self.Workers_button.setGeometry(QtCore.QRect(470, 490, 351, 40))
        self.Workers_button.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Workers_button.setObjectName("Workers_button")
        self.Queries_button = QtWidgets.QPushButton(self.centralwidget)
        self.Queries_button.setGeometry(QtCore.QRect(470, 540, 351, 40))
        self.Queries_button.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Queries_button.setObjectName("Queries_button")
        self.Delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_button.setGeometry(QtCore.QRect(660, 440, 161, 40))
        self.Delete_button.setStyleSheet("font-size: 16px;\n"
"font: \"Yu Gothic UI Semibold\";\n"
"background-color: rgb(245, 245, 245)")
        self.Delete_button.setObjectName("Delete_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Print_prop.setText(_translate("MainWindow", "Тип собственности"))
        self.Print_shop.setText(_translate("MainWindow", "Магазины"))
        self.Print_city.setText(_translate("MainWindow", "Город"))
        self.Print_country.setText(_translate("MainWindow", "Страна"))
        self.Print_book.setText(_translate("MainWindow", "Книги"))
        self.Print_author.setText(_translate("MainWindow", "Авторы"))
        self.Print_dist.setText(_translate("MainWindow", "Районы"))
        self.Print_lang.setText(_translate("MainWindow", "Язык"))
        self.label.setText(_translate("MainWindow", "Просмотр таблиц"))
        self.Print_publish.setText(_translate("MainWindow", "Издательства"))
        self.Change_button.setText(_translate("MainWindow", "Добавить изменения"))
        self.Print_book_in_shop.setText(_translate("MainWindow", "Книги в магазинах"))
        self.Workers_button.setText(_translate("MainWindow", "Редактировать пользователей"))
        self.Queries_button.setText(_translate("MainWindow", "Перейти в режим запросов"))
        self.Delete_button.setText(_translate("MainWindow", "Удаление из таблицы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
