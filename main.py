import sys
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from AddClasses import AddBook, AddAuthor, AddBookInShop, AddPm, AddSm
from UIclass import main_window, LoginScreen, publish_manager, shop_manager, admin, delete, DeleteMessage, queries


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
            self.cursor.execute("SELECT current_user;")
            self.current_user = self.cursor.fetchone()[0]
            self.cursor.execute("SELECT rolname FROM pg_user JOIN pg_auth_members ON pg_user.usesysid = pg_auth_members.member JOIN pg_roles ON pg_roles.oid = pg_auth_members.roleid WHERE pg_user.usename = current_user;")
            self.role_group = self.cursor.fetchone()[0]
            print(f'{self.current_user} из группы {self.role_group} вошёл в систему')
            if self.role_group == 'admins':
                self.admin_menu = MainMenu(self.connection, self.cursor, self.current_user, self.role_group)
                self.admin_menu.show()
            elif self.role_group == 'publish_manager':
                self.cursor.execute(f"SELECT departament FROM \"Publish_manager\" WHERE login = '{self.user}'")
                self.departament = self.cursor.fetchone()[0]
                self.publish_menu = PublishMenu(self.connection, self.cursor, self.current_user, self.departament, self.role_group)
                self.publish_menu.show()
            elif self.role_group == 'shop_manager':
                self.cursor.execute(f"SELECT departament FROM \"Shop_manager\" WHERE login = '{self.user}'")
                self.departament = self.cursor.fetchone()[0]
                self.shop_menu = ShopMenu(self.connection, self.cursor, self.current_user, self.departament, self.role_group)
                self.shop_menu.show()
            else:
                self.error.setText('Неизвестная роль')
            self.close()

        except psycopg2.Error as err:
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
        self.labels = ['id', 'Город']
        self.to_print_table(query)

    def to_print_dist(self):
        query = 'SELECT * FROM "District_view"'
        self.labels = ['id', 'Район']
        self.to_print_table(query)

    def to_print_lang(self):
        query = 'SELECT * FROM "Language_view"'
        self.labels = ['id', 'Язык']
        self.to_print_table(query)

    def to_print_prop(self):
        query = 'SELECT * FROM "Property_type_view"'
        self.labels = ['id', 'Тип собственности']
        self.to_print_table(query)

    def to_print_country(self):
        query = 'SELECT * FROM "Country_view"'
        self.labels = ['id', 'Страна']
        self.to_print_table(query)

    def to_print_book(self):
        query = 'SELECT * FROM "Book_view"'
        self.labels = ['id', 'Название книги', 'Год выпуска', 'Язык', 'Издательство', 'Тип собственности']
        self.to_print_table(query)

    def to_print_author(self):
        query = 'SELECT * FROM "Author_view"'
        self.labels = ['id', 'ФИО', 'Страна', 'Дата рождения', 'Дата смерти']
        self.to_print_table(query)

    def to_print_book_in_shop(self):
        query = 'SELECT * FROM "Book_in_shop_view"'
        self.labels = ['id', 'Название книги', 'Номер магазина', 'Цена за экземпляр', 'Количество экземпляров', 'Дата поставки']
        self.to_print_table(query)

    def to_print_publish(self):
        query = 'SELECT * FROM "Publish_view"'
        self.labels = ['id', 'Город', 'Год открытия', 'Телефон']
        self.to_print_table(query)

    def to_print_shop(self):
        query = 'SELECT * FROM "Shop_view"'
        self.labels = ['id', 'Номер магазина', 'Район', 'Тип собственности', 'Год открытия']
        self.to_print_table(query)

    def to_print_sm(self):
        query = 'SELECT id, login, departament FROM "Shop_manager" ORDER BY id'
        self.labels = ['id', 'Логин', 'Заведение']
        self.to_print_table(query)


class MainMenu(PrintTable, main_window.Ui_MainWindow):
    def __init__(self, connection, cursor, current_user, role_group):
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
        self.Workers_button.clicked.connect(self.to_add_worker)
        self.Queries_button.clicked.connect(self.queries)
        self.connection = connection
        self.cursor = cursor
        self.current_user = current_user
        self.role_group = role_group

    def queries(self):
        self.q = Queries(self.connection, self.cursor)
        self.q.show()

    def to_add_worker(self):
        self.worker = AddWorker(self.connection, self.cursor, self.current_user, self.role_group)
        self.worker.show()


class PublishMenu(QMainWindow, publish_manager.Ui_Dialog):
    def __init__(self, connection, cursor, current_user, departament, role_group):
        super(PublishMenu, self).__init__()
        self.setupUi(self)
        self.connection = connection
        self.cursor = cursor
        self.current_user = current_user
        self.departament = departament
        self.role_group = role_group
        self.auth_as.setText(f'Вы вошли как: {current_user}, Номер заведения: {self.departament}')
        self.Update_book.clicked.connect(self.to_print_book)
        self.Update_author.clicked.connect(self.to_print_author)
        self.Add_book.clicked.connect(self.to_add_book)
        self.Add_author.clicked.connect(self.to_add_author)

    def to_delete_book(self):
        ...

    def to_delete_author(self):
        ...

    def to_add_book(self):
        book = AddBook(self.connection, self.cursor, self.current_user, self.departament)
        book.exec_()

    def to_add_author(self):
        author = AddAuthor(self.connection, self.cursor, self.current_user)
        author.exec_()

    def to_print_book(self):
        query = f'SELECT "Book".id, "Book".name AS book, "Book".year, "Language".name AS language, "Author".name AS author FROM "Book" LEFT JOIN "Language" ON "Language".id = "Book".language LEFT JOIN "Author" ON "Author".id = "Book".author LEFT JOIN "Publish" ON "Publish".id = "Book".publish WHERE "Publish".id = {self.departament} ORDER BY "Book".id'
        self.labels = ['id', 'Название книги', 'Год выпуска', 'Язык']
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget_3.setRowCount(len(self.rows))
        self.tableWidget_3.setColumnCount(len(self.labels))
        self.tableWidget_3.setHorizontalHeaderLabels(self.labels)
        i = 0
        for elem in self.rows:
            j = 0
            for t in elem:
                self.tableWidget_3.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        i = 0
        self.tableWidget_3.resizeColumnsToContents()

    def to_print_author(self):
        query = 'SELECT * FROM "Author_view"'
        self.labels = ['id', 'ФИО', 'Страна', 'Дата рождения', 'Дата смерти']
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget_2.setRowCount(len(self.rows))
        self.tableWidget_2.setColumnCount(len(self.labels))
        self.tableWidget_2.setHorizontalHeaderLabels(self.labels)
        i = 0
        for elem in self.rows:
            j = 0
            for t in elem:
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        i = 0
        self.tableWidget_2.resizeColumnsToContents()


class ShopMenu(QMainWindow, shop_manager.Ui_Dialog):
    def __init__(self, connection, cursor, current_user, departament, role_group):
        super(ShopMenu, self).__init__()
        self.setupUi(self)
        self.setFixedSize(550, 320)
        self.connection = connection
        self.cursor = cursor
        self.current_user = current_user
        self.departament = departament
        self.role_group = role_group
        self.label_2.setText(f'Вы вошли как: {current_user}, Номер заведения: {self.departament}')
        self.Update_book.clicked.connect(self.to_print_book_in_shop)
        self.Add_book_in_shop.clicked.connect(self.to_add_book_in_shop)
        self.Update_book.clicked.connect(self.to_delete_book_in_shop)

    def to_print_book_in_shop(self):
        query = f'SELECT "Book".id, "Book".name, "Book_in_shop".cost, "Book_in_shop".amount, "Book_in_shop".delivery_date FROM "Book_in_shop" LEFT JOIN "Book" ON "Book".id = "Book_in_shop".book_id LEFT JOIN "Shop" ON "Shop".id = "Book_in_shop".shop_id WHERE "Shop".id = {self.departament}'
        self.labels = ['id', 'Книга', 'Цена', 'Количество', 'Дата поставки']
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

    def to_delete_book_in_shop(self):
        ...

    def to_add_book_in_shop(self):
        book_in_shop = AddBookInShop(self.connection, self.cursor, self.current_user, self.departament)
        book_in_shop.exec_()


class AddWorker(PrintTable, admin.Ui_Dialog):
    def __init__(self, connection, cursor, current_user, role_group):
        super(AddWorker, self).__init__()
        self.setupUi(self)
        self.setFixedSize(1100, 350)
        self.connection = connection
        self.cursor = cursor
        self.current_user = current_user
        self.role_group = role_group
        self.label_2.setText(f'Вы вошли как: {current_user}')
        self.Update_shop.clicked.connect(self.to_print_sm)
        self.Update_pub.clicked.connect(self.to_print_pm)
        self.to_add_pub.clicked.connect(self.add_pm)
        self.to_add_shop.clicked.connect(self.add_sm)
        self.to_delete_shop.clicked.connect(self.to_delete_sm)
        self.to_delete_pub.clicked.connect(self.to_delete_pm)

    def to_delete_pm(self):
        self.pm = Delete(self.connection, self.cursor, self.role_group)
        self.pm.show()

    def to_delete_sm(self):
        self.sm = Delete(self.connection, self.cursor, self.role_group)
        self.sm.show()

    def to_print_pm(self):
        query = 'SELECT id, login, departament FROM "Publish_manager" ORDER BY id'
        self.labels = ['id', 'Логин', 'Заведение']
        self.cursor.execute(query)
        self.rows = self.cursor.fetchall()
        self.tableWidget_2.setRowCount(len(self.rows))
        self.tableWidget_2.setColumnCount(len(self.labels))
        self.tableWidget_2.setHorizontalHeaderLabels(self.labels)
        i = 0
        for elem in self.rows:
            j = 0
            for t in elem:
                self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        i = 0
        self.tableWidget_2.resizeColumnsToContents()

    def add_pm(self):
        pm = AddPm(self.connection, self.cursor)
        pm.exec_()

    def add_sm(self):
        sm = AddSm(self.connection, self.cursor)
        sm.exec_()


class DeleteMessage(QMainWindow, DeleteMessage.Ui_Dialog):
    def __init__(self, connection, cursor):
        super(DeleteMessage, self).__init__()
        self.setupUi(self)
        self.setFixedSize(560, 150)
        self.connection = connection
        self.cursor = cursor
        query = f'SELECT * FROM {table} WHERE id = {id}'
        self.cursor.execute(query)
        self.text.setText(f'Вы действительно хотите удалить {self.cursor.fetchall()}')
        self.OKbutton.clicked.connect(self.delete)
        self.CancelButton.clicked.connect(self.cancel)

    def delete(self):
        try:
            query = f'DELETE FROM {table} WHERE id = {id}'
            self.cursor.execute(query)
            self.connection.commit()
            self.error.setText('Удалено!')
        except Exception as err:
            print(err)
            self.error.setText('Ошибка!')

    def cancel(self):
        self.close()


class Delete(QMainWindow, delete.Ui_Dialog):
    def __init__(self, connection, cursor, role_group):
        super(Delete, self).__init__()
        self.setupUi(self)
        self.role_group = role_group
        self.connection = connection
        self.cursor = cursor
        if role_group == 'admins':
            self.table.addItem('Район')
            self.table.addItem('Город')
            self.table.addItem('Страна')
            self.table.addItem('Тип собственности')
            self.table.addItem('Язык')
            self.table.addItem('Менеджер магазина')
            self.table.addItem('Менеджер издательства')
        elif role_group == 'publish_manager':
            self.table.addItem('Книга')
            self.table.addItem('Автор')
            self.table.addItem('Издательство')
        elif role_group == 'shop_manager':
            self.table.addItem('Книга в магазине')
            self.table.addItem('Магазин')
        self.OKbutton.clicked.connect(self.to_delete)

    def to_delete(self):
        global id
        id = self.id.text()
        global table
        if self.table.currentText() == 'Район':
            table = '"District"'
        elif self.table.currentText() == 'Город':
            table = '"City"'
        elif self.table.currentText() == 'Страна':
            table = '"Country"'
        elif self.table.currentText() == 'Тип собственности':
            table = '"Property_type"'
        elif self.table.currentText() == 'Язык':
            table = '"Language"'
        elif self.table.currentText() == 'Менеджер магазина':
            table = '"Shop_manager"'
        elif self.table.currentText() == 'Менеджер издательства':
            table = '"Publish_manager"'
        elif self.table.currentText() == 'Книга':
            table = '"Book"'
        elif self.table.currentText() == 'Автор':
            table = '"Author"'
        elif self.table.currentText() == 'Книга в магазине':
            table = '"Book_in_shop"'
        elif self.table.currentText() == 'Издательство':
            table = '"Book"'
        elif self.table.currentText() == 'Магазин':
            table = '"Author"'
        self.message = DeleteMessage(self.connection, self.cursor)
        self.message.show()


class Queries(QMainWindow, queries.Ui_Dialog):
    def __init__(self, connection, cursor):
        super(Queries, self).__init__()
        self.setupUi(self)
        self.connection = connection
        self.cursor = cursor
        self.queries.currentTextChanged.connect(self.handle_queries_change)  # Подключение сигнала
        self.queries.addItem('Магазины в выбранном районе. Симметричное внутреннее соединение с условием отбора по внешнему ключу')
        self.queries.addItem('Авторы из выбранной страны. Симметричное внутреннее соединение с условием отбора по внешнему ключу')
        self.queries.addItem('Магазины, открытые в выбранном году. Симметричное внутреннее соединение с условием отбора по датам')
        self.queries.addItem('Магазины, открытые между выбранными годами. Симметричное внутреннее соединение с условием отбора по датам')
        self.queries.addItem('Номер магазина, район и год открытия. Симметричное внутреннее соединение без условия')
        self.queries.addItem('Дата рождения, имя и страна автора. Номер магазина, район и год открытия. Симметричное внутреннее соединение без условия')
        self.queries.addItem('Автор, название и язык его книги. Симметричное внутреннее соединение без условия')
        self.queries.addItem('Имя, страна, дата рождения и дата смерти автора. Левое внешнее соединение')
        self.queries.addItem('Имя, страна, дата рождения и дата смерти автора. Правое внешнее соединение')
        self.queries.addItem('Имя, страна, дата рождения и дата смерти выбранного автора. Запрос на запросе по принципу левого соединения')
        self.queries.addItem('ID издания, количество выпущенных книг. Итоговый запрос без условия')
        self.queries.addItem('ID издания, количество выпущенных книг. Итоговый запрос с условием на данные')
        self.queries.addItem('ID издания, количество выпущенных книг. Итоговый запрос с условием на группы')
        self.queries.addItem('ID издания, количество выпущенных книг. Итоговый запрос с условием на данные и на группы')
        self.queries.addItem('ID издания, количество выпущенных книг. Запрос на запросе по принципу итогового запроса')
        self.queries.addItem('ID издания, город, количество выпущенных книг. Запрос с подзапросом')

    def handle_queries_change(self):
        if self.queries.currentText() == 'Магазины в выбранном районе. Симметричное внутреннее соединение с условием отбора по внешнему ключу':
            self.hide_all()
            self.label_combo.show()
            self.label_combo.setText('Выберите район')
            self.comboBox.show()
            query = 'SELECT id, name FROM "District"'
            self.cursor.execute(query)
            for t in self.cursor.fetchall():
                self.comboBox.addItem(str(t))
            district = self.comboBox.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
            district_id = str(district[0])
            self.labels = ['Номер магазина', 'Район', 'Год открытия']
            self.query = f'SELECT * FROM query1({district_id})'
            self.comboBox.currentTextChanged.connect(self.q1)
        elif self.queries.currentText() == 'Авторы из выбранной страны. Симметричное внутреннее соединение с условием отбора по внешнему ключу':
            self.hide_all()
            self.label_combo.show()
            self.comboBox.show()
            self.label_combo.setText('Выберите страну')
            self.comboBox.show()
            query = 'SELECT id, name FROM "Country"'
            self.cursor.execute(query)
            for t in self.cursor.fetchall():
                self.comboBox.addItem(str(t))
            country = self.comboBox.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
            country_id = str(country[0])
            self.labels = ['Дата рождения', 'Автор', 'Страна']
            self.query = f'SELECT * FROM query2({country_id})'
            self.comboBox.currentTextChanged.connect(self.q2)
        elif self.queries.currentText() == 'Магазины, открытые в выбранном году. Симметричное внутреннее соединение с условием отбора по датам':
            self.hide_all()
            self.label_text.show()
            self.textEdit.show()
            self.textEdit.setText('')
            self.label_text.setText('Выберите год')
            self.textEdit.textChanged.connect(self.q3)  # Подключение сигнала
        elif self.queries.currentText() == 'Магазины, открытые между выбранными годами. Симметричное внутреннее соединение с условием отбора по датам':
            self.hide_all()
            self.label_text.show()
            self.textEdit.show()
            self.label_text_2.show()
            self.textEdit_2.show()
            self.textEdit.setText('')
            self.textEdit_2.setText('')
            self.label_text.setText('Выберите начальный год')
            self.label_text_2.setText('Выберите конечный год')
            self.textEdit.textChanged.connect(self.q4)
            self.textEdit_2.textChanged.connect(self.q4)
        elif self.queries.currentText() == 'Номер магазина, район и год открытия. Симметричное внутреннее соединение без условия':
            self.hide_all()
            self.labels = ['Номер магазига', 'Район', 'Год открытия']
            self.query = 'SELECT * FROM query5()'
        elif self.queries.currentText() == 'Дата рождения, имя и страна автора. Номер магазина, район и год открытия. Симметричное внутреннее соединение без условия':
            self.hide_all()
            self.labels = ['Дата рождения', 'Автор', 'Страна']
            self.query = 'SELECT * FROM query6()'
        elif self.queries.currentText() == 'Автор, название и язык его книги. Симметричное внутреннее соединение без условия':
            self.hide_all()
            self.labels = ['ФИО', 'Книга', 'Язык']
            self.query = f'SELECT * FROM query7()'
        elif self.queries.currentText() == 'Имя, страна, дата рождения и дата смерти автора. Левое внешнее соединение':
            self.hide_all()
            self.labels = ['ФИО', 'Страна', 'Дата рождения', 'Дата смерти']
            self.query = f'SELECT * FROM query8()'
        elif self.queries.currentText() == 'Имя, страна, дата рождения и дата смерти автора. Правое внешнее соединение':
            self.hide_all()
            self.labels = ['ФИО', 'Страна', 'Дата рождения', 'Дата смерти']
            self.query = f'SELECT * FROM query9()'
        elif self.queries.currentText() == 'Имя, страна, дата рождения и дата смерти выбранного автора. Запрос на запросе по принципу левого соединения':
            self.hide_all()
            self.textEdit.setText('')
            self.label_text.show()
            self.textEdit.show()
            self.label_text.setText('Выберите имя')
            self.textEdit.textChanged.connect(self.q10)
        elif self.queries.currentText() == 'ID издания, количество выпущенных книг. Итоговый запрос без условия':
            self.hide_all()
            self.labels = ['ID издания', 'Количество выпущенных книг']
            self.query = f'SELECT * FROM query11()'
        elif self.queries.currentText() == 'ID издания, количество выпущенных книг. Итоговый запрос с условием на данные':
            self.hide_all()
            self.label_text.show()
            self.textEdit.show()
            self.label_text_2.show()
            self.textEdit_2.show()
            self.textEdit.setText('')
            self.textEdit_2.setText('')
            self.label_text.setText('Выберите начальный ID издательства')
            self.label_text_2.setText('Выберите конечный ID издательства')
            self.textEdit.textChanged.connect(self.q12)
            self.textEdit_2.textChanged.connect(self.q12)
        elif self.queries.currentText() == 'ID издания, количество выпущенных книг. Итоговый запрос с условием на группы':
            self.hide_all()
            self.label_text.show()
            self.textEdit.show()
            self.label_text.setText('Выберите количество книг')
            self.textEdit.textChanged.connect(self.q13)
        elif self.queries.currentText() == 'ID издания, количество выпущенных книг. Итоговый запрос с условием на данные и на группы':
            self.hide_all()
            self.label_text.show()
            self.textEdit.show()
            self.label_text_2.show()
            self.textEdit_2.show()
            self.label_text_3.show()
            self.textEdit_3.show()
            self.textEdit.setText('')
            self.textEdit_2.setText('')
            self.label_text.setText('Выберите начальный ID издательства')
            self.label_text_2.setText('Выберите конечный ID издательства')
            self.label_text_3.setText('Выберите количество книг')
            self.textEdit.textChanged.connect(self.q14)
            self.textEdit_2.textChanged.connect(self.q14)
            self.textEdit_3.textChanged.connect(self.q14)
        elif self.queries.currentText() == 'ID издания, количество выпущенных книг. Запрос на запросе по принципу итогового запроса':
            self.hide_all()
            self.label_text.show()
            self.textEdit.show()
            self.label_text.setText('Выберите количество книг')
            self.textEdit.textChanged.connect(self.q15)
        elif self.queries.currentText() == 'ID издания, город, количество выпущенных книг. Запрос с подзапросом':
            self.hide_all()
            self.label_combo.show()
            self.comboBox.show()
            self.label_combo.setText('Выберите город')
            self.comboBox.show()
            query = 'SELECT id, name FROM "City"'
            self.cursor.execute(query)
            for t in self.cursor.fetchall():
                self.comboBox.addItem(str(t))
            city = self.comboBox.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
            city_id = str(city[0])
            self.labels = ['ID издания', 'Город', 'Количество выпущенных книг']
            self.query = f'SELECT * FROM query16({city_id})'
            self.comboBox.currentTextChanged.connect(self.q16)

        self.print.clicked.connect(self.to_print)

    def q1(self):
        district = self.comboBox.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        district_id = str(district[0])
        self.labels = ['Номер магазина', 'Район', 'Год открытия']
        self.query = f'SELECT * FROM query1({district_id})'

    def q2(self):
        country = self.comboBox.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        country_id = str(country[0])
        self.labels = ['Дата рождения', 'Автор', 'Страна']
        self.query = f'SELECT * FROM query2({country_id})'

    def q3(self):
        year = self.textEdit.text()
        self.labels = ['Номер магазига', 'Район', 'Год открытия']
        self.query = f'SELECT * FROM query3({year})'

    def q4(self):
        year1 = self.textEdit.text()
        year2 = self.textEdit_2.text()
        self.labels = ['Номер магазига', 'Район', 'Год открытия']
        self.query = f'SELECT * FROM query4({year1}, {year2})'

    def q10(self):
        name = self.textEdit.text()
        self.labels = ['id Автора', 'ФИО', 'Страна', 'Дата рождения', 'Дата смерти']
        self.query = f"SELECT * FROM query10('{name}')"

    def q12(self):
        publish1 = self.textEdit.text()
        publish2 = self.textEdit_2.text()
        self.labels = ['ID издания', 'Количество выпущенных книг']
        self.query = f'SELECT * FROM query12({publish1}, {publish2})'

    def q13(self):
        book_count = self.textEdit.text()
        self.labels = ['ID издания', 'Количество выпущенных книг']
        self.query = f'SELECT * FROM query13({book_count})'

    def q14(self):
        id1 = self.textEdit.text()
        id2 = self.textEdit_2.text()
        book_count = self.textEdit_3.text()
        self.labels = ['ID издания', 'Количество выпущенных книг']
        self.query = f'SELECT * FROM query14({id1}, {id2}, {book_count})'

    def q15(self):
        book_count = self.textEdit.text()
        self.labels = ['ID издания', 'Количество выпущенных книг']
        self.query = f'SELECT * FROM query15({book_count})'

    def q16(self):
        query = 'SELECT id, name FROM "City"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.comboBox.addItem(str(t))
        city = self.comboBox.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        city_id = str(city[0])
        self.query = f'SELECT * FROM query16({city_id})'

    def hide_all(self):
        self.label_text.hide()
        self.textEdit.hide()
        self.label_combo.hide()
        self.comboBox.hide()
        self.label_text_2.hide()
        self.comboBox.clear()
        self.textEdit_2.hide()
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.label_text_3.hide()
        self.textEdit_3.hide()

    def to_print(self):
        try:
            self.cursor.execute(self.query)
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
        except psycopg2.Error as err:
            print(err)
            self.error.setText('Проверьте ввод!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()

    window.show()
    sys.exit(app.exec_())
