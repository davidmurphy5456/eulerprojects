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

def spiralprime():
    total = 0
    count = 0
    i = 3
    flag = True
    while flag == True:
        for j in range(3, -1, -1):
            val = (i**2 - j*(i-1))
            if is_prime(val):
                count += 1
                total +=1
            else:
                total+=1
        if (count/total) <= 0.1:
            print(i)
            flag = False
        i += 2
spiralprime()
    
