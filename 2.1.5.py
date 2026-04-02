import json
import os

FILE_NAME = "library.json"

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        initial_books = [
            {
                "id": 1,
                "title": "Мастер и Маргарита",
                "author": "Булгаков",
                "year": 1967,
                "available": True
            },
            {
                "id": 2,
                "title": "Преступление и наказание",
                "author": "Достоевский",
                "year": 1866,
                "available": False
            }
        ]
        save_books(initial_books)
        return initial_books

def save_books(books):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

def get_next_id(books):
    if not books:
        return 1
    return max(book["id"] for book in books) + 1

def view_all_books(books):
    if not books:
        print("\nБиблиотека пуста!\n")
        return

    print("СПИСОК ВСЕХ КНИГ:")
    for book in books:
        status = "Доступна" if book["available"] else "Выдана"
        print(f"ID: {book['id']} | {book['title']}")
        print(f"   Автор: {book['author']}")
        print(f"   Год: {book['year']}")
        print(f"   Статус: {status}")

def search_books(books):
    if not books:
        print("\nБиблиотека пуста!\n")
        return

    search_term = input("\nВведите название книги или автора: ").lower()

    found_books = []
    for book in books:
        if search_term in book["title"].lower() or search_term in book["author"].lower():
            found_books.append(book)

    if found_books:
        print(f"\nНайдено книг: {len(found_books)}")
        for book in found_books:
            status = "Доступна" if book["available"] else "Выдана"
            print(f"ID: {book['id']} | {book['title']} - {book['author']} ({book['year']}) - {status}")
    else:
        print("\nКниги не найдены!")

def add_book(books):
    print("\nДОБАВЛЕНИЕ НОВОЙ КНИГИ:")
    title = input("Введите название: ").strip()
    author = input("Введите автора: ").strip()

    while True:
        try:
            year = int(input("Введите год издания: "))
            break
        except ValueError:
            print("Ошибка! Введите число.")

    new_book = {
        "id": get_next_id(books),
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }

    books.append(new_book)
    save_books(books)
    print(f"\nКнига '{title}' успешно добавлена! ID: {new_book['id']}")

def change_status(books):
    if not books:
        print("\nБиблиотека пуста!\n")
        return

    view_all_books(books)

    try:
        book_id = int(input("\nВведите ID книги: "))

        for book in books:
            if book["id"] == book_id:
                current_status = "доступна" if book["available"] else "выдана"
                print(f"\nТекущий статус: {current_status}")

                book["available"] = not book["available"]
                new_status = "доступна" if book["available"] else "выдана"

                save_books(books)
                print(f"Статус изменен на: {new_status}")
                return

        print("Книга с таким ID не найдена!")

    except ValueError:
        print("Ошибка! Введите корректный ID.")

def delete_book(books):
    if not books:
        print("\nБиблиотека пуста!\n")
        return

    view_all_books(books)

    try:
        book_id = int(input("\nВведите ID книги для удаления: "))

        for i, book in enumerate(books):
            if book["id"] == book_id:
                confirm = input(f"Вы уверены, что хотите удалить '{book['title']}'? (да/нет): ")
                if confirm.lower() == "да":
                    deleted_book = books.pop(i)
                    save_books(books)
                    print(f"Книга '{deleted_book['title']}' удалена!")
                else:
                    print("Удаление отменено.")
                return

        print("Книга с таким ID не найдена!")

    except ValueError:
        print("Ошибка! Введите корректный ID.")

def export_available_books(books):
    available_books = [book for book in books if book["available"]]

    if not available_books:
        print("\nНет доступных книг для экспорта!")
        return

    with open("available_books.txt", 'w', encoding='utf-8') as file:
        file.write("ДОСТУПНЫЕ КНИГИ В БИБЛИОТЕКЕ\n")

        for book in available_books:
            file.write(f"ID: {book['id']}\n")
            file.write(f"Название: {book['title']}\n")
            file.write(f"Автор: {book['author']}\n")
            file.write(f"Год: {book['year']}\n")

    print(f"\nЭкспорт выполнен! Доступные книги сохранены в файл 'available_books.txt'")
    print(f"Всего доступных книг: {len(available_books)}")

def main():
    books = load_books()

    while True:
        print("БИБЛИОТЕЧНАЯ СИСТЕМА")
        print("1. Просмотр всех книг")
        print("2. Поиск книги")
        print("3. Добавить книгу")
        print("4. Изменить статус книги")
        print("5. Удалить книгу")
        print("6. Экспорт доступных книг")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            view_all_books(books)
        elif choice == "2":
            search_books(books)
        elif choice == "3":
            add_book(books)
        elif choice == "4":
            change_status(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "6":
            export_available_books(books)
        elif choice == "7":
            print("\nДо свидания!")
            break
        else:
            print("\nОшибка! Выберите номер от 1 до 7.")

if __name__ == "__main__":
    main()