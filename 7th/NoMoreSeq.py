def nomore(seq):
    for elem in seq:
        for val in [x for x in seq if x <= elem]:
            yield val
