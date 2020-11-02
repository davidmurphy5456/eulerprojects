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
def truncprime():
    answer = []
    solution = []
    total = 0
    for i in range(10, 1000000):
        if is_prime(i) == True:
            container = []
            lst = list(str(i))
            copy = list(str(i))
            container.append(i)
            for j in range(1, len(lst)):
                del copy[0]
                num = "".join(copy)
                num2 = int(num)
                if is_prime(num2) == True:
                    container.append(num2)
                else:
                    break
            if len(container) == len(lst):
                answer.append(i)
        
    for k in answer:
        container2 = []
        lst2 = list(str(k))
        copy2 = list(str(k))
        container2.append(k)
        for m in range(1, len(lst2)):
            del copy2[-1]
            num = "".join(copy2)
            num2 = int(num)
            if is_prime(num2) == True:
                container2.append(num2)
            else:
                break
        if len(container2) == len(lst2):
            solution.append(k)
    for n in solution:
        total += n
    print(total)
            
truncprime()
                
