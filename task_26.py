# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
a = int(input("Введите число: "))
b = int(input("Введите степень: "))

def exponentiation_recursive(a,b):
    if b == 0:
        return 1
    else:
        return a * exponentiation_recursive(a, b-1) # столько раз а * (а * (а * )) - сколько существует b

print(exponentiation_recursive(a,b))