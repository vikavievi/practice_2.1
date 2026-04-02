students = [
    "Иванов Иван:5,4,3,5",
    "Петров Петр:4,3,4,4",
    "Сидорова Мария:5,5,5,5"
]

with open("students.txt", "w", encoding="utf-8") as f:
    for student in students:
        f.write(student + "\n")

names = []
averages = []

with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        parts = line.split(":")
        name = parts[0]
        grades_str = parts[1]

        grades_list = grades_str.split(",")

        summa = 0
        count = 0

        for grade in grades_list:
            summa = summa + int(grade)
            count = count + 1

        average = summa / count

        names.append(name)
        averages.append(average)

best_index = 0
best_average = averages[0]

i = 1
while i < len(averages):
    if averages[i] > best_average:
        best_average = averages[i]
        best_index = i
    i = i + 1

print("Студент с наивысшим средним баллом:")
print(names[best_index], "(", best_average, ")")

with open("result.txt", "w", encoding="utf-8") as f:
    i = 0
    while i < len(names):
        if averages[i] > 4.0:
            f.write(names[i] + ": " + str(averages[i]) + "\n")
        i = i + 1

print("Результат сохранён в result.txt")