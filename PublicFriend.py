from collections import defaultdict

a = defaultdict(set)
while (buff := eval(input())) != (0, 0):
    if buff[0] != buff[1]:
        a[buff[0]].add(buff[1])
        a[buff[1]].add(buff[0])

print(*sorted([key for key, val in a.items() if len(val) == len(a) - 1]))
