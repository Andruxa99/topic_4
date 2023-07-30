num_chicken = int(input("Введите количество курочек: "))
num_cows = int(input("Введите количество коров: "))
num_pigs = int(input("Введите количество свиней: "))

total_legs: int = (num_chicken * 2) + (num_cows + num_pigs) * 4

print("Общие количество ног на ферме:", total_legs)
