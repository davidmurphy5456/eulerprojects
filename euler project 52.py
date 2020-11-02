from itertools import permutations
def multiperm():
    for i in range (100000, 166668):  #166668
        lst= []
        perm = list(permutations(str(i)))
        for j in perm:
            val = int("".join(j))
            lst.append(val)
        if (2*i) in lst:
            if (3*i) in lst:
                if (4*i) in lst:
                    if (5*i) in lst:
                        if (6*i) in lst:
                            print(i)
multiperm()
        
