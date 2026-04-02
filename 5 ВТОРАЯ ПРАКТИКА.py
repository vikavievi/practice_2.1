N = input("Введите количество лекций: ")
if not N.isdigit():
    print("Ошибка")
    exit()
n = int(N)

full_students = set()
for i in range(n):
    m = int(input(f"Введите количество студентов на лекции {i+1}: "))
    print("Введите фамилии студентов: ")
    students = set()
    for j in range(m):
        name = input().strip()
        students.add(name)
    if i == 0:
        full_students = students
    else:
        full_students = full_students & students
result = sorted(full_students)
print("Примерные студенты:")
for i in result:
    print(i)
