# Задача "Все ли равны?":

first = int(input('Введите число')) # ввести произвольное число
second = int(input('Введите число')) # ввести произвольное число
third = int(input('Введите число')) # ввести произвольное число


if first == second and first == third: # first == second == third:
    print(3)
elif first == second or second == third or first == third: # если хоть одно совпадение, то вывод 2
    print(2)
else:
    print(0) # совпадений нет


