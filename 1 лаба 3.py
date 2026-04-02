string = input('Введите строку: ')
result = []
for i in string:
    if string.count(i) > 1:
        result.append('!')
else:
    result.append(i)
    print(''.join(result))