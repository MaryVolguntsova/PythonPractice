# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

def if_simple(a):
    k = 0
    for i in range(2, a // 2 + 1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
    else:
        print("Число не является простым")

num = int(input('Введите число, которое хотите проверить: '))
print(if_simple(num))