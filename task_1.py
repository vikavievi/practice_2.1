with open('resource/text.txt', 'w', encoding='utf-8') as file:
    file.write("Привет, я Вика\n")
    file.write("Мне 17 лет\n")
    file.write("Я учусь в ТТИТ\n")
    file.write("Я Мастер спорта России по художественной гимнастике\n")
    file.write("Работаю тренером\n")

with open('resource/text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

line_count = len(lines)
print(f"Количество строк в файле: {line_count}")

word_count = 0
for line in lines:
    words = line.split()
    word_count += len(words)
print(f"Количество слов в файле: {word_count}")

longest_line = ""
for line in lines:
    line_without_newline = line.strip('\n')
    if len(line_without_newline) > len(longest_line):
        longest_line = line_without_newline

print (f"Самая длинная строка: {longest_line}")
print(f"Длина самой длинной строки: {len(longest_line)} символов")