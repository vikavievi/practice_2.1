class Flyable:
    def fly(self):
        print(f"{self.name} летит")

    def land(self):
        print(f"{self.name} приземлился")


class Swimmable:
    def swim(self):
        print(f"{self.name} плывет")

    def dive(self):
        print(f"{self.name} ныряет")


class Walkable:
    def walk(self):
        print(f"{self.name} идет")

    def run(self):
        print(f"{self.name} бежит")


class Animal:
    def init(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звук")


class Duck(Animal, Flyable, Swimmable, Walkable):
    def make_sound(self):
        print(f"{self.name} издает звук кряканья")


class Penguin(Animal, Swimmable, Walkable):
    def make_sound(self):
        print(f"{self.name} издает звук трещетки")


class Eagle(Animal, Flyable, Walkable):
    def make_sound(self):
        print(f"{self.name} издает клекот")


class Dolphin(Animal, Swimmable):
    def make_sound(self):
        print(f"{self.name} издает щелчки, скрипы и свист")


class Zoo:
    def init(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def remove_animal(self):
        if not self.animals:
            print("В зоопарке нет животных")
            return
        print("\nУДАЛЕНИЕ ЖИВОТНОГО")
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal.name} ({animal.species})")

        try:
            choice = int(input("Выберите номер животного для удаления: "))
            if 1 <= choice <= len(self.animals):
                animal = self.animals.pop(choice - 1)
                print(f"Животное {animal.name} удалено из зоопарка")
            else:
                print("Ошибка: неверный номер животного")
        except ValueError:
            print("Ошибка: введите число")

    def show_animals(self):
        if not self.animals:
            print("В зоопарке пока нет животных")
            return
        print("\nВСЕ ЖИВОТНЫЕ В ЗООПАРКЕ")
        for i, animal in enumerate(self.animals, 1):
            abilities = []
            if isinstance(animal, Flyable):
                abilities.append("летает")
            if isinstance(animal, Swimmable):
                abilities.append("плавает")
            if isinstance(animal, Walkable):
                abilities.append("ходит")

            abilities_str = ", ".join(abilities)
            print(f"{i}. {animal.name} - {animal.species}, {animal.age} лет ({abilities_str})")

    def make_all_sounds(self):
        if not self.animals:
            print("В зоопарке нет животных")
            return

        print("\nЗВУКИ ЖИВОТНЫХ")
        for animal in self.animals:
            print(f"{animal.name}: ", end="")
            animal.make_sound()

    def feed_animal(self):
        if not self.animals:
            print("В зоопарке нет животных")
            return

        print("\nКОРМЛЕНИЕ ЖИВОТНЫХ")
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal.name} ({animal.species})")

        try:
            choice = int(input("Выберите номер животного для кормления: "))
            if 1 <= choice <= len(self.animals):
                animal = self.animals[choice - 1]
                food = input(f"Введите еду для {animal.name}: ").strip()
                if not food:
                    food = "корм"
                print(f"Покормили {animal.name}: {food}")
            else:
                print("Ошибка: неверный номер животного")
        except ValueError:
            print("Ошибка: введите число")

    def demo_abilities(self):
        if not self.animals:
            print("В зоопарке нет животных")
            return print("\nДЕМОНСТРАЦИЯ СПОСОБНОСТЕЙ")
        for i, animal in enumerate(self.animals, 1):
            print(f"{i}. {animal.name} ({animal.species})")
        try:
            choice = int(input("Выберите номер животного для демонстрации: "))
        if 1 <= choice <= len(self.animals):
            animal = self.animals[choice - 1]
            print(f"\nДемонстрация {animal.name}")

            if isinstance(animal, Flyable):
                animal.fly()
                animal.land()

            if isinstance(animal, Swimmable):
                animal.swim()
                animal.dive()

            if isinstance(animal, Walkable):
                animal.walk()
                animal.run()

            print("Звук: ", end="")
            animal.make_sound()
            print("Демонстрация завершена")
        else:
            print("Ошибка: неверный номер животного")
        except ValueError:
        print("Ошибка: введите число")

    def create_animal():
        print("\nДОБАВЛЕНИЕ НОВОГО ЖИВОТНОГО")
        print("Выберите тип животного:")
        print("1 - Утка (летает, плавает, ходит)")
        print("2 - Пингвин (плавает, ходит)")
        print("3 - Орел (летает, ходит)")
        print("4 - Дельфин (плавает)")

        type_choice = input("Ваш выбор (1-4): ").strip()
        name = input("Введите имя животного: ").strip()
        if not name:
            name = "Безымянный"

        try:
            age = int(input("Введите возраст животного: "))
            if age < 0:
                print("Возраст не может быть отрицательным, установлен 0")
                age = 0
        except ValueError:
            print("Ошибка ввода возраста, установлен 1 год")
            age = 1

        match type_choice:
            case "1":
                return Duck(name, "Утка", age)
            case "2":
                return Penguin(name, "Пингвин", age)
            case "3":
                return Eagle(name, "Орел", age)
            case "4":
                return Dolphin(name, "Дельфин", age)
            case _:
                print("Неверный выбор, создана утка по умолчанию")
                return Duck(name, "Утка", age)

    def main():
        print("СИСТЕМА УПРАВЛЕНИЯ ЗООПАРКОМ")
        zoo = Zoo()

        while True:
            print("\n" + "=" * 50)
            print("ГЛАВНОЕ МЕНЮ:")
            print("1 - Добавить животное")
            print("2 - Удалить животное")
            print("3 - Показать всех животных")
            print("4 - Послушать звуки животных")
            print("5 - Покормить животное")
            print("6 - Демонстрация способностей")
            print("0 - Выйти из программы")
            print("=" * 50)
            choice = input("Выберите действие (0-6): ").strip()

            match choice:
                case "1":
                    animal = create_animal()
                    zoo.add_animal(animal)
                case "2":
                    zoo.remove_animal()
                case "3":
                    zoo.show_animals()
                case "4":
                    zoo.make_all_sounds()
                case "5":
                    zoo.feed_animal()
                case "6":
                    zoo.demo_abilities()
                case "0":
                    print("\n" + "=" * 50)
                    print("ИТОГОВАЯ ИНФОРМАЦИЯ:")
                    zoo.show_animals()
                    print("\nСпасибо за использование системы! До свидания!")
                    print("=" * 50)
                    break
                case _:
                    print("Ошибка: выберите действие от 0 до 6")

    # Исправленная строка запуска
if __name__ == "__main__":
    main()
