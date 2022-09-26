def execute_conv(conv):
    belt = []
    for elem in conv:
        if type(elem) is tuple:
            belt.extend(elem)
        elif type(elem) is int:
            if elem > len(belt):
                break
            else:
                print(tuple(belt[: elem]))
                belt = belt[elem:]


def main():
    execute_conv(eval(input()))


if __name__ == '__main__':
    main()
