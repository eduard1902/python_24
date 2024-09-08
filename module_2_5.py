# Домашняя работа по уроку "Функции в Python. Функция с параметром"

# Задача "Матрица воплоти":

def get_matrix(n, m, value): # Объявите функцию get_matrix и напишите в ней параметры n, m и value
    matrix = [] # Создаю пустой список matrix внутри функции get_matrix
    for i in range(n): # Первый цикл for для кол-ва строк матрицы, n повторов.
        matrix_column = [] # Cоздаю пустой список matrix_column (колонок)
        matrix.append(matrix_column) # Записываем значение
        for j in range(m): # Второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
            matrix_column .append(value) # Пополнение ранее добавленный пустого списка matrix_column значениями value.
    return matrix # Возвращение значений переменной matrix

# Вывод на экран(консоль) результат работы функции get_matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)