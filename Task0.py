import random as rnd
size=int(input('Введи размер многочлена: '))


def create_mnogochlen(size):
    koef={}
    for i in range(size+1):
        koef[i]=rnd.randint(0,100)
    print(koef)

    mnogochlen=''
    for i in range(size,-1,-1):
        if koef[i]!=0:
            if koef[i]==1:
                if i==1:
                   mnogochlen+=f'x + '
                elif i==0:
                   mnogochlen+=f'1'
                else:
                   mnogochlen+=f'x**{i} + '
            else:
                if i==1:
                   mnogochlen+=f'{koef[i]}*x + '
                elif i==0:
                   mnogochlen+=f'{koef[i]} '
                else:
                   mnogochlen+=f'{koef[i]}*x**{i} + '
    if koef[0]==0:
        mnogochlen=mnogochlen[:-2]
    index=mnogochlen.find('x')
    if index==-1:
       return print('0 = 0')
    else:
       return print(mnogochlen+'= 0')

test=create_mnogochlen(size)

