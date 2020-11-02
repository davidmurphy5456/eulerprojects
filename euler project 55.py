def palindrome(nxt):
    list1 = list(str(nxt))
    length = len(list1)
    flag = False
    for j in range(0, length//2):
        if list1[j] == list1[length-(1+j)]:
            flag = True
        else:
            flag = False
            break
    return flag          

def lychrel(i):
    total = 0
    lst = set()
    test = list(str(i))
    test2 = test
    test2.reverse()
    for j in range(len(test2)):
        test2[j] = int(test2[j])*(10**(len(test2)-(j+1)))
        total += test2[j]
    nxt = i + total
    return nxt
def main():
    lst = []
    solution = []
    count = 0
    for i in range(10, 10001):
        flag = False
        nxt = lychrel(i)
        for j in range(50):
            if palindrome(nxt):
                lst.append((i, j+1, nxt))
                flag = True
                break
            else:
                nxt = lychrel(nxt)
        if flag == False:
            solution.append(i)
            count += 1
    print(count)
main()
        
        
    
