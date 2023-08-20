# number = int(input("Введите четырехзначное число: "))
#
# thousands = number // 1000
# hundreds = number % 1000 // 100
# tens = number % 100 // 10
# units = number % 10
#
# print("Цифра в позиции тысяч:", thousands)
# print("Цифра в позиции сотен:", hundreds)
# print("Цифра в позиции десятков:", tens)
# print("Цифра в позиции единиц:", units)

# TODO: Реализация для пятизначного числа
number = int(input("Введите пятизначное число: "))

tens_thousands = number // 10000
thousands = number % 10000 // 1000
hundreds = number % 1000 // 100
tens = number % 100 // 10
units = number % 10
print(tens_thousands)
print(thousands)
print(hundreds)
print(tens)
print(units)
