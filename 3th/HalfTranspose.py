def transprose45(arr):
    for i in range(len(arr)):
        print(*[arr[i][j] for j in range(i + 1)] + [arr[j][i] for j in range(i - 1, -1, -1)], sep=',')


def main():
    arr = []
    buf = input()
    arr.append(eval(buf))
    for i in range(len(arr[0]) - 1):
        arr.append(eval(input()))
    transprose45(arr)


if __name__ == '__main__':
    main()
