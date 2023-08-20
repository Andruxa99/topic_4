number = int(input("Введите положительное трехзначное число: "))

hundreds: int = number % 1000 // 100
tens: int = number % 100 // 10
units: int = number % 10

sum_digits: int = hundreds + tens + units

product_digits: int = hundreds * tens * units

print("Сумма цифр:", sum_digits)
print("Произведение цифр:", product_digits)

"""
>>> 7 / 60
0.11666666666666667
>>> 5764597346594560549876045 % 10
5
>>> 8654 % 10
4
>>> 8654 // 1000
8
>>> 8654 % 1000 // 100
6
>>> 8654 % 1000
654
>>> 654 // 100
6
>>> 8654 // 100  # это ошибка
86
>>> 8654 % 100  # это правильно
54
>>> 54 // 10
5
>>> 8654 % 100 // 10
5
>>> 

"""
