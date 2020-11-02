def primes():
    import math
    count = 0
    value = 0
    total = 5
    for i in range(5, 2000000, 2):
        maxj = 0
        for j in range(2, int(math.sqrt(i))+4):
            maxj += 1
            if i % j == 0:
                break
            elif maxj == int(math.sqrt(i)):
                total += i
                    
            
    print(" total: ", total)
primes()
            
