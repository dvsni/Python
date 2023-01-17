# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

list1 = ["2","43","5","331","91","35","79","53",]
x = input("Введите число: ")

for i in list:
    if x == i:
        print("Заданное число присутсвует в списке")
        break
else:
    print("Заданное чисило отсутсвует в списке")

# Улучшение кода:

from typing import List 

def find_num(str_list:List[str], search_num:int):
    return any([element for element in str_list if str(search_num) in element])
