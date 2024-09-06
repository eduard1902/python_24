# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print("Исходные данные:", my_list)
print("Вывод на консоль:")

index = 0 # Объявляю переменную для индекса

while index < len(my_list):
    current_number = my_list[index] # Получаем текущий элемент

    if current_number < 0: # Проверка на отрицательное число
        break

    if current_number == 0:   # Проверка на ноль
        index += 1
        continue

    print("\t", current_number) # Перенос строки и вывод положительного числа

    index += 1 # Увеличиваем индекс
