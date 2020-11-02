def sumdiff():
    totalsquare = 0
    total = 0
    for i in range(1, 101):
        totalsquare += i**2
        total += i
    difference = total**2 - totalsquare
    print(difference)
sumdiff()
