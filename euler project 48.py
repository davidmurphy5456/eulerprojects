def stupidbigsum():
    total = 0
    for i in range(1, 1001):
        total += (i**i)
    answer = str(total)[-10:]
    print(answer)
stupidbigsum()
