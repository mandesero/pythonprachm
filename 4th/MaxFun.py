def maxfun(seq, *args):
    tmp = [sum(func(i) for i in seq) for func in args]
    m = tmp[0]
    for i, elem in enumerate(tmp):
    	if elem >= m:
    	    ind = i
    	    m = elem
    return args[ind]

