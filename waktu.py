import datetime as dt
class waktu:
    hari_indo={'1':'Senin','2':'Selasa',
    '3':'Rabu','4':'Kamis',
    '5':'Jumat','6':'Sabtu','0':'Minggu'}
    bulan_indo={'01':'Januari','02':'Februari','03':'Maret',
    '04':"April",'05':'Mei','06':'Juni','07':'Juli',
    '08':'Agustus', '09':'September', '10':'Oktober',
    '11':'November','12':'Desember'}
    hari = hari_indo[dt.datetime.now().strftime('%w')]
    tanggal= dt.datetime.now().strftime('%d')
    bulan = bulan_indo[dt.datetime.now().strftime('%m')]
    tahun = dt.datetime.now().strftime('%Y')
    jam = dt.datetime.now().strftime('%H')
    menit=dt.datetime.now().strftime('%M')
    detik = dt.datetime.now().strftime('%S')

c='kucing'
d=('_ '*len(c)).split()
d1=''
# j=input("")
# for i in range(len(c)):
#     for s in range(len(j)):
#         if j[s]==c[i]:
            
print(d)