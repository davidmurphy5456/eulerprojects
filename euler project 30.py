def fifthpower():
    lst =[]
    for i in range(30, 355000): # sum of digits^5 of 999,999 < 355000,
        total = 0
        string = str(i)
        temp = list(string)
        for j in temp:
            num = int(j)
            total += num**5
        if total == i:
            lst.append(i)
    print(lst)
fifthpower()
