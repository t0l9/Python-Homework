def int_func(word):
    latin = "qwertyuiopasdfghjklzxcvbnm"
    return word.title() if not set(word).difference(latin) else False

words = input("Введите строку из слов через пробел: ").split()
for i in words:
    result = int_func(i)
    if result:
        print(int_func(i), " ")
        