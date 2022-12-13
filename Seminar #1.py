# 1. Напишите программу, которая принимает на вход два числа и проверяет является ли одно число квадратом другого.
# *Примеры:*
# -5, 25 -> да
# -4, 16 -> да
# -25, 5 -> да
# -8, 9 -> нет

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# print(f'{num1}, {num2} ->', end=' ')
# if num1 == num2 ** 2 or num2 == num1 ** 2:
#     print('да')
# else:
#     print('нет')


# 2. Напишите программу, которая на вход принмает 5 чисел и находит максимальное из них.
# Примеры:
# -1,4,8,7,5 -> 8
# -78,55,36,90,2 -> 90

# num1 = int(input('Введите первое число'))
# num2 = int(input('Введите второе число'))
# num3 = int(input('Введите третье число'))
# num4 = int(input('Введите четвертое число'))
# num5 = int(input('Введите пятое число'))
# my_max = num1
# if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#     print(f'{num1} максимальное')
# elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
#     print(f'{num2} максимальное')
# elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
#     print(f'{num3} максимальное')
# elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
#     print(f'{num4} максимальное')
# else:
#     print(f'{num5} максимальное')

# numbers = []
# for i in range(1, 6):
#     numbers.append(int(input(f'Введите элемент под номером {i}: ')))
# print(numbers)
# print(max(numbers))

# 3. Напишите программу, которая на вход будет принимать число N и выводить числа от -N до N.
# *Примеры:*
# -5 -> -5,-4,-3,-2,-1,0,1,2,3,4,5

# n = int(input('Введите число: '))
# if n < 0:
#     n *= -1
# for i in range(-n, n+1):
#     print(i, end=' ')

# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру
# дробной части числа.
# *Примеры:*
# -6,78 -> 7
# -5 -> нет
# -0,34 -> 3

# num = float(input('Введите число: '))
# if num % 1 == 0:
#     print('Нет')
# else:
#     num = int(num*10 % 10)
#     print(num)

# num = input('Введите число: ')
# if '.' in num:
#     index_num = num.find('.')+1
#     print(num[index_num])
# elif ',' in num:
#     index_num = num.find(',')+1
#     print(num[index_num])
# else:
#     print('Дробной части нет')

# 5. Напишите программу, которая принмает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30

# user_number = int(input('Введите число: '))
# if ((user_number % 5 == 0 and user_number % 10 == 0) or user_number % 15 == 0) and user_number % 30 != 0:
#     print('Твое число кратно!')
# else:
#     print('Попробуй снова')
