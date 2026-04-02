class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    def calculate_bonus(self):
        return self.salary * 0.1

    def raise_salary(self, percentage):
        if percentage > 0:
            self.salary *= (1 + percentage / 100)
            return True
        return False

    def __str__(self):
        return f"{self.name} (ID: {self.emp_id}), {self.department}, ЗП: {self.salary:.2f}"

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department, team_size):
        super().__init__(name, emp_id, salary, department)
        self.team_size = team_size

    def calculate_bonus(self):
        return self.salary * 0.15 + self.team_size * 100

    def __str__(self):
        return f"Менеджер: {self.name} (ID: {self.emp_id}), {self.department}, Команда: {self.team_size}, ЗП: {self.salary:.2f}"

class Developer(Employee):
    def __init__(self, name, emp_id, salary, department, programming_language):
        super().__init__(name, emp_id, salary, department)
        self.programming_language = programming_language

    def calculate_bonus(self):
        return self.salary * 0.12

    def __str__(self):
        return f"Разработчик: {self.name} (ID: {self.emp_id}), {self.department}, Язык: {self.programming_language}, ЗП: {self.salary:.2f}"

class Intern(Employee):
    def __init__(self, name, emp_id, salary, department, internship_duration):
        super().__init__(name, emp_id, salary, department)
        self.internship_duration = internship_duration

    def calculate_bonus(self):
        return 500

    def __str__(self):
        return f"Стажер: {self.name} (ID: {self.emp_id}), {self.department}, Стажировка: {self.internship_duration} мес., ЗП: {self.salary:.2f}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен в отдел {self.name}")

    def remove_employee(self):
        if not self.employees:
            print("В этом отделе нет сотрудников")
            return
        print("\nСотрудники данного отдела:")
        for i, emp in enumerate(self.employees, 1):
            print(f"{i}. {emp}")
        try:
            choice = int(input("Выберите номер сотрудника для кика: "))
            if 1 <= choice <= len(self.employees):
                employee = self.employees.pop(choice - 1)
                print(f"Сотрудник {employee.name} удален из отдела {self.name}")
            else:
                print("Ошибка!!!!!!!!!!! неверный номер сотрудника")
        except ValueError:
            print("Ошибка!!!!!!!!!!!!! введите число")

    def show_employees(self):
        if not self.employees:
            print(f"В отделе {self.name} нет сотрудников")
            return
        print(f"\nСОТРУДНИКИ ОТДЕЛА {self.name.upper()}")
        for i, employee in enumerate(self.employees, 1):
            print(f"{i}. {employee}")

    def calculate_all_bonuses(self):
        if not self.employees:
            print("В данном отделе нет сотрудников")
            return
        print(f"\nБОНУСЫ ОТДЕЛА {self.name.upper()}")
        total_bonus = 0
        for employee in self.employees:
            bonus = employee.calculate_bonus()
            total_bonus += bonus
            print(f"{employee.name}: {bonus:.2f}")
        print(f"Общая сумма бонусов: {total_bonus:.2f}")


def create_employee():
    print("\nДОБАВЛЕНИЕ НОВОГО СОТРУДНИКА")
    print("Выберите тип сотрудника:")
    print("1 - Менеджер")
    print("2 - Разработчик")
    print("3 - Стажер")

    type_choice = input("Ваш выбор (1-3): ").strip()

    name = input("Введите имя вашего сотрудника: ").strip()
    if not name:
        name = "кто-то"

    emp_id = input("Введите ID вашего сотрудника: ").strip()
    if not emp_id:
        emp_id = "000"

    department = input("Введите отдел: ").strip()
    if not department:
        department = "общий"

    try:
        salary = float(input("Введите зарплату: "))
        if salary < 0:
            print("Зарплата не может быть отрицательной, установлена 0")
            salary = 0
    except ValueError:
        print("Ошибка ввода зарплаты, установлена 0")
        salary = 0

    match type_choice:
        case "1":
            try:
                team_size = int(input("Введите размер команды: "))
                if team_size < 0:
                    team_size = 0
            except ValueError:
                print("Ошибка ввода, установлен размер команды 0")
                team_size = 0
            return Manager(name, emp_id, salary, department, team_size)
        case "2":
            programming_language = input("Введите язык программирования: ").strip()
            if not programming_language:
                programming_language = "Python"
            return Developer(name, emp_id, salary, department, programming_language)
        case "3":
            try:
                internship_duration = int(input("Введите длительность стажировки (мес.): "))
                if internship_duration < 0:
                    internship_duration = 0
            except ValueError:
                print("Ошибка ввода, установлена стажировка 0 месяцев")
                internship_duration = 0
            return Intern(name, emp_id, salary, department, internship_duration)
        case _:
            print("Неверный выбор, создан сотрудник по умолчанию")
            return Employee(name, emp_id, salary, department)


def raise_employee_salary(department):
    if not department.employees:
        print("В отделе нет сотрудников")
        return

    print("\nПОВЫШЕНИЕ ЗАРПЛАТЫ")
    department.show_employees()

    try:
        emp_choice = int(input("Выберите номер сотрудника: "))
        if 1 <= emp_choice <= len(department.employees):
            try:
                percentage = float(input("Введите процент повышения: "))
                employee = department.employees[emp_choice - 1]
                if employee.raise_salary(percentage):
                    print(f"Зарплата {employee.name} повышена на {percentage}%")
                    print(f"Новая зарплата: {employee.salary:.2f}")
                else:
                    print("Ошибка: процент должен быть положительным")
            except ValueError:
                print("Ошибка: введите число для процента")
        else:
            print("Ошибка: неверный номер сотрудника")
    except ValueError:
        print("Ошибка: введите число")


def main():
    print("СИСТЕМА УПРАВЛЕНИЯ СОТРУДНИКАМИ")
    dept_name = input("Введите название отдела: ").strip()
    if not dept_name:
        dept_name = "Основной отдел"
        print(f"Название отдела не введено, установлено: '{dept_name}'")
    department = Department(dept_name)

    while True:
        print("ГЛАВНОЕ МЕНЮ:")
        print("1 - Добавить сотрудника")
        print("2 - Удалить сотрудника")
        print("3 - Показать всех сотрудников")
        print("4 - Рассчитать бонусы")
        print("5 - Повысить зарплату")
        print("0 - Выйти из программы")

        choice = input("Выберите действие (0-5): ").strip()

        match choice:
            case "1":
                employee = create_employee()
                department.add_employee(employee)
            case "2":
                department.remove_employee()
            case "3":
                department.show_employees()
            case "4":
                department.calculate_all_bonuses()
            case "5":
                raise_employee_salary(department)
            case "0":
                print("ИТОГОВАЯ ИНФОРМАЦИЯ:")
                department.show_employees()
                if department.employees:
                    department.calculate_all_bonuses()
                print("\nдьес амигос аривидерчи")
                break
            case _:
                print("Ошибка: выберите действие от 0 до 5")


if __name__ == "__main__":
    main()
