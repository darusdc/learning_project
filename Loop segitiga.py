def segitiga_angka(x):
    c=''
    x=int(x)
    for i in range(x,0,-1):
        for j in range(i):
            c+=f' {i} '
        c+= "\n"
    print(c)
#segitiga_angka(input('masukkan bilangan : '))

def segitiga_angka_rev(x):
    x=int(x)
    a=''
    for i in range(x):
        a+=f' {str(x-i)} '
        print(a)
#segitiga_angka_rev(input('masukkan bilangan : '))

def jam_pasir():
    b=20
    for i in range(b-1,1,-2):
        print(" "*(b-i)+ " *"*i)
    for i in range(1,b,2):
        print(" "*(b-i)+ " *"*i)
#jam_pasir()
# print(list(range(20-1,1,-2)))
# print(list(range(1,20,2)))
def digitalize_int(x):
    x=int(x)
    l1=''
    l2=''
    l3=''
    x = input('Masukkan Angka : ')
    if x>=10:
        print("angka terlalu banyak")
    else:
        if x==1:
            l1="   |"
            l2='   |'
            l3='   |'
        elif x==2:
            l1='__'
            l2=' _|'
            l3='|__'
        elif x==3:
            l1='__ '
            l2='__|'
            l3='__|'
        elif x==4:
            l1='| |'
            l2='|_|'
            l3='  |'
        elif x==5:
            l1=' _'
            l2='|_'
            l3=' _|'
        elif x==6:
            l1="|  "
            l2="|__ "
            l3="|__|"
        elif x==7:
            l1="__"
            l2="  |"
            l3="  |"
        elif x==8:
            l1=' _ '
            l2='|_|'
            l3="|_|"
        elif x==9:
            l1=' _'
            l2='|_|'
            l3=' _|'
        elif x==0:
            l1=' _'
            l2="| |"
            l3='|_|'
        
        print(f'{l1}\n{l2}\n{l3}')

def digitalize_int_dict(x):
    
    angka = { '0' : [' _ ', '| |', '|_|'] ,
            '1' : ['   ', '  |', '  |'] ,
            '2' : [' _ ', ' _|', '|_ '] ,
            '3' : [' _ ', ' _|', ' _|'] ,
            '4' : ['   ', '|_|', '  |'] ,
            '5' : [' _ ', '|_ ', ' _|'] ,
            '6' : [' _ ', '|_ ', '|_|'] ,
            '7' : [' _ ', '  |', '  |'] ,
            '8' : [' _ ', '|_|', '|_|'] ,
            '9' : [' _ ', '|_|', ' _|'] ,
            }
    y = ''
    for a in range(0,3) :
        
        for b in x :
            y += angka[b][a]
                # angka['1'][0]
        y += '\n'

    print(y)
#digitalize_int_dict(input('masukkan angka: '))
def rata_kanan(x):
    c=''
    for i in range(x):
        c+= f' '*(i)+ '*'*(x-i)+'\n'
    print(c)
rata_kanan(5)
