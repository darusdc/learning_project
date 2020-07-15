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
panah_atas(input('masukkan angka : '))
#panah Kanan