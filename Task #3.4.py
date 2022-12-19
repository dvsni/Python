# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import math
def to_bin(input_decimal, i):
    if (input_decimal < 0):
        return "Не преобразуется"
    elif (input_decimal > 0):
        temp = input_decimal % 2
        return to_bin(input_decimal//2, i + 1) + int(temp*math.pow(10,i))
    else:
        return 0
decimal_number = int(input("Введите десятичное число: "))
print("Преобразование десятичного числа в двоичное: ", to_bin(decimal_number, 0))