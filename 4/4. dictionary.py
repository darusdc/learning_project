# andy={
#     'nama': 'andy',
#     'usia':22,
#     'jomblo':True,
#     'Pekerjaan':'PNS',
#     'kendaraan:':['mobil','motor','sepeda'],
#     'address': {
#         'street': 'Jalan Mawar',
#         "RT": 5,
#         "RW": 3,
#         "zipcode":171722,
#         "geo": {
#             'lat' : 14455.11,
#             'long' : 14423.2
#         }
#     }
#     }
# #menambahkan dictionary
# andy['gaji'] = {"harian":250, 'bulanan': 450, 'tahunan': 770}
# print(andy['gaji']['bulanan'])

#Quiz
bahasa = {'senin':'monday',
'selasa':'tuesday',
'rabu':'wednesday',
'kamis': 'thursday',
'jumat':'friday',
'sabtu':'saturday',
'minggu': 'sunday'}

user=input('Masukkan nama hari : ').lower()
if bahasa.get(user):
    #
    print('bahasa inggris dari hari', user, 'adalah', bahasa[user])
else:
    print('Indonesian language for', user, 'day is', list(bahasa.keys())[list(bahasa.values()).index(user)])
#                                                   [senin-minggu][[monday-sunday].index(monday)]#                                                                          
#                                                           [senin-mnggu][0]