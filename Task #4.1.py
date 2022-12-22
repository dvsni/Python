# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# 1-й вариант: 
from math import pi
def input_number(text: str) -> int:
    try:
        number = int(input(text))
    except ValueError:
        print("Не является числом")
    return number

d = input_number("Введите сколько знаков после запятой будет у числа π: ")
print(f'Число π c заданной точностью {d} = {round(pi, d)}')

# 2-ой вариант: 
import math
d = input('Введите степень округления: ' ' ')
d = d[2:len(d)]
print(round(math.pi, len(d)))

