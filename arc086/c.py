import collections
from operator import itemgetter

n, k = list(map(int, input().split()))

a = list(map(int, input().split()))
c = collections.Counter(a)
sorted_c = sorted(c.items(), key=itemgetter(1), reverse=True)

ans = 0
if len(sorted_c) > k:
    ans = sum(c for m, c in sorted_c[k:])

print(ans)
