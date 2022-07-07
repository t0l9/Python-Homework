a = int(input(f"Введите число: "))
b = int(input(f"Введите число: "))
c = int(input(f"Введите число: "))

def my_func(a, b, c):
    list = [a, b, c]
    list.sort()
    return list[-1] + list[-2]

print(my_func(a,b,c))
