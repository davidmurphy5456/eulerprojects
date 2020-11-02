def spiralsum(n):
    total = 1
    for i in range(n, 1, -2):
        for j in range(0, 4):
            total += (i**2 - j*(i-1))
    return total
spiralsum(25)

    
