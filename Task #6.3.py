# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt
xa = int(input("Введите координату X точки А: "))
ya = int(input("Введите координату Y точки А: "))
xb = int(input("Введите координату X точки B: "))
yb = int(input("Введите координату Y точки А: "))

distance = float(round(sqrt((xb-xa)**2+(yb-ya)**2), 3))
print(distance)

# Улучшение кода:

from operator import sub
def find_distance():
    point_a=[int(input('Введите {i} точки A') for i in 'xy')]
    point_b=[int(input('Введите {i} точки B') for i in 'xy')]
    return sum([sub(element)**2 for element in zip(point_a, point_b)]) **0.5
