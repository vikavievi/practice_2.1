text = list(input("Введите строку: "))
N = input("Введите N: ")
if not N.isdigit():
    print("Ошибка")
    exit()
n = int(N)

chars = list(text)
razmer = len(chars) // n
result = []

for i in range(n):
    start = i * razmer
    end = start + razmer
    result.append(chars[start:end])

print("\nРезультат:", result)
