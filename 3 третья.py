from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def scale(self, factor):
        if factor <= 0:
            print("Ошибка: коэффициент масштабирования должен быть положительным")
            return
        self._scale_impl(factor)
        print(f"Фигура масштабирована в {factor} раз")

    @abstractmethod
    def _scale_impl(self, factor):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            print("Ошибка: ширина и высота должны быть положительными")
            self.width = 1
            self.height = 1
        else:
            self.width = width
            self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def _scale_impl(self, factor):
        self.width *= factor
        self.height *= factor

    def __str__(self):
        return f"Прямоугольник: {self.width} x {self.height}"


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            print("Ошибка: радиус должен быть положительным")
            self.radius = 1
        else:
            self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def _scale_impl(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"Круг: радиус = {self.radius}"


class Triangle(Shape):
    def __init__(self, a, b, c):
        sides = [a, b, c]
        sides.sort()
        if sides[0] + sides[1] > sides[2] and all(s > 0 for s in sides):
            self.a = a
            self.b = b
            self.c = c
        else:
            print("Ошибка: стороны не удовлетворяют неравенству треугольника")
            self.a = 3
            self.b = 4
            self.c = 5

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def _scale_impl(self, factor):
        self.a *= factor
        self.b *= factor
        self.c *= factor

    def __str__(self):
        return f"Треугольник: стороны {self.a}, {self.b}, {self.c}"


def create_rectangle():
    print("\nСОЗДАНИЕ ПРЯМОУГОЛЬНИКА")
    try:
        width = float(input("Введите ширину: "))
        height = float(input("Введите высоту: "))
        return Rectangle(width, height)
    except ValueError:
        print("Ошибка: введите числа")
        return Rectangle(1, 1)


def create_circle():
    print("\nСОЗДАНИЕ КРУГА")
    try:
        radius = float(input("Введите радиус: "))
        return Circle(radius)
    except ValueError:
        print("Ошибка: введите число")
        return Circle(1)


def create_triangle():
    print("\nСОЗДАНИЕ ТРЕУГОЛЬНИКА")
    try:
        a = float(input("Введите первую сторону: "))
        b = float(input("Введите вторую сторону: "))
        c = float(input("Введите третью сторону: "))
        return Triangle(a, b, c)
    except ValueError:
        print("Ошибка: введите числа")
        return Triangle(3, 4, 5)


def main():
    print("СИСТЕМА ГЕОМЕТРИЧЕСКИХ ФИГУР")
    shapes = []

    while True:
        print("\nВыберите действие:")
        print("1 - Создать прямоугольник")
        print("2 - Создать круг")
        print("3 - Создать треугольник")
        print("4 - Показать все фигуры")
        print("5 - Масштабировать фигуру")
        print("0 - Выход")

        choice = input("Ваш выбор: ").strip()

        match choice:
            case "1":
                shape = create_rectangle()  # Функция для создания прямоугольника
                shapes.append(shape)
                print(f"Создан: {shape}")
                print(f"Площадь(S): {shape.area():.2f}")
                print(f"Периметр(P): {shape.perimeter():.2f}")

            case "2":
                shape = create_circle()  # Функция для создания круга
                shapes.append(shape)
                print(f"Создан: {shape}")
                print(f"Площадь(S): {shape.area():.2f}")
                print(f"Периметр(P): {shape.perimeter():.2f}")

            case "3":
                shape = create_triangle()  # Функция для создания треугольника
                shapes.append(shape)
                print(f"Создан: {shape}")
                print(f"Площадь(S): {shape.area():.2f}")
                print(f"Периметр(P): {shape.perimeter():.2f}")

            case "4":
                if shapes:
                    print("\nВСЕ ФИГУРЫ")
                    for i, shape in enumerate(shapes, 1):
                        print(f"{i}. {shape}")
                        print(f"Площадь(S): {shape.area():.2f}")
                        print(f"Периметр(P): {shape.perimeter():.2f}")
                else:
                    print("Нет созданных фигур")

            case "5":
                if shapes:
                    print("\nДоступные фигуры:")
                    for i, shape in enumerate(shapes, 1):
                        print(f"{i}. {shape}")

                    try:
                        shape_num = int(input("Выберите номер фигуры: "))
                        if 1 <= shape_num <= len(shapes):
                            try:
                                factor = float(input("Введите нужный коэффициент для масштабирования: "))
                                shapes[shape_num - 1].scale(factor)  # Масштабируем фигуру
                                print(f"Обновленная фигура: {shapes[shape_num - 1]}")
                                print(f"Новая площадь: {shapes[shape_num - 1].area():.2f}")
                                print(f"Новый периметр: {shapes[shape_num - 1].perimeter():.2f}")
                            except ValueError:
                                print("Ошибка: введите число для коэффициента")
                        else:
                            print("Ошибка: неверный номер фигуры")
                    except ValueError:
                        print("Ошибка: введите число")
                else:
                    print("Нет фигур для масштабирования")

            case "0":
                print("\nИТОГОВАЯ ИНФОРМАЦИЯ")
                if shapes:
                    print("Ваши созданные фигуры:")
                    for i, shape in enumerate(shapes, 1):
                        print(f"{i}. {shape}")
                        print(f"Площадь: {shape.area():.2f}")
                        print(f"Периметр: {shape.perimeter():.2f}")
                else:
                    print("Не было создано ни одной фигуры")
                print("Выход из системы. Аривидерчи!")
                break

            case _:
                print("Ошибка: выберите операцию от 0 до 5")


if __name__ == "__main__":
    main()
