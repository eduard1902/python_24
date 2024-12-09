# Задание "Они все так похожи":

import math
class Figure:

    sides_count = 0
    def __init__(self,sides, *color):
        self.set_color(*color)
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.filled = False

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))
    def get_color(self):
        return self.__color
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *__sides: int):
        return all(isinstance(side, int) and side > 0 for side in __sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__((radius,), *color)
        self.__radius = self.get_sides()[0] / (2 * math.pi) if self.get_sides()[0] > 0 else 0

    def get_square(self):
        return math.pi * self.__radius ** 2

class Triangle(Figure):

    sides_count = 3

    def __init__(self, *sides, color):
        super().__init__(sides, *color)
        a, b, c = self.get_sides()
        p = (a + b + c)/2
        self.height = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / a if a > 0 else 0

    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.height

class Cube(Figure):

    sides_count = 12

    def __init__(self, color, side):
        super().__init__([side] * 12, *color)
        self.__sides = [side] * self.sides_count

    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

"""
Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
- Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)

Методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны
целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
 то не изменять, в противном случае - менять.

 Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
- Все атрибуты и методы класса Figure
- Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
- Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
"""