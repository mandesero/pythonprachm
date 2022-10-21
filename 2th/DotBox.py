def calculate_volume():
    dots = []
    while buf := input():
        dots.append(tuple(eval(buf)))
    x = sorted([elem[0] for elem in dots])
    y = sorted([elem[1] for elem in dots])
    z = sorted([elem[2] for elem in dots])
    print((x[-1] - x[0]) * (y[-1] - y[0]) * (z[-1] - z[0]))


def main():
    calculate_volume()


if __name__ == '__main__':
    main()
