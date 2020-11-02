import math
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
def goldbach():
    lst = []
    for i in range(1, 6000):
        if is_prime(i):
            lst.append(i)
    for odd in range(3, 5790, 2):
        flag = True
        for prime in lst:
            if odd in lst:
                flag = False
                break
            if prime < odd:
                square = (odd - prime)/2
                root = math.sqrt(square)
                if root.is_integer():
                    flag = False
                    break
        if flag == True:
            print(odd)
              
            
goldbach()
