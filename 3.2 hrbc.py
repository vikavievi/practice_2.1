def letters():
    text = input("Введите строку: ")
    a = "аеёиоуыэюяaeiou"
    b = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    a_count = 0
    b_count = 0

    for char in text.lower():
        if char in a:
            a_count += 1
        elif char in b:
            b_count += 1
    print(f"Гласных: {a_count} || Согласных: {b_count}")
letters()
