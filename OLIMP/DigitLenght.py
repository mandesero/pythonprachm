def find_range(S):
    num_digits = lambda n: (10 ** n * (9 * n - 1) + 1) // 9 + 1

    l_t, t = 0, 0

    if S <= 10:
        return S, 0, S - 1

    for n in range(1, 19):
        l_t = t
        if (t := num_digits(n)) >= S:
            if t == S:
                t = 10 ** n - 1
                return t + 1, 0, t
            break

    t = S - l_t

    if (S - l_t) % n == 0:
        t = 10 ** (n - 1) + (S - l_t) // n - 1
        return t + 1, 0, t

    T = (S - l_t) % n  # не хватает
    L = 0
    R = 10 ** (n - 1) - 1 + (S - l_t) // n

    while T != 0:
        T += len(str(L))
        L += 1
        while T > 0:
            T -= n
            R += 1
    return R - L + 1, L, R


if __name__ == '__main__':
    print(*find_range(eval(input())))
