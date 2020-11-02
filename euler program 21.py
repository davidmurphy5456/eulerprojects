def amicable():
    lst = list(range(10,10001))
    final = []
    total3 = 0
    for i in lst:
        total = 0
        for j in range(1, i):
            if i % j == 0:
                total += j
        if total > i:
            total2 = 0
            for k in range(1, total):
                if total % k == 0:
                    total2 += k
            if total2 == i:
                final.append(i)
                final.append(total)
                total3 += total + i
    print(total3)
    print(final)
amicable()
