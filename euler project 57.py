def root2():
    num = 3
    denom = 2
    count = 0
    for i in range(1,501):
        lst = list(str(num))
        lst2 = list(str(denom))
        if len(lst) > len(lst2):
            count +=1
        newnum = num + denom*2
        newdenom = denom + num
        newlst = list(str(newnum))
        newlst2 = list(str(newdenom))
        if len(newlst) > len(newlst2):
            count+=1
        num = newnum + newdenom*2
        denom = newdenom + newnum
    print(count)
root2()
    
