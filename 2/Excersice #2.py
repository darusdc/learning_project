m=input("masukkan massa(kg): ")
t=input("masukkan tinggu(cm): ")
print("Massa "+m+" & tinggi "+ str(int(t)/100) + "m")
imt=int(m)/(int(t)/100)**2
if (imt <= 18.5) :
    print(str(imt)+", Berat badan kurang!")
elif (imt >= 18.5 and imt <=24.9):
    print(str(imt)+", Berat badan ideal!")
elif (imt>=25.0 and imt<=29.9):
    print(str(imt)+", Berat badan berlebih!")
elif (imt>=30.0 and imt<=39.9):
    print(str(imt)+", Berat badan sangat berlebih!")
elif (imt>=39.9):
    print(str(imt)+", OBESITAS WEY, AMBIL DIET!")
    pass