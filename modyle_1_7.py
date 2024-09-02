# Additional practical task for the module

grades = [[5,3,3,5,4], [2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(list(students)) #Преобразование множества в список и сортировка списка
# Средние значения оценок для каждого студента
grade= list() #Новый список
for item in grades:
    grade.append(sum(item) / len(item))
# Как вариант используя функции lambda, map, dict
# Lambda аргументы: выражение
# map() преобразует к каждый элементу в массиве и преобразует их в новый массив.
# dict() создаёт словарь
result = dict(map(lambda i,j : (i,j), students,grade))
print(result)