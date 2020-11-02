def collatz():
    i = 1
    largest = 1
    while i < 1000000:
        count = 2
        if i % 2 == 0:
            n = i/2
            while n > 1:
                if n % 2 == 0:
                    n= n/2
                    count += 1
                else:
                    n= 3*n + 1
                    count += 1
            if count > largest:
                largest = count
                term = i
            i += 1
        else:
            n = 3*i + 1
            while n > 1:
                if n % 2 == 0:
                    n= n/2
                    count += 1
                else:
                    n= 3*n + 1
                    count += 1
            if count > largest:
                largest = count
                term = i
            i += 1
    print("sequence length: ", largest,"  ith term: ", term)
collatz()
