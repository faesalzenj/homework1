s=int(input('enter decimal '))
a=[]

while s>0:
    a.append(s%2)
    s//=2
a.reverse()


for i in a:
    print(i,end='')

