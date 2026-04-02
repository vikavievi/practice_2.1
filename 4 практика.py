list1 = input("Введите первый список через пробел:").split()
list2 = input("Введите второй список через пробел:").split()

print("Элементы первого списка, которых нет во втором:")
for i in list1:
    if i not in list2:
        print(i)
