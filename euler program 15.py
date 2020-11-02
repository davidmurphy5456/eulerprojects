def latticepaths():
    i = 40
    j = 20
    num = 1
    denom = 1
    while i > 1:
        num *= i
        i -= 1
    while j > 1:
        denom *= j
        j -= 1
    denomsquare= denom**2
    total = num/ denomsquare
    print(total)
latticepaths()
