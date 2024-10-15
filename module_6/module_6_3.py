# Задача "Мифическое наследование":

"""
Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
1. x_distance = 0 - пройденный путь.
2. sound = 'Frrr' - звук, который издаёт лошадь.
И методами:
3. run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
1. y_distance = 0 - высота полёта
2. sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
И методами:
3. fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
1. move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
2. get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
3. voice - который печатает значение унаследованного атрибута sound.

Пункты задачи:
1. Создайте классы родители: Horse и Eagle с методами из описания.
2. Создайте класс наследник Pegasus с методами из описания.
3. Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

"""

class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)


    def voice(self):
        print(self.sound)



# Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
