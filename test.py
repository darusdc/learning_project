# from waktu import waktu
# from Statistik import statistik
# w=waktu
# print(f"sekarang hari {w.hari} tanggal {w.tanggal}/{w.bulan}/{w.tahun} jam {w.jam}:{w.menit}:{w.detik}")
# i = input('Masukkan deret angka dipisah dengan koma: ').split(',')
# i=[int(i) for i in i]
# stat= statistik(i)
# print(f' Data {i} memiliki \n rata-rata: {stat.mean()} \n nilai tengah: {stat.median()} \n nilai maksimal: {stat.max()}\n nilai minimum: {stat.min()}\n data yang sering muncul: {stat.modus()}')
# data=open('coba.txt','w+')
# data.write("cobalah mengerti!")
a={1:['_____\n|   |'],
2:['|   O'],
3:['|  /|\\ '],
4:['|   |  '],
5:['|  / \\ ']}
b=0
f=0
c='Badak'
d=('_ '*len(c)).split() #_____
print('Hewan berkaki 4!')
d1=''
hange=''
bener=False
while d1!=c or f==5:
    b+=1
    bener=False
    d1=''
    jw= input(f'percobaan ke {b} : ')
    d1=''
    for i in range(len(c)):
        for j in range(len(jw)):
            if jw[j].lower()==c[i].lower():
                d[i]=c[i] #_a_a_
                bener=True
    d1=''.join(d)
    print(d1)
    if d1==c:
        print('Selamat kamu berhasil!')
        print(hange)
    else:
        if bener==False:
            if (f>=0) and (f<4):
                f+=1
                hange+=a[f][0]
                hange+='\n'
            else:
                f+=1
                hange+=a[f][0]
                hange+='\n'
                print('Kamu gagal :(')
                print(hange)
                break
        print(hange)