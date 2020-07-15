'''
> : Lebih Besar
< : Lebih Kecil
==: sama dengan
>=: lebih besar sama dengan
<=: lebih kecil sama dengan
!=: tidak sama dengan
and: dan
or: atau
True and True : true
True and False : False
False and True : False
False dan False : False
'''
#ganjil genap
x = input("Masukkan Angka : ")
if (int(x)%2 == 0) :
    print("Angka "+x+" tergolong bilangan genap")
else :
    print("Angka "+x+" tergolong bilangan ganjil")

#Body Mass Index
m=int(input("masukkan massa(kg): "))
t=int(input("masukkan tinggu(cm): "))
print("Massa", str(m), "KG & tinggi", str(t/100), "m")
imt=m/((t/100)**2)
if (imt <= 18.5) :
    print(str(imt)+", Berat badan kurang!")
elif (imt > 18.5 and imt <=24.9):
    print(str(imt)+", Berat badan ideal!")
elif (imt>24.9 and imt<=29.9):
    print(str(imt)+", Berat badan berlebih!")
elif (imt>29.9):
    print(str(imt)+", OBESITAS!")