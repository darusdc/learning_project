# i = 10
# x = 0
# while(i>0):
#     print(' . ' * i)
#     i -= 1
# z=''
# x=4
# y=1
# for pengulangan in range(0,15):
#     for garisx in range(0,x):
#         if x<=0:
#             z+=" "*3
#         else:
#             z+=" "        
#     for garisy in range(0,y):
#         z+= " * "    
#     z+="\n"
#     x-=1
#     if garisy>=5:
#         y=1
#     else:
#         y+=1
# print(z)
from functools import reduce
#panah atas
def panah_atas(x):
    z=''
    x=int(x)
    x_1=x
    y=1
    smb=input("masukkan simbol untuk digambar panah atas!: ")
    if len(smb)>1:
        print('Error! masukkan 1 karakter saja. :)')
    else:
        for i in range(0,x):
            if i <= round(x/2):
                for a in range(0,x):
                    z+=' '
                for b in range(0,y):
                    if b==0:
                        z+=smb
                    else:
                        z+=smb*2
                z+="\n"
                x-=1
                y+=1
            else:
                x=x_1
                y=1
                for a in range(0,x):
                    z+=' '
                for b in range(0,y):
                    z+=smb
                z+="\n"
    print(z)
#panah_atas(input('masukkan angka : '))
def rowSumOddNumbers(x=int):
    if type(x)!=int or x==0 or x<0:
        print('input yang anda masukkan salah!')
        return False
    out=' '
    x+=1
    odd=[i for i in range(1,(x*x)-(x-1),2)]
    odc=odd[-(x-1):]
    jumlah=' + '.join(map(str,odc))
    hasil = reduce(lambda a,b: a+b,odc)
    for i in range(1,len(odd)):
        if len(odd)==0:
            break
        if i==1:
            out+= " "*((x*2)-(3))
        else:
            out+= " "*((x*2)-(i*2))
        for y in range(i):
            out+= str(odd[0])
            if len(str(odd[0]))==1:
                out+= "   "
            elif len(str(odd[0]))==2:
                out+= "  "
            else:
                out+=" "
            odd.pop(0)
        out+='\n'
    # out.ljust(x*2)
    print(out)
    print(f'jumlah {jumlah} = {hasil}')
rowSumOddNumbers(int(input('masukkan bilangan 1-20: ')))
def ticket(x=list,price=25,operator='Vasya'):
    if x[0]<price:
        return f"No. Customer will not have enough money to buy ticket by {x[0]} dollars of {price} dollar" 
    elif x[0]!=price:
            return f"No. {operator} will not have enough money to give a change to {x[0]} dollars"
    else:
        cashav=[x[i] for i in range(len(x)) if x[i]==price]
        custlist=[x[i]-price for i in range(len(x))]
        p=0
        for i in custlist:
            v=i
            if i>=price:
                for y in range(len(cashav)):
                    if i==0:
                        continue
                    else:
                        cashav[y]=0
                        i-=price
                        p+=1
                        if y==len(cashav)-1:
                            if i!=0:
                                if p>1:
                                    return f'No. {operator} will not have the right bills to give {v+price} dollar of change (you cannot make two bills of {price} from one {v+price})'
                                elif p==1:
                                    return f'No. {operator} will not have the right bills to give {v+price} dollar of change.'    
            elif i<0:
                return f"No. Customer will not have enough money to buy ticket by {v+price} dollars of {price} dollar"
            else:
                continue
        return "Yes"
        # print(custlist)
        # print(cashav)
#print(ticket([10,10,25],10,'Egi'))
def nb_year(p0=1000,percent=2,imigrant=50,target=1200):
    percent=percent/100
    tke=0
    p=p0
    hit=lambda x: (x+(x*percent)+imigrant)
    while p<=target:
        tke+=1
        p=hit(p)
    return f'with initial population: {p0} it will reach {target} by {tke} years'
#print(nb_year(50,4,50,1000))
        