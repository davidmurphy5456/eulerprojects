def abundantnum():
    lst = list(range(1,28124))
    final = []
    total2 = 0
    for i in lst:
        total = 0
        for j in range(1, i):
            if i % j == 0:
                total += j
        if total > i:
            final.append(i)
    for i in final:
        for j in final:
            num = i + j
            if num in lst:
                lst.remove(num)
    for i in lst:
        total2 += i
    print(total2)
                  
abundantnum()
        



