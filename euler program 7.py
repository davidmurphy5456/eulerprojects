def primes():
    import math
    count = 0
    value = 0
    for i in range(1, 150000):
        maxj = 0
        for j in range(2, int(math.sqrt(i))+2):
            maxj += 1
            if count == 10001:
                break
            if i % j == 0:
                break
            elif maxj == int(math.sqrt(i)):
                count += 1
                if i > value:
                    value = i
                    if count == 10001:
                        break
                if count == 10001:
                    break
                    
            
    print("count:", count, " value: ", value)
primes()
            
