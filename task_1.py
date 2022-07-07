a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

def division(a, b):
    if b != 0:
        return a/b
    else:
        return "На ноль делить нельзя"

print(division(a, b))
