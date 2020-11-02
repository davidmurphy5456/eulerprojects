def smallfactor():
    max2 = 0
    count2 = 1
    count3 = 1
    my_list = set()
    primelist = set()
    factor2= set()
    for i in range(1, 21):
        for j in range(2,i):
            if i % j == 0:
                my_list.add(i)

    print(my_list)
    for i in range(1, 20):
        if i in my_list:
            pass
        else:
            primelist.add(i)
    print(primelist)
    for i in my_list:
        if (i % 4 == 0):
            count2 = 2
            if i % 8 == 0:
                count2 = 3
                if i % 16 == 0:
                    count2 = 4
                    if count2 > max2:
                        max2 = count2
    for i in my_list:
        if i % 9 == 0:
            if i % 2 != 0:
                count3 += 1
            
    product = 2 ** max2 * 3 ** count3 * 5  * 7 * 11 * 13 * 17 * 19
    print(max2, count3)
    print(product)
smallfactor()
