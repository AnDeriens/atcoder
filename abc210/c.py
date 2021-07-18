n, k = list(map(int, input().split()))
c = list(map(int, input().split()))

s = [0] * n

init_c = {}
for j in range(k):
    if init_c.get(c[j]) == None:
        init_c[c[j]] = 1
    else: 
        init_c[c[j]] = init_c[c[j]] + 1

cnt = len(init_c)

for i in range(k, n):
    # 要素を削除
    init_c[c[i - k]] -= 1

    if init_c[c[i - k]] == 0:
        del init_c[c[i - k]]

    # 要素を追加
    if init_c.get(c[i]) == None or init_c.get(c[i]) == 0:
        init_c[c[i]] = 1
    else: 
        init_c[c[i]] += 1

    cnt = max(cnt, len(init_c))

print(cnt)
