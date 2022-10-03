def maxfun(seq, *args):
    return args[(tmp := [sum(func(i) for i in seq) for func in args]).index(max(tmp))]