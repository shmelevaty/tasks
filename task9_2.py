N1=int(input("Введите количество чисел первого списка:"))
a1=[]
for i in range(N1):
    print("Введите",i+1,"число:")
    ch=int(input())
    a1.append(ch)
m1=set(a1)
print(m1)
N2=int(input("Введите количество чисел второго списка:"))
a2=[]
for i in range(N2):
    print("Введите",i+1,"число:")
    ch=int(input())
    a2.append(ch)
m2=set(a2)
print(m2)
print("Количество чисел, содержащихся одновременно и в первом и во втором списке:",len(m1.intersection(m2)))
