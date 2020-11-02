
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
def circularprime():
    answer= []
    for i in range(1, 1000000):
        if is_prime(i) == True:
            container = []
            lst = list(str(i))
            container.append(i)
            for j in range(1, len(lst)):
                lst += [lst.pop(0)]
                string = "".join(lst)
                num = int(string)
                if is_prime(num) == True:
                    container.append(num)
                else:
                    break
            if len(container) == len(lst):
                answer.append(i)
    print(answer)
    print(len(answer))
circularprime()
                    
                
