def pythagoreantrip():
    for i in range(1,998):
        for j in range(1, 998):
            for k in range (1, 998):
                if (i+j+k == 1000):
                     asquare = i**2
                     bsquare = j**2
                     csquare = k**2
                     if (csquare > asquare) & (csquare > bsquare):
                         if (asquare + bsquare == csquare):
                             print(i, j, k)
pythagoreantrip()
