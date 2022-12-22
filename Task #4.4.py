# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random, string
file = open('For4.4.txt', 'w', encoding = 'UTF-8')
k = random.randint(1, 5)
coeffs = []
print(k)
i = 0
while i<k+1:
    coeffs.append(random.randint(0, 100))
    i += 1
print(coeffs)
equation = ''
for ind, coeff in enumerate(coeffs):
    if ind == len(coeffs) - 1:
        if coeff > 0:
            equation += str(coeff)
        equation += '=0'
    else:
        if coeff > 0:
            if coeff > 1:
                equation += str(coeff)
            equation += '*x'
            if ind < len(coeffs) - 2:
                equation += '**' + str(len(coeffs) - 1 - ind)
            equation += '+'
file.writelines(equation)
file.close
print(equation)