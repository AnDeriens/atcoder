n = int(input())
a = list(map(int, input().split()))

dict_a = []

for i in range(n):
    dict_a.append({"key": i + 1, "value": a[i]})

a_sorted = sorted(dict_a, key=lambda x:x['value'])

ans = []
for v in a_sorted:
    ans.append(str(v['key']))

print(' '.join(ans))
