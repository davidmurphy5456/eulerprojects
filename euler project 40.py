def champernown():
    count = 0
    lst = []
    for i in range(1, 1000000):
        string = str(i)
        for j in range(len(string)):
            count += 1
            if count == 1:
                lst.append(string[j])
            if (count == 10):
                lst.append(string[j])
            if (count == 100):
                lst.append(string[j])
            if (count == 1000):
                lst.append(string[j])
            if (count == 10000):
                lst.append(string[j])
            if (count == 100000):
                lst.append(string[j])
            if (count == 1000000):
                lst.append(string[j])
    print(lst)
champernown()
            
