class BankAccount:
    def __init__(self, owner_name, initial_balance=0, account_id=""):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_id = account_id
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Пополнение счета: +{amount}")
            print(f"Счет успешно пополнен: {amount}")
        else:
            print("Ошибка! Сумма должна быть положительной")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Снятие мани: -{amount}")
                print(f"Успешно снято(мани больше нет): {amount}")
            else:
                print("Ошибка! Недостаточно средств")
        else:
            print("Ошибка! Сумма должна быть положительной")

    def transfer(self, other_account, amount):
        if isinstance(other_account, BankAccount):
            if amount > 0:
                if amount <= self.balance:
                    self.withdraw(amount)
                    other_account.deposit(amount)
                    self.transaction_history.append(f"Перевод на счет {other_account.account_id}: -{amount}")
                    other_account.transaction_history.append(f"Перевод от счета {self.account_id}: +{amount}")
                    print(f"Успешно переведено: {amount} на счет {other_account.account_id}")
                else:
                    print("Ошибка! Недостаточно средств для перевода")
            else:
                print("Ошибка! Сумма должна быть положительной")
        else:
            print("Ошибка! Переданный объект не является банковским счетом")

    def get_balance(self):
        return self.balance

    def show_history(self):
        if self.transaction_history:
            print("История операций по счету:")
            for operation in self.transaction_history:
                print(f"  - {operation}")
        else:
            print("История операций пуста :/ ")

    def __str__(self):
        return f"Счет {self.account_id}: {self.owner_name}, Баланс: {self.balance}"


def create_account():
    print("\nСОЗДАНИЕ БАНКОВСКОГО СЧЕТА")
    owner_name = input("Введите имя владельца счета: ").strip()
    if not owner_name:
        owner_name = "Неизвестный"
        print("Имя не введено, установлено: 'Неизвестный'")

    while True:
        try:
            initial_balance = float(input("Введите начальный баланс: "))
            if initial_balance >= 0:
                break
            else:
                print("Ошибка: баланс не может быть отрицательным")
        except ValueError:
            print("Ошибка: введите число")

    account_id = input("Введите номер счета: ") or "00001"
    return BankAccount(owner_name, initial_balance, account_id)


def main():
    print("БАНКОВСКАЯ СИСТЕМА")
    account = create_account()
    print(f"\nСЧЕТ СОЗДАН")
    print(account)

    accounts = [account]

    while True:
        print("\nВыберите операцию:")
        print("1 - Пополнение счета")
        print("2 - Снятие денег")
        print("3 - Перевод денег на другой счет")
        print("4 - Показать баланс")
        print("5 - История операций")
        print("6 - Информация о счете")
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
                try:
                    transfer_account_id = input("Введите номер счета для перевода: ")
                    other_account = None
                    for acc in accounts:
                        if acc.account_id == transfer_account_id:
                            other_account = acc
                            break
                    if other_account:
                        amount = float(input("Сумма для перевода: "))
                        account.transfer(other_account, amount)
                    else:
                        print("Ошибка: счет не найден")
                except ValueError:
                    print("Ошибка: введите число")

            case "4":
                balance = account.get_balance()
                print(f"Текущий баланс: {balance}")

            case "5":
                account.show_history()

            case "6":
                print("\nИНФОРМАЦИЯ О СЧЕТЕ")
                print(account)

            case "0":
                print("\nИТОГОВАЯ ИНФОРМАЦИЯ")
                print(account)
                account.show_history()
                print("Выход из системы. До свидания!")
                break

            case _:
                print("Ошибка: выберите операцию от 0 до 6")


if __name__ == "__main__":
    main()
