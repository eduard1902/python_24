# Декораторы в Python

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            for i in range(2, result):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@ is_prime
def sum_three(*number):
    return sum(number)


result = sum_three(2, 3, 6)
print(result)
"""
Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное"
 в противном случае.

"""

