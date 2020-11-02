def listsquares(a, b):
    lst = set()
    for i in range(a, b+1):
        for j in range(a, b+1):
            num = i**j
            lst.add(num)
    new = sorted(lst)
    length = len(new)
    return length

            
        
