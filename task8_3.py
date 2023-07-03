m = int(input("введите максимальную массу, которую может выдержать одна лодка:"))
n = int(input("Введите количество рыбаков:"))
a = []
for i in range(n):
    print("Вес",i+1,"рыбака:")
    a.append(int(input()))
a.sort() 
i=0
j=len(a)-1
k=0
while i<=j:
    if a[i]+a[j]<=m:
        i+=1
    j-=1
    k+=1
    
print(k)
