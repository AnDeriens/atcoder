n = int(input())

a = [0] * n
a_max = [0] * n
left_max_list = [0] * n
right_max_list = [0] * n

for i in range(n):
    a[i] = int(input())

left_max = 0
right_max = 0
for i in range(n):
    left_max = max(left_max, a[i])
    right_max = max(right_max, a[n - i - 1])

    left_max_list[i] = left_max
    right_max_list[n - i - 1] = right_max

for i in range(n):
    ans = -1
    if i > 0:
        ans = max(ans, left_max_list[i - 1])
    if i < n - 1:
        ans = max(ans, right_max_list[i + 1])

    print(ans)
