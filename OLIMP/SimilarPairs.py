def count(arr, pref):
    cnt = 0
    for word in arr:
        if word.startswith(pref):
            cnt += 1
    return cnt


words = []

while buff := input():
    words.append(buff)

max_k = len(words[0])

while max_k > 0:
    watched = []
    for word in words:
        pref = word[:max_k]
        if pref in watched:
            continue
        if count(words, pref) % 2 != 0:
            max_k -= 1
            break
        watched.append(pref)
    else:
        break

print(max_k)
