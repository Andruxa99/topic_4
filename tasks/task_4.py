num_chicken = int(input("Введите кол-во курочек: "))
num_cows = int(input("Введите кол-во коров: "))
num_pigs = int(input("Введите кол-во свиней: "))

total_legs: int = (num_chicken * 2) + (num_cows * 4) + (num_pigs * 4)

print("Общие кол-во ног на ферме: ", total_legs)
