from sympy.ntheory import factorint
def factors():
    answer = []
    for num in range(134000, 135000):
        lst =[]
        test = factorint(num)
        for i in test.keys():
            lst.append(i)
        if len(lst) == 4:
            answer.append(num)
    print(answer)
    for j in answer:
        if (j+1) in answer:
            if (j+2) in answer:
                if (j+3) in answer:
                    print(j)
factors()

            
            
            
