def temukan(c='',l = list):
    z=[]
    for i in range(0,len(l)):
        if c.lower() in l[i] or c.capitalize() in l[i]:
            z.append(l[i])
    if len(z)==0:
        z.append("Data tidak ditemukan")
    return z
ka=['Merdeka', 'Hello','Hellos','Sohib','Kari Ayam']
print(ka)
print(temukan(input("Search: "),ka))