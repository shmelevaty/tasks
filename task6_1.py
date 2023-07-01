N=int(input("Введите количество чисел:"))
k=0
for i in range(1,N+1):
    print("Введите",i,"целое число:")
    chislo=int(input())
    if chislo==0:
        k+=1
print("Количество введенных нулей:",k)
