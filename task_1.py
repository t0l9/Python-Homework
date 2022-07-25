def salary():
    time = float(input("Выработка в часах: "))
    salary = int(input("Ставка в час: "))
    bonus = int(input("Премия: "))
    res = time * salary + bonus
    return f"Заработная плата сотрудника  {res}"
print(salary())
