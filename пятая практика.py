text = input("Введите текст: ").split()
counts = {}
for i in text:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
result1 = ""
chasto = 0
for i, j in counts.items():
    if j > chasto:
        chasto = j
        result1 = i
long = 0
result2 = ""
for i in counts:
    if len(i) > long:
        long = len(i)
        result2 = i
print(f"1) {result1} 2) {result2}")
