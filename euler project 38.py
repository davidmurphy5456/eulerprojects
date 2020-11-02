def pandigital():
    big = 0
    val = 0
    for i in range(1, 10000): # future reduction: only test 90-98, 900-987, 9000-9876
        test = ''
        num = 1
        while len(test) < 9:
            test += str(num* i)
            num += 1
            if (len(test) == 9) and (len(set(test))==9) and ('0' not in test):
                if int(test) > big :
                    big = int(test)
                    val = i
    print(big)
    print(val)
                
pandigital()
        
