def palindrome(x):
    x=str(x)
    c=''
    for i in range(1, len(x)+1):
        c+= x[len(x)-i]
    print(f"is word {x} a paliandrome = {c.lower()==x.lower()}")

#palindrome(input("Masukkan kata yang ingin anda cek : "))

#reverse level 2
def dibalik(x):
    x=str(x)
    c=''
    lst=x.split(" ")
    for i in range(0,len(lst)):
        for y in range(1,len(lst[i])+1):
            c+=lst[i][len(lst[i])-y]
        c+=" "
    print(f'{c}')

#dibalik(input("Kata yang ingin dibalik : "))

def morsein(x):
    x=str(x)
    morse={'a':' .- ','b':' -... ','c':' -.-. ',
    'd':' -.. ','e':' . ','f':' ..-. ','g':' --. ',
    'h':' .... ','i':' .. ','j':' .--- ','k':' -.- ',
    'l':' .-.. ','m':' -- ','n':' -. ','o':' --- ','p':' .--. ',
    'q':' --.- ','r':' .-. ','s':' ... ','t':' - ','u':' .-- ',
    'v':' ...- ','w':' .-- ','x':' -..- ','y':' -.-- ','z':' --.. ',
    ' ': ' | '}
    c=''
    for i in range(0,len(x)):
            c+=morse[x[i].lower()]
    print(f"sandi morse dari {x} adalah \n{c}")
#morsein(input("masukkan kata yang ingin diubah menjadi morse: "))

def caesar_chipher(x):
    x=str(x)
    ca="abcdefghijklmnopqrstuvwxyz"
    a=''
    for i in x:
        if i==" ":
            a+=" "
        else:
            if ca.index(i) +2 >= 26:
                a+=ca[ca.index(i)-24] 
            else:
                a+=ca[ca.index(i)+2]
    print(a)
caesar_chipher(input("Masukkan kata: "))