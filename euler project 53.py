import math
def combination():
    count = 0
    for n in range(22,101):
        numer = math.factorial(n)
        r = n//2
        denom = (math.factorial(n-r))*(math.factorial(r))
        if ((numer/denom) > 1000000) :
            for i in range(0, n+1):
                denom = (math.factorial(n-i))*(math.factorial(i))
                val = (numer/denom)
                if val > 1000000:
                    count += 1
    print(count)
combination()
        
