class Database:
    def __init__(self, name):
        self.name = name
        self.tables = {}

    def create_table(self, name, fields):
        if name in self.tables:
            return False, "Такая таблица уже существует😡"

        self.tables[name] = {
            'fields': fields,
            'data': {},
            'next_id': 1
        }
        return True, "Таблица создана успешно☺️"

    def show_tables(self):
        return list(self.tables.keys())

    def show_table_structure(self, table_name):
        if table_name not in self.tables:
            return None
        return self.tables[table_name]['fields']

    def get_table_data(self, table_name):
        if table_name not in self.tables:
            return None
        return self.tables[table_name]

    def add_data(self, table_name, data):
        if table_name not in self.tables:
            return False, "Такая таблица не найдена😥"

        table = self.tables[table_name]

        for i, value in enumerate(data):
            field_type = table['fields'][i][1]
            if not self.check_type(value, field_type):
                return False, f"Неверный тип данных для поля {table['fields'][i][0]}"

        table['data'][table['next_id']] = data
        table['next_id'] += 1
        return True, "Данные были успешно добавлены🥰"

    def check_type(self, value, type_name):
        try:
            if type_name == 'int':
                int(value)
            elif type_name == 'float':
                float(value)
            elif type_name == 'bool':
                if value.lower() not in ['true', 'false', '1', '0']:
                    return False
            return True
        except:
            return False


class DatabaseSystem:
    def __init__(self):
        self.databases = {}
        self.current_db = None

    def create_database(self, name):
        if name in self.databases:
            return False, "База данных с таким именем уже существует😡"
        self.databases[name] = Database(name)
        return True, "База данных создана успешно🥰"

    def show_databases(self):
        return list(self.databases.keys())

    def use_database(self, name):
        if name not in self.databases:
            return False, "База данных не найдена😥"
        self.current_db = self.databases[name]
        return True, f"Используется база данных: {name}"

    def get_current_db(self):
        return self.current_db


class DatabaseApp:
    def __init__(self):
        self.system = DatabaseSystem()

    def show_menu(self):
        print("\n" + "⁓" * 50)
        print("СИСТЕМА УПРАВЛЕНИЯ БАЗАМИ ДАННЫХ")
        print("⁓" * 50)

        if self.system.current_db:
            print(f"Текущая БД: {self.system.current_db.name}")
            print("\n" + ("♡" + " ") * 20)
            print("1. Работа с таблицами")
            print("2. Показ всех таблиц")
            print("3. Смена базы данных")
            print(("♡" + " ") * 20)
        else:
            print("\n" + ("♡" + " ") * 20)
            print("1. Создание базы данных")
            print("2. Выбор базы данных")
            print("3. Показ всех баз данных")
            print("4. Обучение")
            print("0. Выход")
            print(("♡" + " ") * 20)

    def run(self):
        print("\nЗдравствуйте!👋  Добро пожаловать в систему управления базами данных.")

        while True:
            self.show_menu()
            choice = input("\n🤗 Выберите действие: ")

            if choice == "0":
                print("\nУже уходите?")
                print("Всего хорошего!😚")
                break

            elif choice == "1":
                if self.system.current_db:
                    self.table_menu()
                else:
                    self.create_database()

            elif choice == "2":
                if self.system.current_db:
                    self.show_tables()
                else:
                    self.use_database()

            elif choice == "3":
                if self.system.current_db:
                    self.change_database()
                else:
                    self.show_databases()

            elif choice == "4":
                self.show_tutorial()

            else:
                print("Неверный выбор😥. Попробуйте снова.")

    def create_database(self):
        name = input("Введите название базы данных: ")
        success, message = self.system.create_database(name)
        print(message)

    def show_databases(self):
        dbs = self.system.show_databases()
        if dbs:
            print("Существующие базы данных:")
            for db in dbs:
                print(f"- {db}")
        else:
            print("Базы данных отсутствуют😥")

    def use_database(self):
        self.show_databases()
        name = input("Введите название базы данных: ")
        success, message = self.system.use_database(name)
        print(message)

    def change_database(self):
        self.system.current_db = None
        print("Текущая база данных сброшена")

    def show_tables(self):
        if not self.system.current_db:
            print("База данных не выбрана😡")
            return

        tables = self.system.current_db.show_tables()
        if tables:
            print("Таблицы в текущей базе данных:")
            for table in tables:
                print(f"- {table}")
        else:
            print("Таблицы отсутствуют😥")

    def table_menu(self):
        while True:
            print("\n♡♡♡ РАБОТА С ТАБЛИЦАМИ ♡♡♡")
            print("1. Создание таблицы")
            print("2. Добавление данных")
            print("3. Показ таблицы с данными")
            print("0. Назад")

            choice = input("\n🤗 Выберите действие: ")

            if choice == "0":
                break
            elif choice == "1":
                self.create_table()
            elif choice == "2":
                self.add_data()
            elif choice == "3":
                self.show_table_structure()
            else:
                print("Неверный выбор😥")

    def create_table(self):
        name = input("Введите название таблицы: ")

        print('Добавление полей (введите "ok" для завершения):')
        fields = []

        while True:
            field_name = input("Название поля: ")
            if field_name.lower() == 'ok':
                break

            field_type = input("Тип поля (int/float/string/bool): ")
            if field_type not in ['int', 'float', 'string', 'bool']:
                print("Неверный тип поля😥")
                continue

            fields.append((field_name, field_type))

        if fields:
            success, message = self.system.current_db.create_table(name, fields)
            print(message)
        else:
            print("Таблица должна содержать хотя бы одно поле")

    def add_data(self):
        table_name = input("Введите название таблицы: ")

        if table_name not in self.system.current_db.tables:
            print("Таблица не найдена😥")
            return

        table = self.system.current_db.tables[table_name]
        data = []

        for field_name, field_type in table['fields']:
            value = input(f"Введите значение для {field_name} ({field_type}): ")
            data.append(value)

        success, message = self.system.current_db.add_data(table_name, data)
        print(message)

    def show_table_structure(self):
        if not self.system.current_db:
            print("База данных не выбрана😥")
            return

        table_name = input("Введите название таблицы: ")

        if table_name not in self.system.current_db.tables:
            print("Таблица не найдена😥")
            return

        table = self.system.current_db.tables[table_name]

        print(f"\n♡♡♡ ТАБЛИЦА: {table_name} ♡♡♡")

        headers = ["ID"] + [field[0] for field in table['fields']]

        all_rows = []
        if table['data']:
            for record_id, data in table['data'].items():
                row = [str(record_id)] + [str(value) for value in data]
                all_rows.append(row)

        column_widths = []
        for i in range(len(headers)):
            max_width = len(headers[i])

            for row in all_rows:
                if len(row[i]) > max_width:
                    max_width = len(row[i])

            column_widths.append(max_width + 2)

        def format_row(row_data):
            formatted_cells = []
            for i, cell in enumerate(row_data):
                formatted_cells.append(cell.ljust(column_widths[i]))
            return " | ".join(formatted_cells)

        total_width = sum(column_widths) + 3 * (len(headers) - 1)
        print("-" * total_width)

        print(format_row(headers))
        print("-" * total_width)

        if all_rows:
            for row in all_rows:
                print(format_row(row))
        else:
            print("Таблица пуста😥".center(total_width))

        print("-" * total_width)
        print(f"Всего записей: {len(table['data'])}")

    def show_tutorial(self):
        print("\n" + ("♡" + " ") * 20)
        print("ОБУЧЕНИЕ ПО СИСТЕМЕ")
        print("⁓" * 50)
        print("1. Сначала создайте базу данных")
        print("2. Выберите базу данных для работы")
        print("3. В выбранной БД создавайте таблицы с полями")
        print("4. Добавляйте данные в таблицы")
        print("5. Поддерживаемые типы данных: int, float, string, bool")
        print(("♡" + " ") * 20)


if __name__ == "__main__":
    app = DatabaseApp()
    app.run()