n = int(input())

p = list(map(int, input().split()))

p_min = n + 1
cnt = 0

for x in p:
    if p_min > x:
        cnt += 1
        p_min = x

print(cnt)

