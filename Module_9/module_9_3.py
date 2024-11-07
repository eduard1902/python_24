# генераторные сбороки

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))
print(list(second_result))

"""
Задача:
Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
Необходимо создать 2 генераторных сборки:
    1. В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков first и second,
    если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
    2. В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых
    позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

"""