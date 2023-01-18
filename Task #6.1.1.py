# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

#1-ый вариант:
from random import sample

numbs = list(map(abs, sample(range(-20, 20), 20)))
print("Начальный список чисел: ")
print(f"\t{numbs}")
result = [n for i, n in enumerate(numbs[1:]) if n > numbs[i]]
print("Элементы этого списка, значения которых больше предыдущего элемента: ")
print(f"\t{result}")

#2-ой вариант:
list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
new_list = [el for el in list if el > list[list.index(el) - 1]]
print(new_list)