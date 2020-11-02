def factorialsum():
    num = 1
    total = 0
    for i in range(1,101):
        num *= i
    string = str(num)
    integer = list(map(int, string))
    for i in range(len(integer)):
        total += integer[i]
    print(total)
factorialsum()
