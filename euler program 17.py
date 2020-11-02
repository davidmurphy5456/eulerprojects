import num2word
import numpy as np
def numberword():
    lst = []
    count = 0
    for i in range (1, 1001):
        word = num2word.word(i)
        temp = list(word)
        lst.append(temp)
    full = np.concatenate(lst, axis = None)
    for i in range(len(full)):
        if (full[i] == ' ') | (full[i] == '-'):
            pass
        else:
            count += 1
    andcount = 3* 891
    total = count + andcount
    print(total)
numberword()


    
