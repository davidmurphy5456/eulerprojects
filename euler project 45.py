import math
def is_trip(a):
    tri = (math.sqrt(8*a+1)-1)/2
    if tri.is_integer():
        return True
    return False
def is_pent(a):
    pent = (math.sqrt(24*a+1)+1)/6
    if pent.is_integer():
        return True
    return False
def tripenthex():
    num = 144
    while True:
        hecks = 2*(num**2) - num
        if is_trip(hecks) and is_pent(hecks):
            print(hecks)
            break
        num += 1
tripenthex()

    
    
    
    
    
