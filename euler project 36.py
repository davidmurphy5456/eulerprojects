def palindrome():
    total = set()
    for i in range(1, 1000001):
        list1 = list(str(i))
        if len(list1) > 1:
            length = len(list1)
            for j in range(0, length//2):
                if list1[j] == list1[length-(1+j)]:
                    if ((j+1) == (length-(1+j))) | ((j+2) == (length-(1+j))):
                        total.add(i)
                else:
                    break
        else:
            total.add(i)
    lst = list(total)
    return lst 
def palindromebinary(a):
    final = set()
    for k in a:
        binary = bin(k)
        list2 = list(str(binary))
        del list2[0:2]
        if len(list2) > 1:
            length = len(list2)
            for m in range(0, length//2):
                if list2[m] == list2[length-(1+m)]:
                    if ((m+1) == (length-(1+m))) | ((m+2) == (length-(1+m))):
                        final.add(k)
                else:
                    break
        else:
            final.add(k)
        
    full = list(final)
    full.sort()
    count = 0
    for n in full:
        count += n
    print(full)
    print(count)
palindromebinary(palindrome())
                    
            
                
                    
                
