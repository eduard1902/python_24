# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

# Задача "Всё не так уж просто":

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки
primes = []
not_primes= []

for i in numbers:
    # Пропускаем число 1, так как оно не является ни простым, ни составным
    if i == 1:
        continue
    # Находим все простые числа и предполагаем
    is_prime = True

    # Числа меньше 2 не являются простыми
    if i < 2:
        is_prime = False
    else:
        # Проверяем все числа от 2
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

    # Записываем числа в соответствующие списки
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print("Исходный код:")
print("numbers = ", numbers)
print("\t")
print("Primes:", primes)
print("Not Primes:", not_primes)





