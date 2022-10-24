from decimal import *
from functools import lru_cache

def PiGen():
    @lru_cache
    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f
    getcontext().prec = 10000
    a = Decimal(426880) * Decimal(10005).sqrt()
    sm = Decimal(0)
    k = 0
    while True:

        sm += Decimal(factorial(6 * k) * (13591409 + 545140134 * k)) / Decimal(
            (factorial(3 * k) * (factorial(k) ** 3) * (-262537412640768000) ** k)
        )

        k += 1
        yield a/sm
