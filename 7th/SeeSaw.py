def seesaw(seq):
    seq = list(seq)
    odd = [i for i in seq if i % 2 != 0]
    even = [i for i in seq if i % 2 == 0]
    for i in range(min(len(odd), len(even))):
        yield even[i]
        yield odd[i]

    for j in range(i + 1, len(odd)):
        yield odd[j]

    for j in range(i + 1, len(even)):
        yield even[j]
