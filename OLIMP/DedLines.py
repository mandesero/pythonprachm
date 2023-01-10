from collections import defaultdict
import bisect
dd = defaultdict(int)

l = []

fn = 0
max_day = 1
while s := input():
    day, fine = list(map(int, s.split()))
    max_day = max(day, max_day)
    fn += fine
    l.append((day, fine))

l.sort(key=lambda x: x[1], reverse=True)
check_lst = []
st = set()
f_day = 0

for d, f in l:
    dd[d] += 1
    if dd[d] > d or d in st:
        continue
    if f_day == max_day:
        break

    if bisect.bisect(check_lst, d) < d:
        bisect.insort_left(check_lst, d)
        f_day += 1
        fn -= f
    else:
        st.add(d)

print(fn)


