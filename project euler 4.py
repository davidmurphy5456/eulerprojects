def palindrome():
    big = 0
    for i in range(400,1000):
        for j in range(400, 1000):
            num = i * j
            list1 = list(str(num))
            if len(list1) == 6:
                if list1[0] == list1[-1]:
                    if list1[1] == list1[-2]:
                        if list1[2] == list1[-3]:
                            if num > big:
                                big = num
    print(big)
palindrome()
