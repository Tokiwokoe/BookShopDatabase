import sys
import connection
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from UIclass import main_window


class PrintTable(QMainWindow):
    def __init__(self):
        super(PrintTable, self).__init__()

    def to_print_table(self, query):
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(len(self.labels))
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        i = 0
        for elem in self.rows:
            j = 0
            for t in elem:
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        i = 0
        self.tableWidget.resizeColumnsToContents()

    def to_print_city(self):
        query = 'SELECT name FROM "City"' \
                'ORDER BY id'
        self.labels = ['Город']
        self.to_print_table(query)

    def to_print_dist(self):
        query = 'SELECT name FROM "District"' \
                'ORDER BY id'
        self.labels = ['Район']
        self.to_print_table(query)

    def to_print_lang(self):
        query = 'SELECT name FROM "Language"' \
                'ORDER BY id'
        self.labels = ['Язык']
        self.to_print_table(query)

    def to_print_prop(self):
        query = 'SELECT name FROM "Property_type"' \
                'ORDER BY id'
        self.labels = ['Тип собственности']
        self.to_print_table(query)

    def to_print_country(self):
        query = 'SELECT name FROM "Country"' \
                'ORDER BY id'
        self.labels = ['Страна']
        self.to_print_table(query)

    def to_print_book(self):
        query = 'SELECT "Book".name, year, "Language".name, "Author".name, "Publish".phone FROM "Book" ' \
                'LEFT JOIN "Language" ON "Language".id = "Book".language ' \
                'LEFT JOIN "Author" ON "Author".id = "Book".author ' \
                'LEFT JOIN "Publish" ON "Publish".id = "Book".publish ' \
                'ORDER BY "Book".id'
        self.labels = ['Название книги', 'Год выпуска', 'Язык', 'Издательство', 'Тип собственности']
        self.to_print_table(query)

    def to_print_author(self):
        query = 'SELECT "Author".name, "Country".name, birth_date, death_date FROM "Author" ' \
                'LEFT JOIN "Country" ON "Country".id = "Author".country ' \
                'ORDER BY "Author".id'
        self.labels = ['ФИО', 'Страна', 'Дата рождения', 'Дата смерти']
        self.to_print_table(query)

    def to_print_book_in_shop(self):
        query = 'SELECT "Book".name, "Shop".number, cost, amount, delivery_date FROM "Book_in_shop" ' \
                'LEFT JOIN "Book" ON "Book".id = "Book_in_shop".book_id ' \
                'LEFT JOIN "Shop" ON "Shop".id = "Book_in_shop".shop_id ' \
                'ORDER BY "Book_in_shop".shop_id'
        self.labels = ['Название книги', 'Номер магазина', 'Цена за экземпляр', 'Количество экземпляров', 'Дата поставки']
        self.to_print_table(query)

    def to_print_publish(self):
        query = 'SELECT "City".name, year_opened, phone FROM "Publish" ' \
                'LEFT JOIN "City" ON "City".id = "Publish".city ' \
                'ORDER BY "Publish".id'
        self.labels = ['Город', 'Год открытия', 'Телефон']
        self.to_print_table(query)

    def to_print_shop(self):
        query = 'SELECT number, "District".name, "Property_type".name, year_opened FROM "Shop" ' \
                'LEFT JOIN "District" ON "District".id = "Shop".district ' \
                'LEFT JOIN "Property_type" ON "Property_type".id = "Shop".property_type ' \
                'ORDER BY "Shop".id'
        self.labels = ['Номер магазина', 'Район', 'Тип собственности', 'Год открытия']
        self.to_print_table(query)


class MainMenu(PrintTable, main_window.Ui_MainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setupUi(self)
        self.setFixedSize(860, 725)
        self.cursor = connection.connection.cursor()
        self.Print_book.clicked.connect(self.to_print_book)
        self.Print_city.clicked.connect(self.to_print_city)
        self.Print_dist.clicked.connect(self.to_print_dist)
        self.Print_lang.clicked.connect(self.to_print_lang)
        self.Print_prop.clicked.connect(self.to_print_prop)
        self.Print_author.clicked.connect(self.to_print_author)
        self.Print_book_in_shop.clicked.connect(self.to_print_book_in_shop)
        self.Print_country.clicked.connect(self.to_print_country)
        self.Print_publish.clicked.connect(self.to_print_publish)
        self.Print_shop.clicked.connect(self.to_print_shop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainMenu()

    window.show()
    sys.exit(app.exec_())
