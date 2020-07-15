z='';
x=1;
y=9;
for item in range(6):
    for item1 in range(0, x):
        for item2 in range(0,y):
            z+=" "
        z+= " * "
    z += "\n"
    x += 2
    y -= 1
print(z)