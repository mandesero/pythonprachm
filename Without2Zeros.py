def No_2Zero(n, k):
    t = [1, k - 1] + [0] * (n - 1)
    for i in range(2, len(t)):
        t[i] = (t[i - 1] + t[i - 2]) * (k - 1)
    return t[-1]
