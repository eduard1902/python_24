# Задача "За честь и отвагу!":
from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power):
        self.knight_name = name
        self.power = power
        super().__init__()

    def run(self):
         print(f'{self.knight_name}, на нас напали!')
         enemies = 100
         days = 1
         while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.power
            if enemies > 0:
                print(f'{self.knight_name} сражается {days} день(дня)..., осталось {enemies} воинов.')
            else:
                print(f'{self.knight_name} одержал победу спустя {days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
time.sleep(1)
second_knight.start()
second_knight.join()
first_knight.join()

print('Все битвы окончились!')



""""
Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
    1. Атрибут name - имя рыцаря. (str)
    2. Атрибут power - сила рыцаря. (int)
А также метод run, в котором рыцарь будет сражаться с врагами:
    1. При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
    2. Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
    3. В процессе сражения количество врагов уменьшается на power текущего рыцаря.
    4. По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., 
    осталось <кол-во воинов> воинов."
    5. После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
Пункты задачи:
    1. Создайте класс Knight с соответствующими описанию свойствами.
    2. Создайте и запустите 2 потока на основе класса Knight.
Выведите на экран строку об окончании битв.

"""