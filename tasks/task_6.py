num_1 = int(input("Введите первое положительное число: "))
num_2 = int(input("Введите второе положительное число: "))

is_divisible: float = (num_1 % num_2) == 0

print(bool(is_divisible))

# ------ example
k = 11

k % 2 == 0  # четное
# k % 2 != 1  # четное

k % 2 != 0  # нечетное
# k % 2 == 1  # нечетное
