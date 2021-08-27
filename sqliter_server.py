import sqlite3


class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def store_data(self, id, time, description, amount):
        with self.connection:
            return self.cursor.execute('INSERT INTO `expenses` (`id`, `time`, `description`, `amount`) VALUES(?,?,?,?)',
                                       (id, time, description, amount))

    def double_check(self):
        with self.connection:
            result = self.cursor.execute('SELECT `id` FROM `expenses`').fetchall()
            return result[-1][0]

    def get_data(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM `expenses`').fetchall()