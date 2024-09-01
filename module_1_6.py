# Practical assignment on the topic: "Dictionaries and sets"

# Работа со словарями:
my_dict = {'Мария': 1995, 'Олег': 1987, 'Алла': 2000, 'Эдуард': 1972}
print('Cловарь my_dict:',my_dict)
print('Значение по существующему ключу:', my_dict['Мария'])
print(my_dict.get('Александр', 'Таких данных нет'))
my_dict.update({'Вячеслав': 2005, 'Ольга': 2007})
print(my_dict)
print('Удаляемое значение',my_dict['Мария'])
my_dict.pop('Мария')
print(my_dict.get('Мария', 'Таких данных нет'))
print('Измененный словарь:',my_dict)
print('') #  переход на новую строку
# Работа с множествами:
my_set = {0, 1, 2, 3.14, 4, 0, 0, 4, (1, 4, 7), True}
print('Set:',my_set)
my_set.add(9)
my_set.add('String')
my_set.remove(0)
print('Modified set: ',my_set)
