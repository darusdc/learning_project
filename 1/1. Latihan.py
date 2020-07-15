import datetime
# nama = input("nama : ")
# umur = input("umur : ")
# print("karakter nama saya pada posisi index modulus 2 dari umur saya adalah", nama[-(int(umur) % 2) + 5:-1])

#1
# x=4
# y=3
# z=2
# w=((x+y*z)/(x*y))**z
# print(w)

# # 2

# x=input('silahkan masukkan angka berapapun: ')
# print("kuadrat dari" , x ,"=" , str(int(x)**2))

# # 3
# d=int(input("masukkan jumlah hari: "))
# year=round(d/360)
# month=int((d%360)/30)
# week=int(((d%360)%30)/7)
# day=int(((d%360)%30)%7)
# print(str(year), "Tahun" ,str(month), "Bulan", str(week), "Minggu", str(day), "Hari")

# #4
# total_usia = 49
# rasio = 0.4
# umur_budi = (total_usia*10)/(10+(rasio*10))
# umur_andi = 49-umur_budi
# print('Usia budi:',str(umur_budi),'Usia Andi',str(umur_andi),'2 tahun lagi Usia Andi dan Budi adalah:', str(int(umur_andi+2)), '', str(int(umur_budi+2)))

# #5
# w = input("Masukkan Kata:").lower()
# y=input("masukkan huruf/kata yang ingin dihitung:").lower()
# print("Jumlah huruf/kata ,' adalah {len(w.split(y)-1)}")

# #6
# jam=9*60
# m1=60
# m2=40
# j=120
# t=j/(m1+m2)
# t*=60
# jam+=t
# menit=jam%60
# print('mobil a&b tabrakan di jam', str(round(jam/60))+ ":"+ str(round(menit)))
def detik_ke_waktu(x):
    if x.isnumeric()==False:
        print('input invalid')
    else:
        x=int(x)
        if x>359999:
            print('angka yang anda masukkan lebih dari nilai maksimal')
        elif x<0:
            print('invalid')
        else:
            j=round(x/3600)
            m=round(x/60%60)
            d=round(x%60)
            if j<10:
                j=f'0{str(j)}'
            if m<10:
                m=f'0{str(m)}'
            if d<10:
                d=f'0{str(d)}'
            print(f'{j}:{m}:{d}')
detik_ke_waktu(input('masukkan jumlah detik: '))