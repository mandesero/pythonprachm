from collections import defaultdict

def find_end_punc(seq):
    punc = ['.', '!', '?']
    return sorted([(seq.find(i), i) for i in punc if seq.find(i) != -1])



words1 = defaultdict(int)
words2 = defaultdict(int)

p, b, g, e = input()
# pbge
# .Sf!
puncs = (p, e)
text = ""
while (buff := input().strip()):
    text += buff
#     print(f"{text = }")
#     # If we have 2 seq
#     t = find_end_punc(text)
#     if len(t) >= 2:
#
#         # if s1 is seq?
#         if t[0][1] == e:
#             s1 = text[: t[0][0] + 1].split()
#             if s1[-1][0] == g:
#                 words1[s1[-1]] += 1
#
#
#         # if s2 is seq?
#         if t[1][1] in puncs and t[0][1] == p:
#             s2 = text[t[0][0] + 1: t[1][0]].split()
#             # print(f"{s2 = }")
#             if s2[0][0] == b:
#                 words2[s2[0]] += 1
#
#     # delete s1
#         text = text[t[0][0] + 1:]
#
#     #delete not seq
#     for i in range(1, len(t)):
#         if t[i][1] not in puncs:
#             text = text[t[i][0] + 1:]
#         else:
#             break
# else:
#     t = find_end_punc(text)
#     if t and t[0][1] == e:
#         s1 = text[: t[0][0] + 1].split()
#         if s1[-1][0] == g:
#             words1[s1[-1]] += 1
#     # text = text[t[0][0] + 1:]
#
#
#
#
# t1 = max(words1.items(), key=lambda x: x[1])[1]
# t2 = max(words2.items(), key=lambda x: x[1])[1]
# a1 = 0
# a2 = 0
# for i in words1:
#     if words1[i] == t1:
#         a1 = i
#         break
#
# for i in words2:
#     if words2[i] == t2:
#         a2 = i
#         break
#
# ans = ""
# if a2:
#     ans += f"{a2} {words2[a2]} -"
# else:
#     ans += '... 0 -'
#
# if a2:
#     ans += f"{a1} {words1[a1]}"
# else:
#     ans += '... 0'
# print(ans)
#


# print(words1)
# print(words2)


seqs = []
pnc = ['.', '!', '?']
start = 0
for i, l in enumerate(text):
    if l in pnc:
        seqs.append(
            text[start: i + 1].strip()
        )
        start = i + 1
# print(*seqs, sep='\n')
if seqs[1][-1] == e:
    t = seqs[1].split()[-1]
    if t[0] == g:
        words2[g] += 1


for i in range(1, len(seqs)):
    if seqs[i][0] == b and seqs[i - 1][-1] == p:
        words1[seqs[i].split()[0]] += 1
    if seqs[i][-1] == e:
        t = seqs[i].split()[-1]
        if t[0] == g:
            words2[t] += 1


t1 = max(words1.items(), key=lambda x: x[1])[1]
t2 = max(words2.items(), key=lambda x: x[1])[1]
print(f"{t1 = } {t2 = }")
a1 = 0
a2 = 0
ans = ""

for i in words1:
    if words1[i] == t1:
        a1 = i
        break

for i in words2:
    if words2[i] == t2:
        a2 = i
        break
if a2:
    ans += f"{a1} {words1[a1]} - "
else:
    ans += '... 0 -'

if a2:
    ans += f"{a2} {words2[a2]}"
else:
    ans += '... 0'
print(ans)



print(words1)
print(words2)