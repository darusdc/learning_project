z=''
x=1
y=5
for item in range(5):
    for item2 in range(y):
        z+="   "
    for item1 in range(x):
        z+= " * "
    z += "\n"
    x += 2
    y -= 1
for item in range(6):
    for item2 in range(y):
        z+="   "
    for item1 in range(x):
        z+= " * "
    z += "\n"
    x -= 2
    y += 1
print(z)