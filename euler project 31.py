def coincount():
    count = 1 # added 1 for case with 1 2-pound coin
    for a in range(0, 3): #number of 1-pound coins
        for b in range(0, int((200-100*a)/50+1)): # number of 50-pence coins; denom = coinvalue
            for c in range(0, int((200-100*a - 50*b)/20+1)):
                for d in range(0, int((200-100*a - 50*b - 20*c)/10 + 1)):
                    for e in range(0, int((200-100*a - 50*b - 20*c - 10*d)/5 +1)):
                        for f in range(0, int((200-100*a - 50*b-20*c- 10*d - 5*e)/2 +1)):
                            count +=1
    return count
