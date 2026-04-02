import datetime
import os

LOG_FILE = "calculator.log"

def show_last_operations():
    if not os.path.exists(LOG_FILE):
        print("Лог-файл отсутствует.")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        print("Лог пуст.")
        return

    last_lines = lines[-5:]
    print("\n--- Последние 5 операций ---")
    for line in last_lines:
        print(line.strip())
    print("----------------------------")

def clear_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            pass
        print("Лог очищен.")
    else:
        print("Лог-файл не существует, нечего очищать.")

def log_operation(a, op, b, result):
    #здесь мы записываем дату, время и тд
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {a} {op} {b} = {result}\n")

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b
    else:
        return "Неизвестная операция"

def main():
    print("Калькулятор с логированием")
    show_last_operations()

    while True:
        print("\nМЕНЮ:")
        print("1. Выполнить операцию")
        print("2. Очистить лог")
        print("3. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                op = input("Введите операцию (+, -, *, /): ").strip()
            except ValueError:
                print("Ошибка: введены некорректные числа.")
                continue

            result = calculate(a, b, op)
            print(f"Результат: {result}")

            if isinstance(result, (int, float)):
                log_operation(a, op, b, result)
            else:
                print("Операция не записана в лог из-за ошибки.")

        elif choice == "2":
            clear_log()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()