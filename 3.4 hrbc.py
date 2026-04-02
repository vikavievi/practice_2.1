def check_anagram():
    a, b = input("Введите строки через пробел: ").split()

    a = a.lower().replace(" ", "")
    b = b.lower().replace(" ", "")

    Z = sorted(a) == sorted(b)
    print(f"Результат: {Z}")
check_anagram()


