import random
def pl(t):
    for i in t:
        print(*i)
    print()
        
n=int(input("Введите количество столбцов матрицы:"))
m=int(input("Введите количество строк матрицы:"))
tmp1=[[random.randint(-100,100) for i in range(n)] for i in range(m)]
pl(tmp1)
tmp2=[[random.randint(-100,100) for i in range(n)] for i in range(m)]
pl(tmp2)
tmp3=[[0 for i in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        tmp3[i][j]=tmp1[i][j]+tmp2[i][j]
                   
pl(tmp3)
