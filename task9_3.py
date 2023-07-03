N=int(input("введите количество элементов списка:"))
print("Введите элементы списка через пробел")
a = list(map(int, input().split()))
m=set()
for i in range(len(a)):
    if a[i] in m:
        print("Yes")
    else:
        print("No")
        m.add(a[i])
