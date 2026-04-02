def per():
    a = input("Введите предложение: ")

    words = a.split()
    gan = words[::-1]
    result = " ".join(gan)
    result = result.capitalize()

    print(f"Результат: {result}")
per()

