def maxlength():
    lim = 1000
    maxlength=0
    max_d= 1
    for i in range(1, lim):
        q = []
        val = 1
        len_recur = 0
        while val not in q:
            if not val:  #if val is 0, empty, false
                break
            len_recur += 1
            q.append(val)
            val = (val% i) * 10  #returns val*10 if val < i
        if not val:
            continue
        len_recur -= q.index(val)  # subtract leading digits

        if len_recur > maxlength :
            maxlength = len_recur
            max_d = i
    print(max_d)
    print(q)
    print(maxlength)
maxlength()
	


