from numpy import loadtxt
from collections import Counter

lines = loadtxt(r"C:\Users\david\Downloads\poker.txt", dtype = str, comments="#", delimiter=",", unpack=False)
dictt = {"T":10, "J":11, "Q":12, "K":13, "A":14}
def hands(test):
    hand1 = []
    hand2 = []
    for j in range(0,15,3):
        val = test[j]
        if val in dictt.keys():
            for k,p in dictt.items():
                if k == val:
                    hand1.append(p)
        else: 
            num = int(val)
            hand1.append(num)
    for n in range(15, 29, 3):
        val = test[n]
        if val in dictt.keys():
            for k,p in dictt.items():
                if k == val:
                    hand2.append(p)
        else:
            num = int(val)
            hand2.append(num)
    hand1.sort()
    hand2.sort()
    return hand1, hand2
def suit(test):
    suit1 = set()
    suit2 = set()
    for j in range(1, 14, 3):
        val = test[j]
        suit1.add(val)
    for n in range(16, 29, 3):
        val = test[n]
        suit2.add(val)
    return suit1, suit2
def highcard(hand1, hand2):
    if (hand1[4] > hand2[4]):
        return True
    else:
        return False
def pairs(hand1, hand2):
    a = dict(Counter(hand1))
    b = dict(Counter(hand2))
    count1 = []
    count2 = []
    place = [k for k,v in a.items() if v == 2]
    holder = [k for k,v in b.items() if v == 2]
    
    for i in place:
        count1.append(int(i))
    for j in holder:
        count2.append(int(j))
    count1.sort()
    count2.sort()
    if len(count1) > len(count2):
        return hand1
    elif (len(count1) == len(count2)) & (len(count1) > 0):
        if count1[-1] > count2[-1]:
            return hand1
        elif count2[-1] > count1[-1]:
            return hand2
    elif len(count2) > len(count1):
        return hand2
    elif len(count1)== 0:
        return False
    
def triple(hand1, hand2):
    a = dict(Counter(hand1))
    b = dict(Counter(hand2))
    count1 = []
    count2 = []
    place = [k for k,v in a.items() if v == 3]
    holder = [k for k,v in b.items() if v == 3]
    
    for i in place:
        count1.append(int(i))
    for j in holder:
        count2.append(int(j))
    count1.sort()
    count2.sort()
    if len(count1) > len(count2):
        return hand1
    elif (len(count1) == len(count2)) and (len(count1) > 0):
        if count1[-1] > count2[-1]:
            return hand1
        elif count2[-1] > count1[-1]:
            return hand2
    elif len(count2) > len(count1):
        return hand2
    elif len(count1)== 0:
        return False

def straight(hand1, hand2):
    count1 = 0
    count2 = 0
    for i in range(0,4):
        if (int(hand1[i])+1) == int(hand1[i+1]):
            count1 +=1
        if (int(hand2[i])+1) == int(hand2[i+1]):
            count2 +=1
    if count1 == 4:
        if count2 != 4:
            return hand1
        else:
            return False
    if count2 == 4:
        if count1 != 4:
            return hand2
def fullhouse(hand1, hand2):
    a = dict(Counter(hand1))
    b = dict(Counter(hand2))
    counttrip1 = []
    counttrip2 = []
    place = [k for k,v in a.items() if v == 3]
    holder = [k for k,v in b.items() if v == 3]
    
    for i in place:
        counttrip1.append(int(i))
    for j in holder:
        counttrip2.append(int(j))
    
    countpair1 = []
    countpair2 = []
    test1 = [x for x,g in a.items() if g == 2]
    test2 = [x for x,g in b.items() if g == 2]
    
    for m in test1:
        countpair1.append(int(m))
    for n in test2:
        countpair2.append(int(n))
    countpair1.sort()
    countpair2.sort()
    if len(counttrip1) == 1:
        if len(counttrip2) == 0:
            if len(countpair1) == 1:
                return hand1
        elif len(counttrip2) == 1:
            if (len(countpair1) ==1) & (len(countpair2)==1):
                if counttrip1[0] > counttrip2[0]:
                    return hand1
                elif counttrip2[0] > counttrip1[0]:
                    return hand2
                    
    elif len(counttrip2) == 1:
        if len(counttrip1) == 0:
            if len(countpair2) == 1:
                return hand2
    else:
        return False
def four(hand1, hand2):
    a = dict(Counter(hand1))
    b = dict(Counter(hand2))
    count1 = []
    count2 = []
    place = [k for k,v in a.items() if v == 4]
    holder = [k for k,v in b.items() if v == 4]
    
    for i in place:
        count1.append(int(i))
    for j in holder:
        count2.append(int(j))
    if len(count1) > len(count2):
        return hand1
    elif len(count2) > len(count1):
        return hand2
    elif (len(count1) == len(count2)) & (len(count1) > 0):
        if count1[0] > count2[0]:
            return hand1
        elif count2[0] > count1[0]:
            return hand2
        elif count2[0] > count2[0]:
            return hand2
    elif len(count1)== 0:
        return False

def flush(suit):
    if len(suit) == 1:
        return True
    else:
        return False
def straightflush(hand1, hand2, suit1, suit2):
    if straight(hand1, hand2) == hand1:
        if flush(suit1):
            return hand1
    elif straight(hand1, hand2) == hand2:
        if flush(suit2):
            return hand2
    else:
        return False
def royalflush(hand1, hand2, suit1, suit2):
    if hand1[0] == 10:
        if straight(hand1, hand2) == hand1:
            if flush(suit1) == True:
                return hand1
    elif hand2[0] == 10:
        if straight(hand1, hand2) == hand2:
            if flush(suit2) == True:
                return hand2
    else:
        return False

def poker():
    counthigh = 0
    countpair = 0
    counttrip = 0
    countstraight = 0
    countfull = 0
    countfour = 0
    countsf = 0
    countflush = 0
    countrf = 0
    for i in range(0, 1000):
        test = lines[i]
        test.split()
        hand1, hand2 = hands(test)
        suit1, suit2 = suit(test)
        if royalflush(hand1, hand2, suit1, suit2) == hand1:
            countrf += 1
            print("royalflush", hand1, hand2)
        elif royalflush(hand1, hand2, suit1, suit2) == hand2:
            pass
        elif straightflush(hand1, hand2, suit1, suit2) == hand1:
            countsf += 1
            print("straightflush", hand1, hand2)
        elif straightflush(hand1, hand2, suit1, suit2) == hand2:
            pass
        elif four(hand1, hand2) == hand1:
            countfour +=1
            print("fourkind", hand1, hand2)
        elif four(hand1, hand2) == hand2:
            pass
        elif fullhouse(hand1, hand2) == hand1:
            countfull += 1
            print("fullhouse", hand1, hand2)
        elif fullhouse(hand1, hand2) == hand2:
            pass
        elif flush(suit1) == True:
            if flush(suit2) == False:
                countflush +=1
                print("flush", hand1, hand2)
        elif flush(suit2) == True:
            if flush(suit1) == False:
                pass
        elif straight(hand1, hand2) == hand1:
            countstraight +=1
            print("straight", hand1, hand2)
        elif straight(hand1, hand2) == hand2:
            pass
        elif triple(hand1, hand2)== hand1:
            counttrip += 1
            print( "trip", hand1, hand2)
        elif triple(hand1,hand2) == hand2:
            pass
        elif pairs(hand1, hand2)== hand1:
            countpair += 1
            print("pair", hand1, hand2)
        elif pairs(hand1, hand2) == hand2:
            pass
        elif highcard(hand1,hand2):
            counthigh += 1
            print("high card", hand1, hand2)
    print("countrf", countrf)
    print("countflush", countflush)
    print("countsf", countsf)
    print("countstraight", countstraight)
    print("countfour", countfour)
    print("counttrip", counttrip)
    print("counthigh", counthigh)
    print("countpair", countpair)
    print("countfull", countfull)
    fullcount = counthigh + countpair + counttrip + countstraight + countfull + countfour + countsf + countflush + countrf
    print(fullcount)
poker()
