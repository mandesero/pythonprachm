from math import sqrt


def solve_eq():
    a, b, c = eval(input())
    if (a, b, c) == (0, 0, 0):
        print(-1)
        return
    if a == 0:
        print(-c / b if b != 0 else 0)
        return
    d = b ** 2 - 4 * a * c
    if d > 0:
        print(*sorted([(-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)]))
        return
    elif d == 0:
        print(-b / (2 * a))
        return
    print(0)


def main():
    solve_eq()


if __name__ == '__main__':
    main()
