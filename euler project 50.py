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
def consecutiveprimesum():
    lst = []
    total = 0
    length= 0
    last = len(lst)
    large = 0
    for i in range(1000000):
        if is_prime(i):
            lst.append(i)
    for j in range(len(lst)):
        last = len(lst)
        for k in range(j+length, last):   #using editable last rather than len(lst) cuts down on excess iter.
            total = sum(lst[j:k])
            if total < 1000000:
                if total in lst:
                    length = k-j   #note j+length = k (where k is current iter.)
                                   #makes it so k now starts iter. at next largest value
                                   # ie if last length was 21, will now only take slices [j:k] > 21
                    large = total
            else:  #reduce iterations past upped bound
                last = j+1
                break
    print(large)
            
        
consecutiveprimesum()
