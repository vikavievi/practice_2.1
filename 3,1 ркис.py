def slovo():
    a = input("Введите предложение: ")
    words = a.split()
    long = max(words, key=len)
    print(f"Самое длинное слово: {long}")
slovo()
