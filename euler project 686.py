import math
def numgen():
    i = 90
    rank = 0
    previ=0
    lower = math.log(1.23, 10)  #smaller numbers, if value >lower but <upper,
                                #that means 2**i started with 123
    upper = math.log(1.24, 10)
    while rank < 678910:
        num = math.log(2,10)*i
        diff = (num - int(num))   #smaller numbers to work with
        if diff >= upper:        #three possible i+= values: 196, 289(93+196), 485(196+196+93)
            i += 93              #for +485 iter., diff will be both above and below range. ie 196(from else) + 93(from above) + 196(from below)
        elif diff < lower:
            i+= 196
        else:
            rank +=1
            previ=i
            i+=196
            
    print(diff, rank, previ)
numgen()
