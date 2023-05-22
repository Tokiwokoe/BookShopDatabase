import sys
import psycopg2

import generator
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from UIclass import main_window, LoginScreen


class AuthWindow(QMainWindow, LoginScreen.Ui_Auth):
    def __init__(self):
        super(AuthWindow, self).__init__()
        self.setupUi(self)
        self.login.clicked.connect(self.to_login)
        self.sign_up.clicked.connect(self.to_sign_up)

    def to_login(self):
        try:
            self.user = self.loginfield.text()
            self.password = self.passwordfield.text()
            self.connection = psycopg2.connect(
                host='localhost',
                database='Bookshop',
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            self.menu = MainMenu(self.connection, self.cursor)  # передаем connection и cursor
            self.menu.show()
            self.close()

        except Exception as err:
            print(err)
            self.error.setText('Проверьте ввод')

    def to_sign_up(self):
        ...


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
        query = 'SELECT * FROM "City_view"'
        self.labels = ['Город']
        self.to_print_table(query)

    def to_print_dist(self):
        query = 'SELECT * FROM "District_view"'
        self.labels = ['Район']
        self.to_print_table(query)

    def to_print_lang(self):
        query = 'SELECT * FROM "Language_view"'
        self.labels = ['Язык']
        self.to_print_table(query)

    def to_print_prop(self):
        query = 'SELECT * FROM "Property_type_view"'
        self.labels = ['Тип собственности']
        self.to_print_table(query)

    def to_print_country(self):
        query = 'SELECT * FROM "Country_view"'
        self.labels = ['Страна']
        self.to_print_table(query)

    def to_print_book(self):
        query = 'SELECT * FROM "Book_view"'
        self.labels = ['Название книги', 'Год выпуска', 'Язык', 'Издательство', 'Тип собственности']
        self.to_print_table(query)

    def to_print_author(self):
        query = 'SELECT * FROM "Author_view"'
        self.labels = ['ФИО', 'Страна', 'Дата рождения', 'Дата смерти']
        self.to_print_table(query)

    def to_print_book_in_shop(self):
        query = 'SELECT * FROM "Book_in_shop_view"'
        self.labels = ['Название книги', 'Номер магазина', 'Цена за экземпляр', 'Количество экземпляров', 'Дата поставки']
        self.to_print_table(query)

    def to_print_publish(self):
        query = 'SELECT * FROM "Publish_view"'
        self.labels = ['Город', 'Год открытия', 'Телефон']
        self.to_print_table(query)

    def to_print_shop(self):
        query = 'SELECT * FROM "Shop_view"'
        self.labels = ['Номер магазина', 'Район', 'Тип собственности', 'Год открытия']
        self.to_print_table(query)


class MainMenu(PrintTable, main_window.Ui_MainWindow):
    def __init__(self, connection, cursor):
        super(MainMenu, self).__init__()
        self.setupUi(self)
        self.setFixedSize(860, 640)
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
        self.Gen_button.clicked.connect(self.to_generate_all)
        self.connection = connection
        self.cursor = cursor

    def to_generate_all(self):
        """Генерация для таблиц"""
        try:
            for i in range(10):
                self.to_generate_dist()
                self.to_generate_language()
                self.to_generate_city()
                self.to_generate_prop()
                self.to_generate_country()
            self.to_generate_author()
            self.to_generate_publish()
            self.to_generate_book()
            self.to_generate_shop()
            #self.to_generate_book_in_shop()
        except Exception as err:
            print(err)


        """Генерация для JSON"""
        try:
            for i in range(10000):
                self.to_generate_json()
        except Exception as err:
            print(err)

    def to_generate(self, query):
        if query.startswith('S'):  # SELECT
            self.cursor.execute(query)
            return self.cursor.fetchone()
        elif query.startswith('I'):  # INSERT
            self.cursor.execute(query)
            self.connection.commit()
            print('Генерация завершена')

    def to_generate_dist(self):
        query = 'SELECT id FROM "District" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = generator.generate_dist(self.id)
        self.to_generate(query)

    def to_generate_city(self):
        query = 'SELECT id FROM "City" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = generator.generate_city(self.id)
        self.to_generate(query)

    def to_generate_country(self):
        query = 'SELECT id FROM "Country" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = generator.generate_country(self.id)
        self.to_generate(query)

    def to_generate_prop(self):
        query = 'SELECT id FROM "Property_type" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = generator.generate_prop(self.id)
        self.to_generate(query)

    def to_generate_language(self):
        query = 'SELECT id FROM "Language" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = generator.generate_language(self.id)
        self.to_generate(query)

    def to_generate_author(self):
        query = 'SELECT id FROM "Author" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = 'SELECT id FROM "Country" ORDER BY id DESC LIMIT 1'
        self.country = self.to_generate(query)
        query = generator.generate_author(self.id, self.country)
        self.to_generate(query)

    def to_generate_shop(self):
        query = 'SELECT id FROM "Shop" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = 'SELECT id FROM "District" ORDER BY id DESC LIMIT 1'
        self.dist = self.to_generate(query)
        query = 'SELECT id FROM "Property_type" ORDER BY id DESC LIMIT 1'
        self.prop = self.to_generate(query)
        query = generator.generate_shop(self.id, self.dist, self.prop)
        self.to_generate(query)

    def to_generate_book(self):
        query = 'SELECT id FROM "Book" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = 'SELECT id FROM "Language" ORDER BY id DESC LIMIT 1'
        self.lang = self.to_generate(query)
        query = 'SELECT id FROM "Author" ORDER BY id DESC LIMIT 1'
        self.author = self.to_generate(query)
        query = 'SELECT id FROM "Publish" ORDER BY id DESC LIMIT 1'
        self.publish = self.to_generate(query)
        query = generator.generate_book(self.id, self.lang, self.author, self.publish)
        self.to_generate(query)

    def to_generate_publish(self):
        query = 'SELECT id FROM "Publish" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = 'SELECT id FROM "City" ORDER BY id DESC LIMIT 1'
        self.city = self.to_generate(query)
        query = generator.generate_publish(self.id, self.city)
        self.to_generate(query)

    def to_generate_book_in_shop(self):
        query = 'SELECT id FROM "Book_in_shop" ORDER BY id DESC LIMIT 1'
        self.id = self.to_generate(query)
        query = 'SELECT id FROM "Book" ORDER BY id DESC LIMIT 1'
        self.book = self.to_generate(query)
        query = 'SELECT id FROM "Shop" ORDER BY id DESC LIMIT 1'
        self.shop = self.to_generate(query)
        query = generator.generate_book_in_shop(self.id, self.book, self.shop)
        self.to_generate(query)

    def to_generate_json(self):
        query = generator.generate_json()
        self.to_generate(query)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()

    window.show()
    sys.exit(app.exec_())
