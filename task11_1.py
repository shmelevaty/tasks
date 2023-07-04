def f(a):
    p=1
    for i in range(1,a+1):
        p*=i
    return(p)

n=int(input("Введите число:"))
ch=f(n)
print("Факториал числа", n,"равен:",ch)
s=[]
for i in range(ch,0,-1):
    s.append(f(i))

print("список факториалов чисел:",s)
