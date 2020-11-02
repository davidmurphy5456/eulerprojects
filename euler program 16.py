def largedigitsum():
    num = str(2**1000)
    large = list(map(int, num))
    total = sum(large)
    print(total)
largedigitsum()
