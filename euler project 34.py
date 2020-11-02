def factorialsum():
    for i in range(140, 3000000): #9! is 362880 so by 3mil, the extra digit outstrips the growth
        total2 = 0
        string = str(i)
        lst = list(string)
        for j in lst:
            total = 1
            j = int(j)
            for k in range(1,j+1):
                total *= k
            total2 += total
        if i == total2:
            print(i)
factorialsum()
