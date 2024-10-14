# Задача "Изменять нельзя получать":
"""
Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт, а Sedan(седан) - наследник класса Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:
1. Атрибут owner(str) - владелец транспорта. (владелец может меняться)
2. Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
3. Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
4. Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)


А так же атрибут класса:
1. Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)

Каждый объект Vehicle должен содержать следующий методы:
1. Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
2. Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
3. Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
4. Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
а так же владельца в конце в формате "Владелец: <имя>"
5. Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в
списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".

"""

class Vehicle:
    # __COLOR_VARIANTS = []
    __COLOR_VARIANTS = ['red', 'yellow', 'black', 'gray', 'white', 'orange']
    # self.red = red
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    # название модели транспорта
    def get_model(self):
        print(f'Модель: {self.__model}')
    # мощность двигателя
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        Vehicle.get_model(self)
        Vehicle.get_horsepower(self)
        Vehicle.get_color(self)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя поменять цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Исходный код:

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()