
x = int(input("Введите действительное положительное число: "))
y = int(input("целое отрицательное число: "))

def my_func(x,y):
    return x ** y

def my_func_1(x,y):
    res = 1
    for i in range(abs(x)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res

print(my_func(x,y))
print(my_func_1(x,y))
