

print('Введите ваш список чисел через пробел:')
num = input()
list1 = list(map(int, num.split()))

while True:
    print("Выберите действие:")
    print("1.Сортировка по возрастанию")
    print("2.Сортировка по убыванию")
    print("3.Нахождение максимального и минимального числа")
    print("4.Приведения чисел к ASCII таблице, и вывод получившихся символов.")
    print("5. Выход")
    a = input("Выберите номер действия:")

    match a:
        case "1":
            rezult = sorted(list1)
            print("Сортировка по возрастанию:", rezult)
        case "2":
            rezult = sorted(list1, reverse=True)
            print("Сортировка по убыванию:", rezult)
        case "3":
            minim = min(list1)
            maxim = max(list1)
            print("\nМинимальное число:", minim)
            print("\nМаксимальное число:", maxim)
        case "4":
            rezult = []
            for i in list1:
                if 0 <= i <= 1114111:
                    symbol = chr(i)
                    result.append(symbol)
                else:
                    print(f"Число {i} не может быть преобразованно в символ")
                print("\nСимволы ASCII: result")
        case "5":
            print("Конец программы")
            break
        case _:
            print("\nОшибка")



