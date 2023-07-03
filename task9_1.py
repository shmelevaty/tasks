N=int(input("Введите количество чисел:"))
a=[]
for i in range(N):
    print("Введите",i+1,"число:")
    ch=int(input())
    a.append(ch)
am=set(a)
print("Количество различных чисел среди введенных равно ",len(am))
