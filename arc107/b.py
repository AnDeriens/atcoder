import math

n, k = list(map(int, input().split()))

cnt_list = [0] + [0] * (2 * n)
sum_cnt = 0

for i in range(1, 2 * n + 1):
    sum_cnt += int((i - 1) * (i - 2) / 2)
    cnt_list[i] = sum_cnt

cnt = 0

for a in range(2, n * 2 + 1):
    b = a - k
    if 2 <= b and b <= 2 * n:
        cnt += cnt_list[a] * cnt_list[b]

print(cnt)
