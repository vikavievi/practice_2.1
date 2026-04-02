class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "доступна" if self.available else "выдана"
        return f"'{self.title}' - {self.author} ({self.year}) [{status}]"


class Reader:
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"Книга '{book.title}' выдана читателю {self.name}")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"Книга '{book.title}' возвращена читателем {self.name}")
        else:
            print(f"Ошибка: книга '{book.title}' не была выдана этому читателю")

    def show_borrowed_books(self):
        if self.borrowed_books:
            print(f"Книги читателя {self.name}:")
            for book in self.borrowed_books:
                print(f"  - {book.title} ({book.author})")
        else:
            print(f"У читателя {self.name} нет выданных книг")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                print("Ошибка: книга с таким ISBN уже существует")
                return
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку")

    def show_all_books(self):
        print("\nВСЕ КНИГИ В БИБЛИОТЕКЕ")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def show_available_books(self):
        print("\nДОСТУПНЫЕ КНИГИ")
        available_books = [book for book in self.books if book.available]
        if available_books:
            for i, book in enumerate(available_books, 1):
                print(f"{i}. {book}")
        else:
            print("Нет доступных книг")

    def borrow_book(self, book_index, reader):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if book.available:
                book.available = False
                reader.borrow_book(book)
            else:
                print("Ошибка: книга уже выдана")
        else:
            print("Ошибка: неверный номер книги")

    def return_book(self, book_index, reader):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.available:
                book.available = True
                reader.return_book(book)
            else:
                print("Ошибка: книга уже доступна в библиотеке")
        else:
            print("Ошибка: неверный номер книги")


def create_library():
    """Создает библиотеку с 5 предустановленными книгами"""
    library = Library()

    books_data = [
        ("Как выспаться за 3 часа", "Андрей Неупокоев", 2022, "111"),
        ("Беременна в 16", "Телеканал Ю", 2025, "222"),
        ("Лекарство от нервов", "Надеюсь Придумают", 2030, "333"),
        ("Как выселить соседей", "Хватит Сверлить", 2015, "444"),
        ("Сессия автоматом", "Мои Мечты", 2026, "555")
    ]

    for title, author, year, isbn in books_data:
        book = Book(title, author, year, isbn)
        library.add_book(book)

    return library


def main():
    print("БИБЛИОТЕЧНАЯ СИСТЕМА")
def main():
    print("БИБЛИОТЕЧНАЯ СИСТЕМА")
    reader_name = input("Введите ваше имя: ").strip()
    if not reader_name:
        reader_name = "Читатель"
        print("Имя не введено, установлено: 'Читатель'")

    reader = Reader(reader_name, "001")
    library = create_library()

    print(f"\nДобро пожаловать, {reader_name}!")
    print("Библиотека содержит 5 книг:")

    while True:
        library.show_all_books()

        print("\nВыберите операцию:")
        print("1 - Взять книгу")
        print("2 - Вернуть книгу")
        print("3 - Показать доступные книги")
        print("4 - Мои книги")
        print("0 - Выход")

        choice = input("Ваш выбор: ").strip()

        match choice:
            case "1":
                library.show_available_books()
                try:
                    book_num = int(input("Введите номер книги для выдачи: "))
                    library.borrow_book(book_num, reader)
                except ValueError:
                    print("Ошибка: введите число")

            case "2":
                if reader.borrowed_books:
                    print("\nВаши выданные книги:")
                    for i, book in enumerate(reader.borrowed_books, 1):
                        print(f"{i}. {book.title}")

                    try:
                        return_num = int(input("Введите номер книги для возврата: "))
                        if 1 <= return_num <= len(reader.borrowed_books):
                            book_to_return = reader.borrowed_books[return_num - 1]
                            for idx, lib_book in enumerate(library.books, 1):
                                if lib_book.isbn == book_to_return.isbn:
                                    library.return_book(idx, reader)
                                    break
                        else:
                            print("Ошибка: неверный номер книги")
                    except ValueError:
                        print("Ошибка: введите число")
                else:
                    print("У вас нет книг для возврата")

            case "3":
                library.show_available_books()

            case "4":
                reader.show_borrowed_books()

            case "0":
                print(f"\nИТОГОВАЯ ИНФОРМАЦИЯ")
                print(f"Читатель: {reader_name}")
                reader.show_borrowed_books()
                print("Выход из системы. До свидания!")
                break

            case _:
                print("Ошибка: выберите операцию от 0 до 4")


if __name__ == "__main__":
    main()
