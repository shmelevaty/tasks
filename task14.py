def v(n):
    if n==[]:
        print("Конец списка")
    else:
        print(n.pop(0))
        v(n)


my_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
v(my_list)
