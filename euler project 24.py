from itertools import permutations
def lexpermutation():
    num = list(permutations('0123456789'))
    num = ("".join(x) for x in num)
    num = list(map(int, num))
    print(num[999999])
lexpermutation()
