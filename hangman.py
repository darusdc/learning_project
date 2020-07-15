class hangman:
    def __init__(self, p,s,knc,jwb,Clue):
        self.percobaan=p
        self.salah=s
        self.kunci=knc
        self.Clue=Clue
        self.jwb=jwb
    def play(self):
        a={1:['_____'],
        2:['|   O'],
        3:['|  /|\ '],
        4:['|   |  '],
        5:['|  / \ ']}
        b=self.percobaan
        f=self.salah
        c=self.kunci
        d=['*'*i for i in range(len(c))]
        print(self.Clue)
        b+=1
        d1=''
        hange=''
        for i in range(len(d)):
            d1+=d[i]
        print(d1)
        jw= input(f'percobaan ke {b} : ')
        d1=''
        for i in range(len(c)):
            for j in range(len(jw)):
                if jw[j]==c[i]:
                    d[i]=c[i]
            else:
                f+=1
        for i in range(len(d)):
            d1+=d[i]
        if d1==c:
            return 'horayyy! you won!'
        else:
            if f<=5 and f>0:
                for i in range(f):
                    hange+=a[f][0]
                    hange+='\n'
                print(hange)