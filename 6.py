def shifr():
    for i in stroka:
        if ord(i) - step < 96:
            print(chr(ord(i) + step - 26), end = '')
        else:
            print(chr(ord(i) + step), end = '')

def deshifr():
    for i in stroka:
        if ord(i) - step < 97:
            print(chr(ord(i) - step + 26), end = '')
        else:
            print(chr(ord(i) - step), end = '')

print('\nШИФР ЦЕЗАРЯ(не салат)')
print('\n1)Зашифровать сообщение')
print('2)Дешифровать сообщение')
a = input('\nВыберите нужное действие: ')
stroka = input('\nВведите ваш текст: ')
step = int(input('\nУкажите шаг для шифровки/дешивровки: '))
match a:
    case '1':
        shifr()
    case '2':
        deshifr()
    case _:
        print('Ошибка')
