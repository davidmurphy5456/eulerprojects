def primefactor():
    for i in range(1, 775147):
        if 600851475143 % i == 0:
            print(i)
            for j in range(2, i-1):
                if i % j == 0:
                    print(i, "is not prime")
                    break
                
primefactor()
