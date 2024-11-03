first = int(input("Первый "))
second = int(input("Второй "))
third = int(input("Третий "))

if first == second and second == third:
    print("Все числа одинаковые")
elif not (first == second and second == third):
    print("Все разные")
else:
    print("Ни то, ни другое")