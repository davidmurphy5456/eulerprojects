test = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
product = set() #collects products that satisfy pandigital
for i in range(9):  #tests values with multicand digit = 1
    for j in range(1100, 9999): # tests multiplier with digit = 4
        lst = []
        num = i*j
        string = list(str(num))
        a = list(str(i))
        b = list(str(j))
        for k in a:
            lst.append(k)
        for l in b:
            lst.append(l)
        for p in string:
            lst.append(p)
        lst.sort()
        if lst == test:
            product.add(num)
for i in range(9, 99): #tests values with multicand digit = 2
    for j in range(100, 999): #tests multiplier with digit = 3
        lst = []
        num = i*j
        string = list(str(num)) #line plus two below convert into list of digits
        a = list(str(i))
        b = list(str(j))
        for k in a:
            lst.append(k)
        for l in b:
            lst.append(l)
        for p in string:
            lst.append(p)
        lst.sort()
        if lst == test:  #tests for exact match to set containing 1-9
            product.add(num) #adds good values to collection set
print(sum(product)) #adds all products produced by pandigital constraint


