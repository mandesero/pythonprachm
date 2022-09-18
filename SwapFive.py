def swap_five():
    x = int(input())
    n, d = 1, 10 * x - 1
    while True:
        if (x * (10 ** n - 1)) % d == 0:
            return (x * (10 ** n - 1)) // d
        n += 1


def main():
    print(swap_five())


if __name__ == '__main__':
    main()
