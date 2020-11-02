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
def pandigitalprime():
    big = 0
    val = 0
    num = '123456789'
    flag = True    #while loop condition
    digit = 9    #allows testing n-length pandigitals
    while flag:
        perm = permutations(num[:digit])  #creates all permutations of 123456789 up to digit
        perm = list(perm)[::-1]          #creates reverse order list of permutations
        for i in perm:
            if int(i[digit-1]) % 2 != 0:   #tests if last digit is even
                num2 = int("".join(i))
                if is_prime(num2) == True:   #if last digit was odd, runs is_prime on integer of i
                    if num2 > big :
                        big = num2
                        flag = False    #if this value is largest, ends while loop on next iteration
                        break           #ends for loop running through permutations
        digit -= 1
    print(big)
pandigitalprime()
