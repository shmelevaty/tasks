N=int(input("введите количество элементов списка:"))
a=[]
for i in range(1,N+1):
    print(i,"элемент:")
    ai=int(input())
    a.append(ai)
a.reverse()
print(a)
