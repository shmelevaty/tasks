x=int(input("Введите минимальную сумму инвестиций:"))
A=int(input("Стартовый капитал Майкла:"))
B=int(input("Стартовый капитал Ивана:"))
print("Инвестором станет:")
if A>=x and B>=x:
    print("2")
elif A>=x and B<x:
    print("Mike")
elif A<x and B>=x:
    print("Ivan")
elif (A+B)>=x:
    print("1")
else:
    print("0")
