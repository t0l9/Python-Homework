def sum_numbers():
    s = 0
    while True:
        my_list = input("Введите числа или Q для выхода: ").split()
        for num in my_list:
            if num != "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("Для выхода нажмите Q: ")
        
        print(f"Сумма чисел равно = {s}")
    
print(sum_numbers())
