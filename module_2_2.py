first = int(input("Первый "))
second = int(input("Второй "))
third = int(input("Третий "))

if first == second == third:
    print(3)
elif first == second or second == third:
    print(2)
else:
    print(0)
