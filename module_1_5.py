# Practical assignment on the topic: "Immutable and mutable objects. Tuples and lists"

immutable_var = (1 ,2 , 3 , 'red', 'yellow', 'The blue sea')
print(immutable_var)

# immutable_var[5] = 255 TypeError: объект 'tuple' не поддерживает назначение элементов
print(type(immutable_var)) # тип переменной immutable_var tuple

# Создание изменяемых структур данных:

mutable_list = [1 ,2 , 3 , 'red', 'yellow', 'The blue sea']
mutable_list[0] = 'black'
print(mutable_list)