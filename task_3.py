import csv
import os

CSV_FILE = "products.csv"

INITIAL_DATA = [
    ["Название", "Цена", "Количество"],
    ["Яблоки", "100", "50"],
    ["Бананы", "80", "30"],
    ["Молоко", "120", "20"],
    ["Хлеб", "40", "100"]
]


def load_products():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(INITIAL_DATA)
        print(f"Создан файл {CSV_FILE} с начальными данными.")

    products = []
    with open(CSV_FILE, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader)

        for row in reader:
            if row:
                product = {
                    "name": row[0],
                    "price": int(row[1]),
                    "quantity": int(row[2])
                }
                products.append(product)

    return products

def save_products(products):
    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Название", "Цена", "Количество"])

        for product in products:
            writer.writerow([product["name"], product["price"], product["quantity"]])

def add_product(products):
    name = input("Введите название товара: ")
    name = name.strip()

    if name == "":
        print("Название не может быть пустым.")
        return

    try:
        price = int(input("Введите цену: "))
    except ValueError:
        print("Цена должна быть числом.")
        return

    try:
        quantity = int(input("Введите количество: "))
    except ValueError:
        print("Количество должно быть числом.")
        return

    for product in products:
        if product["name"].lower() == name.lower():
            print("Товар с таким названием уже существует.")
            return

    new_product = {"name": name, "price": price, "quantity": quantity}
    products.append(new_product)
    print(f"Товар '{name}' добавлен.")


def search_product(products):
    query = input("Введите название для поиска: ")
    query = query.strip().lower()

    found = []
    for product in products:
        if query in product["name"].lower():
            found.append(product)

    if len(found) > 0:
        print("\nНайденные товары:")
        for product in found:
            print(f"{product['name']} | Цена: {product['price']} | Количество: {product['quantity']}")
    else:
        print("Ничего не найдено.")


def total_value(products):
    total = 0
    for product in products:
        total = total + product["price"] * product["quantity"]

    print(f"Общая стоимость всех товаров на складе: {total} руб.")


def show_products(products):
    if len(products) == 0:
        print("Список товаров пуст.")
    else:
        print("\nСписок товаров:")
        for product in products:
            print(f"{product['name']} | Цена: {product['price']} | Количество: {product['quantity']}")


def main():
    products = load_products()

    while True:
        print("\nУПРАВЛЕНИЕ СКЛАДОМ")
        print("1. Показать все товары")
        print("2. Добавить товар")
        print("3. Поиск товара")
        print("4. Рассчитать общую стоимость")
        print("5. Сохранить и выйти")

        choice = input("Выберите действие: ")
        choice = choice.strip()

        if choice == "1":
            show_products(products)

        elif choice == "2":
            add_product(products)

        elif choice == "3":
            search_product(products)

        elif choice == "4":
            total_value(products)

        elif choice == "5":
            save_products(products)
            print("Данные сохранены. До свидания!")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")

main()