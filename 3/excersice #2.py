z=''
x=5
for item in range(4):
    for item1 in range(0, x):
        z+= " * "
    z += "\n"
    x -= 1
for item in range(5):
    for item1 in range(0, item+1):
        z+= " * "
    z += "\n"
print(z)