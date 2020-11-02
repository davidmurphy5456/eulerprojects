def bounds():
    lower = 1020304050607080900
    upper = 1929394959697989900
    rootlow = int(lower**.5)
    rootup= int(upper**.5)
    print("lower", rootlow, "upper", rootup)
def testrun():
    for i in range(1389000000, 1389026623):  #brute forced lowerbound for simplicity
        num = i**2
        lst = list(str(num))
        if (lst[0]=="1") & (lst[2]=="2") & (lst[4]=="3") & (lst[6]=="4") & (lst[8]=="5") & (lst[14]=="8") & (lst[16]=="9"):
            print(num, i)
testrun()     
