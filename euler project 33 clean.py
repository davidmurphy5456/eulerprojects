def digitcancel():
    total = 1
    for i in range(10,100):
        for j in range(10,100):
            if i/j >= 1:
                continue
            if (i % 10 == 0) & (j % 10 == 0):
                continue
            if (j % 10 == 0):
                continue
            num = i
            denom = j
            test = num/denom
            top = list(str(num))
            bottom = list(str(denom))
            top.sort()
            bottom.sort()
            for k in top:
                for l in bottom:
                    if len(bottom) == 2:
                        if k == l:
                            top.remove(k)
                            bottom.remove(l)
                            top[0] = int(top[0])
                            bottom[0] = int(bottom[0])
                            quotient = top[0]/bottom[0]
                            if quotient == test:
                                print("numerator", num, "denominator", denom)
                                total *= test
    print(total)
                          
            
digitcancel()
                        
            
