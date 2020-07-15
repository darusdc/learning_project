a=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<10:
    print(a[i]**2)
    i+=1

# case 1
password='12345'
c=0
while c<=3:
    if input("masukkan password: ")!=password:
        if c==3:
            print("Try again later")
        else:
            print("Password Incorrect")
        c+=1
    else:
        print("Password correct")
        break

# quiz

for a in range(1,6):
    if a%2 !=0:
        print(a)
    else:
        print("wow!")

def fizzbuzz(x):
    x = int(x)
    c=''
    for y in range(1,x+1):
        if y%3 ==0 and y%5!=0:
            c="fizz"
        elif y%5 ==0 and y%3!=0:
            c="buzz"
        elif y%3 ==0 and y%5 ==0:
            c="fizz buzz"
        else:
            c=(y)
        print(c)

fizzbuzz(input('masukkan nilai yang ingin di fizz and buzz : '))

a=[1,2,3,4,5,6,7]
b=[]
for i in a:
    b.append(a[len(a)-i])
print(b)
