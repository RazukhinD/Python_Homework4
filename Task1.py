import random as rnd
size1=int(input('Введи размер первого многочлена: '))
size2=int(input('Введи размер второго многочлена: '))

def create_dict_with_coef(size):
    koef={}
    for i in range(size+1):
        koef[i]=rnd.randint(0,100)
    return (koef)

def create_mnogochlen(koef,size):
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
        else:
            mnogochlen=mnogochlen
    if koef[0]==0:
        mnogochlen=mnogochlen[:-2]
    index=mnogochlen.find('x')
    if index==-1:
       return '0 = 0'
    else:
       return f'{mnogochlen} = 0'
koef1=create_dict_with_coef(size1)
koef2=create_dict_with_coef(size2)
mnogochlen1=create_mnogochlen(koef1,size1)
mnogochlen2=create_mnogochlen(koef2,size2)

data1=open('mnogochlen1.txt','w')
data1.write(mnogochlen1)
data1.close()
data2=open('mnogochlen2.txt','w')
data2.write(mnogochlen2)
data2.close()

data1=open('mnogochlen1.txt','r')
while True:
    line = data1.readline()
    if not line:
        break
    first_read_mnogochlen=line
data1.close()
data2=open('mnogochlen2.txt','r')
while True:
    line = data2.readline()
    if not line:
        break
    second_read_mnogochlen=line
data2.close()
print(first_read_mnogochlen)
print(second_read_mnogochlen)

def create_koef_dict(mnogochlen):
    mnogochlen=mnogochlen.replace(' ','')
    mnogochlen=mnogochlen.replace('*','')
    mnogochlen=mnogochlen[:-2].split('+')
    koef=[]
    koef_keys=[]
    for item in mnogochlen[:-1]:
        if item.split('x')[1]=='':
             koef_keys.append(1)
        else:
            koef_keys.append(int(item.split('x')[1]))
    for item in mnogochlen:
        if item.split('x')[0]=='':
            koef.append(1)
        else:
            koef.append(item.split('x')[0])
    koef_keys=koef_keys[:-1]
    koef_keys.append(0)
    koef_dict=dict(zip(koef_keys,koef))
    return koef_dict

koef1_dict=create_koef_dict(first_read_mnogochlen)
koef2_dict=create_koef_dict(second_read_mnogochlen)
print(koef1_dict)
print(koef2_dict)

a=(koef1_dict,koef2_dict)
result_koef_dict = {}

for dictionary in a:
  for key in dictionary:
    try:
      result_koef_dict[key] += int(dictionary[key])
    except KeyError:
      result_koef_dict[key] = int(dictionary[key])


print(result_koef_dict)



