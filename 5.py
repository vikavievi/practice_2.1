a = input('Введите строку: ')
a1 = list(a)
final = []
i = 0
x = 0
final.append([])
while i < len(a1):
    final.append([a1[i]])
    i += 1
while x < len(a1):
    j = x + 1
    while j < len(a1):
        final.append([a1[x], a1[j]])
        j += 1
    x += 1
final.append(a1)
print(final)
