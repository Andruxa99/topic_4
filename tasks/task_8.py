interval: int = int(input(
    "Введите величину временного интервала в минутах: "))

hours: float = interval // 60
minutes: float = interval % 60

print("Результат:", hours, "часа", minutes, "минут")

# 7 * 60 = 420
# 420 // 60

# 147 // 60
# 147 % 60

# 2 - часа
# 27 - минуты
