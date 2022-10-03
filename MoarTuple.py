def moar(a, b, n):
    return len([elem for elem in a if elem % n == 0]) > len([elem for elem in b if elem % n == 0])
