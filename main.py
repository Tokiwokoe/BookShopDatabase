import sys
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from AddClasses import AddBook, AddAuthor, AddBookInShop, AddPm, AddSm
from UIclass import main_window, LoginScreen, publish_manager, shop_manager, admin, delete, DeleteMessage


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
        self.labels = ['Язык']
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
        self.connection = connection
        self.cursor = cursor
        self.current_user = current_user
        self.role_group = role_group

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AuthWindow()

    window.show()
    sys.exit(app.exec_())
