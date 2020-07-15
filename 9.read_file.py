import json
import csv
# data=open('daftar.csv','r')
# x=data.read().split('\n')
# head=x[0].split(',')
# content=[]
# z=[]
# for a in x[1:]:
#     content=a.split(',')
#     z.append(dict(zip(head,content)))
# data=open('daftar1.json','w')
# data.write(str(z))
def csv_to_json(path_csv,path_json):
    listdata=[]
    with open(path_csv, mode='r') as daftar:
        a=csv.DictReader(daftar)
        fieldn=list(a.fieldnames)
        fieldc=list(a.reader)
        for i in fieldc:
            listdata.append(dict(zip(fieldn,i)))
    with open(path_json,'w') as tulis:
        json.dump(listdata, tulis)
def json_to_csv(path_json,path_csv):
    with open(path_json,'r') as daftar:
        a=json.load(daftar)
        fieldn=list(a[0].keys())
    with open(path_csv,'w', newline='') as tulis:
        write= csv.DictWriter(tulis,fieldn)
        write.writeheader()
        write.writerows(a)
def isvalidcc4(no):
    a=str(no)
    valid=False
    b=[]
    if a.find('-')>0 or len(a)==16:
        # print('masuk 1')
        if a[0]=='4' or a[0]=='5' or a[0]=='6':
            # print('masuk 2')
            if a.find('-')>0:
                c=a.split('-')
                # print(c)
                for i in c:
                    # print(i)
                    if len(i)>4 or len(i)<4 or i.isnumeric()==False:
                        b.append(False)
                        break
                    else:
                        for j in range(len(i)):
                            if i==i[j]*4:
                                # print('vat')
                                b.append(False)
                                continue
                            else:
                                # print('tur')
                                b.append(True)
                                break
            else:
                if a.isnumeric()==False:
                    # print('salah')
                    b.append(False)
                else:
                    chk=[]
                    for i in range(0,len(a),4):
                            chk.append(a[i:i+4])
                    for i in chk:
                        for j in range(len(i)):
                            if i==i[j]*4:
                                # print('vat')
                                b.append(False)
                                continue
                            else:
                                # print('tur')
                                b.append(True)
                                break
        else:
            # print('masuk terakhir')
            b.append(False)
    else:
        b.append(False)
    # print(b)
    if b.count(False)>0:
        valid=False
    else:
        valid=True
                    
    return valid
def isvalidcc(no):
    a=str(no)
    valid=False
    b=[]
    if a.find('-')>0 or len(a)==16:
        # print('masuk 1')
        if a[0]=='4' or a[0]=='5' or a[0]=='6':
            # print('masuk 2')
            if a.find('-')>0:
                d=a.split('-')
                c=a.replace('-','')
                for i in d: 
                    if len(i)>4 or len(i)<4:
                        b.append(False)
                # print(c)
            else:
                c=a
            if c.isnumeric()==False or len(c)>16:
                # print('salah')
                b.append(False)
            else:
                for j in range(len(c)):
                    if c[j:j+4]==c[j]*4:
                        # print('vat')
                        b.append(False)
                    else:
                        # print('tur')
                        b.append(True)
        else:
            # print('masuk terakhir')
            b.append(False)
    else:
        b.append(False)
    # print(b)
    if b.count(False)>0:
        valid=False
    else:
        valid=True                
    return valid

# with open('nasabah.json','r') as baca:
#     a=json.load(baca)
#     val=[]
#     inval=[]
#     for i in range(len(a)):
#         if isvalidcc(a[i]['noCreditCard'])==True:
#             val.append(a[i])
#         else:
#             inval.append(a[i])
# with open('valid.json','w') as tulis:
#     json.dump(val,tulis)
# with open('invalid.json','w') as tulis:
    json.dump(inval,tulis)
# json_to_csv('valid.json','valid.csv')
# json_to_csv('invalid.json','invalid.csv')
def moveZeros(x=list):
    for i in range(len(x)):
        for y in range(i+1,len(x)):
            if type(x[i])==bool:
                continue
            elif x[i]==0:
                x[i],x[y]=x[y],x[i]
    return x
meh=[False,True,1,0,0,'a','0']
print(moveZeros(meh))