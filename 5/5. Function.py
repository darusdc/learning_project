# def ratarata(x):
#     import math
#     print(math.sqrt(x))

# ratarata(10)

# def calc(x,y,z):
#     if y =="-":
#         print("hasil pengurangan dari",x,'dan',z,'adalah',str(x-z))
#     elif y=="+":
#         print("hasil penambahan dari ",x,'dan',z,'adalah',str(x+z))
#     elif y=="/" or y==":":
#         print("hasil pembagian dari ",x,'dan',z,'adalah',str(x/z))
#     elif y=="*" or y=="x":
#         print("hasil perkalian dari ",x,'dan',z,'adalah',str(x*z))
#     elif y=="**" or y=="^":
#         print("hasil pangkat dari ",x,'dan',z,'adalah',str(x**z))

# calc(14,'x',12)
# def triangle(a,t):
#     a = int(a)
#     t= int(t)
#     print("Luas segitiga yang anda inginkan adalah", (a*t)/2)
# def lingkaran(r):
#     r= int(r)
#     print("Luas Lingkaran yang anda inginkan adalah", 3.14*(r**2))

# c=input("jenis bangun apa yang ingin anda hitung? ").lower()
# if c == 'segitiga':
#     c=input("masukkan alas dan tinggi dipisah dengan coma tanpa spasi : ")
#     triangle(c.split(",")[0], c.split(",")[-1])
# elif c=='lingkaran':
#     lingkaran(input('Jari-jari lingkaran: '))

# def vocal_changer_o(kata):
#     kata.lower()
#     kata=kata.replace('a','o')
#     kata=kata.replace('i','o')
#     kata=kata.replace('u','o')
#     kata=kata.replace('e','o')
#     return kata

# print(vocal_changer_o('aaaaaaaaaaaaaaaaaaaaaaaaa'))
a= {"test_1" : ["",[print("Berhasil")]]}
contoh = [a]
def fungsi1(x):
    return 0
def fungsi2(x,y):
    return 1
def fungsi3(z):
    return [0]
def fungsi4():
    return 0
#print(contoh[0])   
contoh[fungsi1(0)]['test_1'][fungsi2(0,0)][fungsi3(0)[fungsi4()]]