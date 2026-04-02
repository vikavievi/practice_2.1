class BankAccount:
    def __init__(self, owner, balance=0, account_number=""):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Пополнение: +{amount}")
            print(f"Успешно пополнено: {amount}")
        else:
            print("Ошибка: сумма должна быть положительной")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.history.append(f"Снятие: -{amount}")
                print(f"Успешно снято: {amount}")
            else:
                print("Ошибка: недостаточно средств")
        else:
            print("Ошибка: сумма должна быть положительной")

    def get_balance(self):
        return self.balance

    def show_history(self):
        if self.history:
            print("История операций:")
            for operation in self.history:
                print(f"  - {operation}")
        else:
            print("История операций пуста")

    def __str__(self):
        return f"Счет {self.account_number}: {self.owner}, Баланс: {self.balance}"

def create_account():
    print("\nСОЗДАНИЕ БАНКОВСКОГО СЧЕТА")
    owner = input("Введите имя владельца счета: ").strip()
    if not owner:
        owner = "Неизвестный"
        print("Имя не введено, установлено: 'Неизвестный'")

    while True:
        try:
            balance = float(input("Введите начальный баланс: "))
            if balance >= 0:
                break
            else:
                print("Ошибка: баланс не может быть отрицательным")
        except ValueError:
            print("Ошибка: введите число")

    account_number = "00001"
    return BankAccount(owner, balance, account_number)

def main():
    print("БАНКОВСКАЯ СИСТЕМА")
    account = create_account()
    print(f"\nСЧЕТ СОЗДАН")
    print(account)
    print()

    while True:
        print("\nВыберите операцию:")
        print("1 - Пополнение счета")
        print("2 - Снятие денег")
        print("3 - Показать баланс")
        print("4 - История операций")
        print("5 - Информация о счете")
        print("0 - Выход")

        choice = input("Ваш выбор: ").strip()

        match choice:
            case "1":
                try:
                    amount = float(input("Сумма для пополнения: "))
                    account.deposit(amount)
                except ValueError:
                    print("Ошибка: введите число")

            case "2":
                try:
                    amount = float(input("Сумма для снятия: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Ошибка: введите число")

            case "3":
                balance = account.get_balance()
                print(f"Текущий баланс: {balance}")

            case "4":
                account.show_history()

            case "5":
                print("\nИНФОРМАЦИЯ О СЧЕТЕ")
                print(account)

            case "0":
                print("\nИТОГОВАЯ ИНФОРМАЦИЯ")
                print(account)
                account.show_history()
                print("Выход из системы. До свидания!")
                break

            case _:
                print("Ошибка: выберите операцию от 0 до 5")

if __name__ == "__main__":
    main()