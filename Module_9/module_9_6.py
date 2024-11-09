# Генераторы

def all_variants(text):
    text_l = len(text)
    for t in range(text_l):
        for s in range(text_l - t):
             yield text[s:s + t +1]


a = all_variants("abc")
for i in a:
    print(i)
"""
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
1. Напишите функцию-генератор all_variants(text).
2. Опишите логику работы внутри функции all_variants.
3. Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
a = all_variants("abc")
for i in a:
print(i)
Вывод на консоль:
a
b
c
ab
bc
abc
"""

