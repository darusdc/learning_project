from functools import reduce
class statistik():
    def __init__(self,data):
        self.data= list(data)
    
    def mean(self):
        x=self.data
        a=reduce(lambda a,b:a+b,x)
        b=len(x)
        return round(a/b,2)
    def median(self):
        x= self.data
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[i] >x[j]:
                    x[i],x[j]=x[j],x[i]
        if len(x)%2!=0:
            return x[int(len(x)/2)]
        else:
            return x[((x[(len(x)//2)]+x[(len(x)//2)-1])//2)]
    def max(self):
        x=self.data
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[i] >x[j]:
                    x[i],x[j]=x[j],x[i]
        return x[-1]
    def min(self):
        x=self.data
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                if x[i] >x[j]:
                    x[i],x[j]=x[j],x[i]
        return x[0]
    def modus(self):
        x=self.data
        banyak=dict()
        jt=[]
        for i in range(len(x)):
            banyak[x[i]]=x.count(x[i]) #[1:2][1:2][2:3][2:3][2:3][3:1][4:1][5:1][6:2]
        for i,v in banyak.items():#[1:2][2:3][3:1][4:1][5:1][6:2]
            jt.append(v)
        for c in range(len(jt)): #hasil jt[2,3,1,1,1,2]
            for d in range(c+1,len(jt)):
                if jt[c]>jt[d]:
                    jt[c],jt[d]=jt[d],jt[c]# [1,1,1,2,2,3]
        if jt[-1]==jt[-2]:
            return f'nilai yang sering muncul lebih dari sama dengan 2'
        else:
            return list(banyak.keys())[list(banyak.values()).index(jt[-1])]
            #       [1,2,3,4,5,6][2,3,1,1,1,2].index(3)
