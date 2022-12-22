# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from random import choice

def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="UTF-8") as my_f_1, \
        open(name_2, "r", encoding="UTF-8") as my_f_2:

     first = my_f_1.readlines()
     second = my_f_2.readlines()
     if len(first) == len(second):
        with open("sum4.5.txt", "w", encoding="UTF-8") as my_f_3:
            for i, v in enumerate(first):
                my_f_3.write(f"{v[:-5]} + {second[i]}")
     else:
        print("Содержание файла не соответсвует")
poly_sum("for4.5(1).txt","for4.5(2).txt")

