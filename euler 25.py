import math
def fibonaci():
    total=2
    first = 1
    sec = 1
    fib = 0
    digits = 1
    while digits < 1000:
        fib = first + sec
        first = sec
        sec = fib
        total += 1
        digits = int(math.log10(fib)+1)
    print(total)
fibonaci()
        
        
