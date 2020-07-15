# quiz 1
# inp=[2,4,6,8]
# print(inp)
# print(list(map(lambda a:a**2,inp)))
# y= [a**2 for a in inp]
# print(y)

#quiz 2
# words_list = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']
# inp=input("what do you want to search? ")
# print(list(filter(lambda a: inp in a, words_list)))

#quiz 3
# inp = [1,2,3,4,5]
# print(list(map(lambda a: a*2, filter(lambda a: a>3,inp))))

#quiz 4
# inp=int(input("masukkan angka yang ingin difaktorkan: "))
# itung=[i+1 for i in range(inp)]
# print(f'bilangan faktor dari {inp} adalah {list(filter(lambda a: inp%a==0, itung))}')

#quiz 5
# inp=int(input("masukkan angka yang ingin difaktorkan: "))
# itung=[i+1 for i in range(inp)]
# def prima_check(x):
#     for j in range(1,x+1):
#         if j >1:
#             for i in range(2,x):
#                 if x%i==0:
#                     break
#             else:
#                 return x
# print(list(filter(prima_check,itung)))
# barang=['transaksi','Jasa',"biaya","ongkos"]
# harga=500
# harga=[harga*i if i>0 else 100 for i in range(len(barang))]
# e= dict(zip(barang, harga))
# print(e)
from functools import reduce

# inp=[i+1 for i in range(0,100)]
# a = map(lambda a: a*2, filter(lambda a: a if a%2==0 else False,inp))
# print(reduce(lambda a,b: a+b,a))
# print(reduce(lambda a,b: a+b,inp))

