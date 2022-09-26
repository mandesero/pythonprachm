from math import sqrt


def solve(x):
    ans = []
    t = int(sqrt(x))
    for i in range(t + 1):
        b = i * i
        for j in range(i, int(sqrt(x - b)) + 1):
            for k in range(j, int(sqrt(x - i * i - j * j)) + 1):
                for n in range(int(sqrt(x - i * i - j * j - k * k)), k - 1, -1):
                    s = b + j * j + k * k + n * n
                    if x == s:
                        if not sorted([i, j, k, n], key=lambda q: -q) in ans:
                            ans.append(sorted([i, j, k, n], key=lambda q: -q))
                        break
                    elif s < x:
                        break
    for arr in sorted(ans):
        print(*arr)


def main():
    n = int(input())
    solve(n)


if __name__ == '__main__':
    main()