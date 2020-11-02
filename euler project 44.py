def summationX():
    total = 1
    lst= [1]
    for i in range(1, 2400):  #brute forced max =/
        total += (3*i +1)
        lst.append(total)
    return lst
def pentagon(a):
    lst = a
    for i in lst:
        for j in lst:
            if (j- i) in lst:
                if (i +j) in lst:
                    print(i, j)

    
