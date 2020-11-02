from itertools import permutations
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
def primesequence():
    for i in range(2000, 10000):
        test = set()
        if is_prime(i):
            test.add(i)
            string = str(i)
            perm = list(permutations(string[:4]))
            for j in perm:
                if '0' not in j:
                    num = int("".join(j))
                    if is_prime(num):
                        test.add(num)
            if len(test) >= 3:
                test = list(test)
                test.sort()
                for a in range(0, len(test)):
                    for b in range(a+1, len(test)):
                        diff = test[b] - test[a]
                        if (test[b] + diff) in test:
                            print(test[a], test[b], (test[b] + diff))
                    
                        
                        
primesequence()
                    
                    
            
