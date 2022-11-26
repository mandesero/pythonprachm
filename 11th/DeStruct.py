import sys

a = sys.stdin.read().strip()

import base64

f = base64.b85decode(a)

head = f[:f.find(0)]
body = f[f.find(0) + 1:]

heads = [int.from_bytes(head[i: i + 1], byteorder='big', signed=True) for i in range(len(head))]
segm_size = sum(abs(i) for i in heads)

p = [body[i * segm_size: (i + 1) * segm_size] for i in range(len(body) // segm_size + 1)]
k = 0
b = []
for j in heads:
    b.append(slice(k, k + abs(j)))
    k += abs(j)

sss = 0
for segm in p:
    c = [
        (heads[i], segm[b[i]]) for i in range(len(b))
    ]

    for k, v in c:
        if k > 0:
            sss += int.from_bytes(v, byteorder='big', signed=False)
        else:
            sss += int.from_bytes(v, byteorder='big', signed=True)

print(sss)
