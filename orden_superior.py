from functools import reduce

# Uso de filter

my_list = [1,4,5,6,9,13,19,21]

# filter recive una funcion y un iterable
odd = list(filter(lambda x: x%2 != 0, my_list))

print(odd)

my_list_two = [1,2,3,4,5]

# list comprehensions
squares = [i**2 for i in my_list_two]

print(squares)

squares_map = list(map(lambda x: x**2, my_list_two))

print(squares_map)

my_list_three = [2,2,2,2,2]

all_multiplied = 1

for i in my_list_three:
    all_multiplied = all_multiplied * i

print(all_multiplied)

reduce_func = reduce(lambda a, b: a * b, my_list_three)

print(reduce_func)
