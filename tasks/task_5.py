wins: int = int(input("Введите кол-во побед: "))
draws: int = int(input("Введите кол-во ничейных игр: "))
losses: int = int(input("Введите кол-во поражений: "))

total_points: int = (wins * 3) + (draws * 1) + (losses * 0)

print("Общее кол-во очков:", total_points)
