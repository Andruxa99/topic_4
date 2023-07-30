interval: int = int(input("Введите величину временного интервала в минутах: "))

hours: float = interval // 60
minutes: float = interval % 60

print("Результат:", hours, "часа", minutes, "минут")
