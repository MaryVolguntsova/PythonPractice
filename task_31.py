# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
def fibonacci_numbers(n):
    if n in (1, 2):
        return 1
    return fibonacci_numbers(n-1) + fibonacci_numbers(n-2)

num = int(input("Введите N-е число Фибоначчи, которое хотите найти: "))
print("Значение этого числа = ", fibonacci_numbers(num))