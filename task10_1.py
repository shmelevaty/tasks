pets ={}
pets2={}
while (True):
    n=input("Введите имя питомца: ")
    if n=='':
        break
    else:
        n1=input('Вид питомца: ')
        n2=int(input('Возраст питомца: '))
        n3=input('Имя владельца:  ')
        pets2={'Вид питомца:':n1, 'Возраст питомца:':n2, 'Имя владельца:':n3  }
        pets[n]=pets2
        for key, value in pets.items():
            vid=value['Вид питомца:']
            age=value['Возраст питомца:']
            nameof=value['Имя владельца:']
            year = ''
            if age % 10 == 1 and age != 11 and age % 100 != 11:
                year = 'год'
            elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
                year = 'года'
            else:
                year = 'лет'
        print("Это", vid, "по кличке", key,"Возраст питомца:", age, year, "Имя владельца:", nameof)

