import math
def righttriangle():
    solution = set()
    for m in range(1, 1001):
        lst = []
        answer = set()
        for i in range(1, 500):
            for j in range(i, 500):
                ksquare = i**2 + j**2
                k = math.sqrt(ksquare)
                if (i + j + k) == m:
                    if k not in lst:
                        answer.add((i, j, k))
                        lst.append(k)
                if len(answer) >= len(solution):
                    biggest = m
                    solution = answer
    print(biggest)
righttriangle()
                    
                    
                    
                
                
