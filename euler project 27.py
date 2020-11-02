
def is_prime(n):
    if n==1:
        return False
    elif n==2 or n==3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    elif (n < 0):
        return False
    elif all(n % i != 0 for i in range(2, (int(n**0.5)+2))):
        return True
    else:
        return False
def seive(n):
    primes=[]
    neg = []
    for i in range(n):
        if is_prime(i)==True:
            primes.append(i)
            i *= -1
            neg.append(i)
    neg.reverse()
    for i in primes:
        neg.append(i)
    full = neg
    return (full, primes, n)
def quadraaticprimes(a):
    full, primes, n = a
    big = 0
    for i in full:
        for j in primes:
            total = 0
            for k in range(0, n):
                if is_prime(k**2 + i*k + j) == True:
                    total += 1
            if total > big:
                big = total
                f = i
                g = j
    print(big, "a: ", f, "b:", g)
            
            
            
        

        
            
