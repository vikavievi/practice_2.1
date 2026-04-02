s = input('Введите строку: ')
itog = []
for i in s:
    if s.count(i) > 1:
        itog.append('!')
    else:
        itog.append(i)
print(''.join(itog))
