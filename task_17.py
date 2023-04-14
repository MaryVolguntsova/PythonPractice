n = int(input("Величина списка: "))
n_digits = [int(input("Введите числа: ")) for i in range(n)]
print(n_digits)
n_digits = set(n_digits)
print(n_digits)
print(len(n_digits))