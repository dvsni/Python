# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number_n = int(input("Введите целое число: "))
factorial_list = [1]
i = 1
while i < number_n:
    factorial_list.append(factorial_list[i - 1]*(i + 1))
    i+=1
print(factorial_list)