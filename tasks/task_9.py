num_switches: int = int(input("Введите количество переключателей: "))

combinations: int = (num_switches - 1) ** 3

print("Количество возможных комбинаций:", combinations)
