def iskabisat(x):
    x=int(x)
    
    if x%400<100 and x%400%4==0:
        return f'{x} adalah kabisat'
    else:
        return f'{x} bukan kabisat'
    # else:
    #     y=x%100
    #     if y%4==0:
    #         return f'{x} adalah kabisat'
    #     else:
    #         return f'{x} bukan kabisat'
# print(iskabisat(input("masukkan tahun: ")))

student_data = [
    {'nama': 'Andi', 'usia': 21},
    {'nama': 'Budi', 'usia': 22},
    {'nama': 'Caca', 'usia': 23},
    {'nama': 'Deni', 'usia': 24},
]
class student():
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

def masukin(x = dict):
    student_list=[]
    for i in range(len(x)):
       student_list.append(student(x[i]['nama'],x[i]['usia']))
    return student_list

x=student_data
for i in range(len(x)):
    vars()[x[i]['nama'].lower()] = student(x[i]['nama'],x[i]['usia'])
x=masukin(student_data)
# print(x[0].nama)
# print(x[0].usia)
# print(x[1].nama)
# print(x[1].usia)
# print(andi.nama)
# print(andi.usia)
# print(budi.nama)
# print(budi.usia)

class persegi():
    def __init__(self,sisi):
        self.luas=sisi**2
        self.keliling=sisi*4

c= persegi(int(input('masukkan panjang sisi: ')))
print(f'luas persegi adalah {c.luas}, dengan keliling {c.keliling}')