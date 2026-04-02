N = input("Введите количество строк: ")
if not N.isdigit():
    print("Ошибка")
    exit()
n = int(N)
words = []

print("Введите строки:")
for i in range(n):
    word = input()
    words.append(word)

def gemetry(word):
    total = 0
    for char in word.upper():
        total += ord(char)
    return total

words.sort(key=gemetry)

print("Отсортированные строки:")
for word in words:
    print(word)
