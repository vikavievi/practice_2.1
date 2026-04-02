a = int(input('Введите число больше 10: '))
if a < 10:
    print('Введенное число меньше 10')
else:
    a = str(a)
    for s in a:
        print(s, end=' ')
