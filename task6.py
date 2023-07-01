word=input("Введите слово из маленьких латинских букв")
a=word.count("a")
e=word.count("e")
i=word.count("i")
o=word.count("o")
u=word.count("u")
gl=a+e+i+o+u
sogl=len(word)-gl
print("Количество гласных букв в слове:",gl)
print("Количество согласных букв в слове:",sogl)
if a==0:
    print("Количество букв 'a' в слове: False")
else:
    print("Количество букв 'a' в слове:",a)
if e==0:
    print("Количество букв 'e' в слове: False")
else:
    print("Количество букв 'e' в слове:",e)
if i==0:
    print("Количество букв 'i' в слове: False")
else:
    print("Количество букв 'i' в слове:",i)
if o==0:
    print("Количество букв 'o' в слове: False")
else:
    print("Количество букв 'o' в слове:",o)
if u==0:
    print("Количество букв 'u' в слове: False")
else:
    print("Количество букв 'u' в слове:",u)
