second = input("Введите количество секунд: ")
if not second.isdigit():
    print('Ошибка')
    exit()
sec = int(second)

day = sec // 86400
ostalos = sec % 86400

hours = ostalos // 3600
ostalos = ostalos % 3600

minutes = ostalos // 60
seconds = ostalos % 60

print(day, ":", hours, ":", minutes, ":", seconds)
