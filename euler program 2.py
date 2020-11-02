def evenfibonacci():
    total = 0
    first = 1
    sec = 2
    evencount = 2
    fullcount = 1
    while sec < 4000000:
        if total % 2 == 0:
            evencount += total
        total = first + sec
        first = sec
        fullcount += sec
        sec = total
        
    print("total:", total)
    print("evencount:", evencount)
    print("fullcount:", fullcount)
evenfibonacci()
        
