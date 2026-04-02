text = input("Введите символы через пробел: ")
chars = text.split()
result = []
group = [chars[0]]

for i in chars[1:]:
    if i == group[-1]:
        group.append(i)
    else:
        result.append(group)
        group = [i]
result.append(group)

print("Результат:", result)

