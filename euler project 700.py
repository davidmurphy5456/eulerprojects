def eulercoin():
    quotient= 258162
    val = 1504170715041707
    test = 4503599627370517
    lst = [val]
    for i in range(20500000000, 3460000000000000):
        num = val * i
        q = num % test
        if q < quotient:
            lst.append(q)
            quotient = q
            #marker = i
    print(lst)
    #print(marker)
eulercoin()
