z=''
x=1
y=9
for item in range(10):
    for item2 in range(0,y):
        z+="   "
    for item1 in range(0, x):
        z+= " * "
    z += "\n"
    x += 2
    y -= 1
print(z)