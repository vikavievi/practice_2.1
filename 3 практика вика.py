def check():
    while True:
        numbers = input("\nВведите ваш список чисел через пробел: ")
        if not numbers.strip():
            print("Введена пустая строка! Введите целые числа")
            continue
        try:
            list1 = list(map(int, numbers.split()))
            return list1
        except ValueError:
                print("\nОшибка! Пожалуйста, вводите только целые числа")

list1 = check()

while True:
    input("Нажмите Enter для показа меню")
    print("Выберите действие: ")
    print("1.Сортировка по возрастанию")
    print("2.Сортировка по убыванию")
    print("3.Нахождения минимального и максимального числа")
    print("4.Приведения чисел к ASCII таблице, и вывод получившихся символов")
    print("5.Выход из программы")
    a = input("\nЗапишите номер действия: ")

    match a:
        case "1":
            result = sorted(list1)
            print("\nСортировка по возрастанию: ", result)
        case "2":
            result = sorted(list1, reverse = True)
            print("\nСортировка по убыванию: ", result)
        case "3":
            minimum = min(list1)
            maximum = max(list1)
            print("\nМинимальное число:", minimum)
            print("Максимальное число:", maximum)
        case "4":
            result = []
            for i in list1:
                if 0 <= i <= 1114111:
                    symbol = chr(i)
                    result.append(symbol)
                else:
                    print(f"\nЧисло {i} не может быть преобразованно в символ")
            print("\nСимволы ASCII:", result)
        case "5":
            print("\nКонец программы")
            break
        case _:
            print("\nОшибка")
