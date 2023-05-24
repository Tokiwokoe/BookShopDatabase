import datetime

from PyQt5.QtWidgets import QDialog
from UIclass import add_book, add_author


class AddBook(QDialog, add_book.Ui_Dialog):
    def __init__(self, connection, cursor, current_user, role_group):
        super(AddBook, self).__init__()
        self.setupUi(self)
        self.setFixedSize(650, 320)
        self.connection = connection
        self.cursor = cursor
        self.current_user = current_user
        self.role_group = role_group
        self.Add.clicked.connect(self.correct_data)
        query = 'SELECT id, name FROM "Language"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.lang.addItem(str(t))
        query = 'SELECT id, name FROM "Author"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.author.addItem(str(t))
        query = 'SELECT "Publish".id, "City".name, phone FROM "Publish" LEFT JOIN "City" ON "City".id = "Publish".city'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.publish.addItem(str(t))

    def correct_data(self):
        name = self.name.text().strip()
        year = self.year.text()
        lang = self.lang.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        author = self.author.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        publish = self.publish.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        lang_id = str(lang[0])
        author_id = str(author[0])
        publish_id = str(publish[0])
        if 2023 >= int(year) >= 1980:
            try:
                query = 'SELECT id FROM "Book" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                query = f"INSERT INTO \"Book\" VALUES({int(self.id[0]) + 1}, '{name}', {year}, {lang_id}, {author_id}, {publish_id})"
                self.cursor.execute(query)
                self.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')


class AddAuthor(QDialog, add_author.Ui_Dialog):
    def __init__(self, connection, cursor, current_user, role_group):
        super(AddAuthor, self).__init__()
        self.setupUi(self)
        self.setFixedSize(650, 280)
        self.connection = connection
        self.cursor = cursor
        self.current_user = current_user
        self.role_group = role_group
        self.Add.clicked.connect(self.correct_data)
        query = 'SELECT id, name FROM "Country"'
        self.cursor.execute(query)
        for t in self.cursor.fetchall():
            self.country.addItem(str(t))

    def correct_data(self):
        name = self.name.text().strip()
        country = self.country.currentText().replace('(', '').replace(')', '').replace(' \'', '\'').split(',')
        birth = self.birth.text()
        country_id = str(country[0])
        if int(birth[6:]) < datetime.date.today().year - 18:
            try:
                query = 'SELECT id FROM "Author" ORDER BY id DESC LIMIT 1'
                self.cursor.execute(query)
                self.id = self.cursor.fetchone()
                if self.checkBox.checkState():
                    death = self.death.text()
                    if int(birth[6:]) < int(death[6:]) + 18:
                        query = f"INSERT INTO \"Author\"(id, name, country, birth_date, death_date) VALUES({int(self.id[0]) + 1}, '{name}', {country_id}, '{birth}', '{death}')"
                else:
                    query = f"INSERT INTO \"Author\"(id, name, country, birth_date) VALUES({int(self.id[0]) + 1}, '{name}', {country_id}, '{birth}')"
                self.cursor.execute(query)
                self.connection.commit()
                self.error.setText('Успешно добавлено')
            except Exception as err:
                print(err)
                self.error.setText('Что-то пошло не так :(')
        else:
            self.error.setText('Проверьте корректность заполнения полей!')