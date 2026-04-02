def RLE():
    text = input("Введите строку: ")
    result = ""
    i = 0

    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        if count > 1:
            result += text[i] + str(count)
        else:
            result += text[i]
        i += 1

    print(f"Результат: {result}")
RLE()
