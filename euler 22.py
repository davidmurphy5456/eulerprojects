
def alphabetize():
    from numpy import loadtxt
    lines = loadtxt(r"C:\Users\david\Downloads\eulernames.txt", dtype = str, comments="#", delimiter=",", unpack=False)
    lines.sort()
    dictt = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26 }
    lst = []
    for i in range(len(lines)):
        total = 0
        for j in list(lines[i]):
            if j == ' ' :
                pass
            elif j == '"' :
                pass
            else:
                for k, p in dictt.items():
                    if k == j:
                        total += p
        lst.append(total)
    print(lst)
    count = 1
    namescore=0
    for i in lst:
        num = i * count
        count += 1
        namescore += num
    print("total namescore: ", namescore)
alphabetize()
    
        
        
    
