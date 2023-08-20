a: int = int(input("Введите число a: "))
b: int = int(input("Введите число b: "))

a, b = b, a

print("Значения после перестановки:")
print("a =", a, "\nb =", b)
# print("a = " + str(a), "b = " + str(b), sep='\n')
