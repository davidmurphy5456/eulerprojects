from itertools import permutations
def pandigital():
    total = 0
    lst = []
    num = '0123456789'
    perm = list(permutations(num[:10]))
    for i in perm:
        num1 = int("".join(i[1:4]))
        if num1 % 2== 0:
            num2 = int("".join(i[2:5]))
            if num2 % 3 == 0:
                num3 = int("".join(i[3:6]))
                if num3 % 5 == 0:
                    num4 = int("".join(i[4:7]))
                    if num4 % 7 == 0:
                        num5 = int("".join(i[5:8]))
                        if num5 % 11 == 0:
                            num6 = int("".join(i[6:9]))
                            if num6 % 13 == 0:
                                num7 = int("".join(i[7:10]))
                                if num7 % 17 == 0:
                                    lst.append(i)
                                    total += int("".join(i))
    print(total)

                                    
pandigital()                        
