def tickets(peopleInLine): # [25, 25, 50, 50, 100]
    list = [] # [25,25,50,50]
    money = {25:0, 50:0, 100:0}
           #{25:0, 50:2, 100:0}

    for j in peopleInLine:
        if j == 25:
            money[25] += 1
            list.append(j)
        elif j == 50 and money[25] > 0:
            money[25] -= 1
            money[50] += 1
            list.append(j)
        elif j == 50 and money[25] == 0:
            print('NO')
            break
        elif j == 100 and money[50] >= 1 and money[25] >= 1:
            money[100] += 1
            money[50] -= 1
            money[25] -= 1
            list.append(j)      
        elif j == 100 and money[25] >= 3:
            money[100] += 1
            money[25] -= 3
            list.append(j)
        else:
            print('NO')
            break            
    
    if len(list) == len(peopleInLine):
        print('YES')

peopleInLine = [25, 25, 50, 50, 100]              
tickets(peopleInLine)

RowSumOddNumbers
def rowSumOddNumbers(n) : # 10
    numbers  = [] # => [[1], [3,5], [7,9,11], ....., [91,93,95,97,101,103,105,107,109]]
    nilai = 1 # => 3 => 5 => 7 => 9 => 11 => 13

    # bikin list nya dulu
    for i in range(1, n+1) : # [1,2,3,4,5,6,7,8,9,10] ; i=1 ; i=2 ; i=3
        temp = [] 
        # [7, 9, 11]
        for j in range(i) : # [0,1,2]
            temp.append(nilai) 
            nilai += 2
        numbers.append(temp)
    print(numbers)
    
    #ngeprint segitiga
    z = ''                      # [0,1,2,3,4,5,6,7,8,9]
    for num, i in zip(numbers, range(len(numbers))) : # [([1], 0), ([3,5], 1), ([7,9,11], 2), ...... ([91,93,95,...,109], 9)]
        for j in range(n-i) : # [0,1,2,3,4,5,6,7,8]
            z += '**'
        for k in num : # [1] ; k=1 ; [3,5]
            #ljust berfungsi kayak padding, nambahin spasi di sebelah kanan huruf (jumlahnya sampai 4)
            # z += str(k).ljust(4)
            if k < 10:
                z += str(k) + ('*'*3)
            elif k < 100:
                z += str(k) + ('*'*2)
            else:
                z += str(k) + ('*'*1)
        z += '\n' 
    print(z)

    sum_row = ''
    
    for num in numbers[-1]: # [91,93,95,97,101,103,105,107,109]
        if num == numbers[-1][-1]: # 109 == 109
            sum_row += str(num)
        else:    
            sum_row += str(num)
            sum_row += ' + '
    sum_row += ' = {}'.format(sum(numbers[-1]))       
    
    if sum(numbers[-1]) == 1:
        print(1)
    else:
        print(sum_row)    


# rowSumOddNumbers(1)
# rowSumOddNumbers(2)
rowSumOddNumbers(2)