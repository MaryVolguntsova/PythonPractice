# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
n = int(input("Введите число N-чисел массива: "))
my_massive = [random.randint(1, n) for i in range(n)] # пробую более короткий способ заполнения
print(my_massive)
x = int(input("Введите число, которое хотите найти в массиве, или я найду число, близкое по величине к нему: "))

for i in range(len(my_massive)):
    if my_massive[i] == x:
        print("Это число есть в массиве")
        break

def nearest_value(my_massive, x):
    near_x = my_massive[0]
    for item in my_massive:
        if abs(item - x) < abs(near_x - x):
            near_x = item
    return near_x

print("Близжайшее число к заданному значению", nearest_value(my_massive, x))
